# Lab 03: What Anyone on Your Network Can Read

**Meeting:** 32 · Eavesdropping
**Graded:** as part of the Meeting 32 classwork.
**Turn in:** `evidence/Lab03.md` in your lab repository, pushed on the `lab03` branch with a pull request, by the end of the period.

This lab opens a packet capture: a saved recording of the traffic on a network. Nothing in it is live, and you capture nothing today. `01_cleartext_vs_tls.pcap` was recorded on the network at Riverside Clinic, which is made up for this course. One person, jrivera, signs in to two of the clinic's websites. The first sign-in uses HTTP. The second uses HTTPS.

You read the file two ways. **Wireshark** shows each packet on the screen. `tcpdump`, run through `scripts/record.py`, writes what you found into your evidence file.

## Step 1: Get ready

**1a. Start a branch.** First, on GitHub, merge the pull request **Add Lab 03** in your lab repository. Then, in the VM, with your own GitHub username in place of `<your-username>`:

```bash
cd ~/version_control/apcyber-2026-2027-vm-labs-<your-username>
git switch main
git pull
git switch -c lab03
cd labs/03-what-anyone-can-read
```

*You should see* `Switched to a new branch 'lab03'`. Every command below runs from this folder. The script is `../../scripts/record.py` from here, as in Part 2 of Lab 02.

**1b. Install Wireshark.** Check whether it is already there:

```bash
wireshark --version
```

If it prints a version number, go on to Step 2. If it says `command not found`, install it:

```bash
sudo apt update
sudo apt install -y wireshark
```

It asks for your password. Partway through, a screen asks **Should non-superusers be able to capture packets?** **<No>** is already highlighted. Press **Enter**. You only open files in this lab. The install takes a few minutes.

*You should see* the prompt come back. Run `wireshark --version` again: it prints a version number.

## Step 2: Sign the lab rules

```bash
gnome-text-editor ../../evidence/Lab03.md &
```

The lab rules are at the top of the evidence file. Read them, type your full name after `Signed:`, and save with **Ctrl+S**. Leave the editor open. Do not open the capture until you have signed.

## Part 1: The whole conversation

### Step 3: List every packet

```bash
python3 ../../scripts/record.py 03 step3 tcpdump -nn -r 01_cleartext_vs_tls.pcap
```

No `sudo` this time. Reading a file is not capturing. Each line is one packet. The first line says which file it read. Your times may differ from the sample, because the VM shows them in its own time zone.

*You should see* 19 packet lines that start like these:

```
01:54:00.000000 IP 192.168.10.47.54053 > 203.0.113.10.80: Flags [S], seq 1000, win 8192, length 0
01:54:00.021000 IP 203.0.113.10.80 > 192.168.10.47.54053: Flags [S.], seq 5000, ack 1001, win 8192, length 0
```

### Step 4: Open it in Wireshark

```bash
wireshark 01_cleartext_vs_tls.pcap &
```

Each row is one packet. Click a row, and the middle pane shows that packet's layers: Ethernet, IP, TCP, and what it carried. Use the port card at the bottom of this README for question 2.

## Part 2: The HTTP sign-in

### Step 5: Read the password

In Wireshark, type `http` in the display filter bar at the top and press **Enter**. Two packets are left. Click the one that says `POST /login`. Then right-click it and choose **Follow** > **TCP Stream**. Wireshark puts the whole conversation in one window: what the laptop sent in red, and what the server sent back in blue.

Close that window, clear the filter, and record the same lines:

```bash
python3 ../../scripts/record.py 03 step5 "tcpdump -nn -A -r 01_cleartext_vs_tls.pcap port 80 | grep -a -E 'POST|Host|username|Set-Cookie'"
```

`-A` prints what each packet carried as text. `grep` keeps the four lines that matter. In the password, `%21` is how a web form writes `!`.

## Part 3: The HTTPS sign-in

### Step 6: Try the same thing on port 443

In Wireshark, type `tls` in the filter bar and press **Enter**. Right-click any packet, then **Follow** > **TCP Stream**. Compare it with the HTTP stream.

### Step 7: What HTTPS still shows

Clear the filter. Click the packet whose Info column says `Client Hello`. In the middle pane, open **Transport Layer Security** > **Handshake Protocol: Client Hello**, then the **Extension: server_name** line. The laptop sent the site's name before the encryption started.

Record it. Every web name in this course's files ends in `.example`. The second command counts how many port 443 lines contain the word `password`:

```bash
python3 ../../scripts/record.py 03 step7 "tcpdump -nn -A -r 01_cleartext_vs_tls.pcap port 443 | grep -a -o '[a-z][a-z.-]*\.example'; tcpdump -nn -A -r 01_cleartext_vs_tls.pcap port 443 | grep -a -c password"
```

## Step 8: Answer the questions

Go back to the editor. Every output is already in the file. If the editor says the file changed on disk, choose **Reload**. Type each answer after `Answer:`, questions 1 to 10, then A to C in Part 4. Save with **Ctrl+S**.

## Step 9: Turn it in

Save the file first, then:

```bash
cd ../..
git add evidence/Lab03.md
git commit -m "Lab 03: evidence"
git push -u origin lab03
gh pr create --fill --base main --reviewer jd12
```

*You should see* a link to your pull request. Do not merge it.

## If it broke

| You see | Fix |
|:--|:--|
| `wireshark: command not found` | Step 1b did not finish. Run `sudo apt update`, then `sudo apt install -y wireshark`, and choose **No** for non-superusers. |
| `tcpdump: 01_cleartext_vs_tls.pcap: No such file or directory` | Run the `cd labs/03-what-anyone-can-read` line from Step 1a. If it still fails, merge the **Add Lab 03** pull request on GitHub, then `git switch main`, `git pull`, `git switch lab03`, `git merge --no-edit main`. |
| `python3: can't open file` | From the lab folder the script is `../../scripts/record.py`. |
| `There is no <!-- output: step5 --> line` | The step name is typed wrong, or `evidence/Lab03.md` is missing. Copy the command from this README. |
| The Wireshark window never appears | Press **Enter** in the terminal. The `&` lets the terminal keep working while Wireshark opens. |
| Follow is greyed out | Click a packet first, then right-click that packet. |
| The editor says the file changed on disk | Choose **Reload**. Your name is saved if you pressed **Ctrl+S** in Step 2. |

## Port card

| Port | Program |
|--:|:--|
| 20, 21 | FTP, file transfer |
| 22 | SSH, remote sign-in |
| 23 | Telnet, remote sign-in with no encryption |
| 25 | SMTP, sending email |
| 53 | DNS |
| 80 | HTTP, web pages |
| 110 | POP3, collecting email |
| 443 | HTTPS, secure web pages |
| 3306 | MySQL, a database |
| 3389 | RDP, remote desktop |
