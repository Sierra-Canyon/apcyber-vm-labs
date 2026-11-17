# Lab 5.5: Lying About Names, and Drowning the Server

**Meeting:** 35 · DNS Poisoning, DoS and DDoS
**Graded:** as part of the Meeting 35 classwork.
**Turn in:** `evidence/Lab05.5.md` in your lab repository, pushed on the `lab05.5` branch with a pull request, by the end of the period.

Lab 5.5 sits between Labs 05 and 06. Part 1 is Riverside Clinic's monitoring system: five alerts, each with the lines that set it off. You read them and name the attack. Part 2 poisons one name on your own VM, then puts it back.

## Lab rules

- Analyze only what you are given. Every alert in Part 1 is made up for this course.
- Part 2 changes one file on your own VM and nothing else. Never change name lookups on a computer or network you do not own.
- Curiosity is not authorization.

## Step 1: Start a branch

First, on GitHub, merge the pull request **Add Lab 5.5** in your lab repository. Then, in the VM, with your own GitHub username in place of `<your-username>`:

```bash
cd ~/version_control/apcyber-2026-2027-vm-labs-<your-username>
git switch main
git pull
git switch -c lab05.5
cd labs/05.5-lying-about-names
gnome-text-editor ../../evidence/Lab05.5.md &
```

*You should see* `Switched to a new branch 'lab05.5'`, then the evidence file opens. Every command below runs from this folder, so the script is `../../scripts/record.py`. The lab number is `05.5`.

## Part 1: Read the alerts

### Step 2: Five alerts

The alerts are in Part 1 of `evidence/Lab05.5.md`. An alert is a claim. The lines under it are the evidence. For each one, name the attack, copy the line that proves it, and say which leg of the CIA triad it breaks. Alert 1 is done together, on the screen.

Type each answer after `Answer:` and save with **Ctrl+S**. Part 1 has no commands.

## Part 2: Poison one name, on your own VM

DNS poisoning makes a name lead to the wrong address. Your VM checks one file, `/etc/hosts`, before it asks any DNS server. You will add one wrong line to that file on your own VM, see where the name goes, and take the line out again.

### Step 3: Where does the name go now?

```bash
python3 ../../scripts/record.py 05.5 step3 getent hosts neverssl.com
```

*You should see* one line: a real internet address, then `neverssl.com`.

### Step 4: Add one wrong line

`sudo` asks for your VM password first, so give it now:

```bash
sudo -v
python3 ../../scripts/record.py 05.5 step4 "echo '127.0.0.1 neverssl.com' | sudo tee -a /etc/hosts"
```

*You should see* `127.0.0.1 neverssl.com` printed back. `127.0.0.1` is the VM itself.

### Step 5: Where does the name go now?

```bash
python3 ../../scripts/record.py 05.5 step5 getent hosts neverssl.com
```

### Step 6: Try to reach it

```bash
python3 ../../scripts/record.py 05.5 step6 "curl -sS -m 5 http://neverssl.com | head -3"
```

Then open **Firefox** in the VM and go to `http://neverssl.com`. Note what the page says.

### Step 7: Take the line out, and check

```bash
python3 ../../scripts/record.py 05.5 step7 "sudo sed -i '/neverssl.com/d' /etc/hosts; getent hosts neverssl.com"
```

*You should see* a real internet address again.

## Step 8: Answer the questions

Every output is already in the file. Type each answer after `Answer:`, questions 1 to 16 in Part 1 and 17 to 21 in Part 2. Save with **Ctrl+S**.

## Step 9: Turn it in

Save the file first, then:

```bash
cd ../..
git add evidence/Lab05.5.md
git commit -m "Lab 5.5: evidence"
git push -u origin lab05.5
gh pr create --fill --base main --reviewer jd12
```

*You should see* a link to your pull request. Do not merge it.

## If it broke

| You see | Fix |
|:--|:--|
| `Cannot find .../evidence/Lab05.5.md` | Merge **Add Lab 5.5** on GitHub, then `git switch main`, `git pull`, `git switch lab05.5`, `git merge --no-edit main`. |
| `There is no <!-- output: step3 --> line` | The lab number or step name is typed wrong. The lab number is `05.5`. Copy the command from this README. |
| `cd: labs/05.5-lying-about-names: No such file or directory` | Same fix as the first row. |
| Step 3 prints nothing | The VM has no internet. Check that the network is on, then run Step 3 again. |
| Firefox still shows the page in Step 6 | It is showing a saved copy. Press **Ctrl+Shift+R** to reload it. |
| Step 7 still shows `127.0.0.1` | Run Step 7 again. Then `cat /etc/hosts`: no line should mention `neverssl.com`. |
| The editor says the file changed on disk | Choose **Reload**. |
