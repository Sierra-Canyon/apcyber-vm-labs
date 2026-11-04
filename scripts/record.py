"""Run one lab command and record what it printed in your evidence file.

How to use it, from anywhere inside your lab repository:

    python3 scripts/record.py 01 step2 ip -br addr

  01       the lab number, so the output goes in evidence/Lab01.md
  step2    the spot in that file, marked <!-- output: step2 -->
  the rest is the command to run, typed exactly as the lab README shows it

A command with a pipe ( | ) goes inside quotation marks, so the whole
pipeline reaches this script as one piece:

    python3 scripts/record.py 02 step7 "grep BLOCK kestrel_roastery.log | wc -l"

You see the output on the screen as it happens. When the command finishes,
the output is written into the evidence file, in a code block, right under
its marker. Running the same step again replaces what was there, so a
mistake is never stuck in the file.
"""

import subprocess
import sys
from pathlib import Path


def run_and_show(command_words):
    """Run the command, print each line as it arrives, and return all the lines."""
    # One piece (a pipeline in quotation marks) is handed to bash so the pipe works.
    # Several pieces are run directly, one word each, exactly as typed.
    if len(command_words) == 1:
        process = subprocess.Popen(["bash", "-c", command_words[0]],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    else:
        process = subprocess.Popen(command_words,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    lines = []
    try:
        for line in process.stdout:
            print(line, end="")          # show it on the screen now
            lines.append(line.rstrip("\n"))
        process.wait()
    except KeyboardInterrupt:
        # Ctrl+C stops the command. Keep whatever it printed before that.
        process.terminate()
        print("\n(stopped with Ctrl+C; keeping what printed before that)")
    return lines


def write_into_evidence(evidence_file, step, command_text, lines):
    """Put the output under the step's marker, replacing any earlier output there."""
    marker = f"<!-- output: {step} -->"
    old_lines = evidence_file.read_text().split("\n")
    new_block = ["```text", f"$ {command_text}"] + lines + ["```"]

    result = []
    i = 0
    while i < len(old_lines):
        result.append(old_lines[i])
        if old_lines[i] == marker:
            # Skip an older code block that sits right under the marker, if there is one.
            j = i + 1
            if j < len(old_lines) and old_lines[j] == "```text":
                j += 1
                while j < len(old_lines) and old_lines[j] != "```":
                    j += 1
                j += 1                   # step past the closing ```
                i = j
            else:
                i = i + 1
            result.extend(new_block)
            continue
        i += 1

    evidence_file.write_text("\n".join(result))


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 scripts/record.py <lab number> <step> <command>")
        print("Example: python3 scripts/record.py 01 step2 ip -br addr")
        sys.exit(1)

    lab_number = sys.argv[1]
    step = sys.argv[2]
    command_words = sys.argv[3:]

    # The evidence folder sits next to the scripts folder, at the top of the repository.
    repo_top = Path(__file__).resolve().parent.parent
    evidence_file = repo_top / "evidence" / f"Lab{lab_number}.md"
    if not evidence_file.exists():
        print(f"Cannot find {evidence_file}. Is the lab number right?")
        sys.exit(1)

    # Check the marker before running anything, so a typo costs nothing.
    marker = f"<!-- output: {step} -->"
    if marker not in evidence_file.read_text().split("\n"):
        print(f"There is no {marker} line in evidence/{evidence_file.name}.")
        print("Check the step name against the lab README. Nothing was run.")
        sys.exit(1)

    # sudo asks for your password. Ask now, on the screen, before the output is collected.
    first_word = command_words[0].split()[0]
    if first_word == "sudo":
        subprocess.run(["sudo", "-v"])

    lines = run_and_show(command_words)
    write_into_evidence(evidence_file, step, " ".join(command_words), lines)
    print(f"\nRecorded under {step} in evidence/{evidence_file.name}.")


main()
