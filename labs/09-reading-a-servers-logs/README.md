# Lab 09: Reading a Server's Logs

**Meeting:** 43 · Logs
**Graded:** as part of the Meeting 43 classwork.
**Turn in:** `evidence/Lab09.md` in your lab repository, pushed on the `lab09` branch with a pull request, by the end of the period.

Kestrel's store server, `203.0.113.10`, keeps two logs. Both are copied into this folder from one night, Saturday 5 December into Sunday 6 December. They are made up for this course.

| File | What it records |
|:--|:--|
| `kestrel_store_auth.log` | The authentication log: every sign-in, failed or accepted, and every `sudo` |
| `kestrel_store_firewall.log` | The network log: every connection the server's firewall allowed or blocked, with the number of the rule that decided |
| `firewall_rules.txt` | The firewall's rules, numbered |

On a real Linux server the authentication log is `/var/log/auth.log`, and reading it takes `sudo`. These copies do not.

The firewall log's columns are the date, the time, the rule number, the action, the protocol, the **source** address and **source port** (where it came from), and the **destination** address and **destination port** (where it was going).

## Step 1: Start a branch

First, on GitHub, merge the pull request **Add Lab 09** in your lab repository. Then, in the VM:

```bash
cd ~/version_control/apcyber-2026-2027-vm-labs-<your-username>
git switch main
git pull
git switch -c lab09
cd labs/09-reading-a-servers-logs
```

*You should see* `Switched to a new branch 'lab09'`. Every command below runs from this folder, so the script is `../../scripts/record.py`.

## Part 1: The authentication log

### Step 2: The last 30 lines

```bash
python3 ../../scripts/record.py 09 step2 tail -n 30 kestrel_store_auth.log
```

`tail -n 30` shows the end of a log, where the newest lines are. This file is short, so you see all of it. `lortega` is Luis Ortega, Kestrel's owner.

### Step 3: The failed sign-ins

```bash
python3 ../../scripts/record.py 09 step3 "grep 'Failed password' kestrel_store_auth.log | grep -o 'from [0-9.]*' | sort | uniq -c; grep 'Failed password' kestrel_store_auth.log | grep -o 'for .* from' | sort | uniq -c | sort -rn"
```

The first count is by address. The second is by the account each attempt tried.

### Step 4: The sign-ins that worked

```bash
python3 ../../scripts/record.py 09 step4 "grep Accepted kestrel_store_auth.log; grep sudo kestrel_store_auth.log"
```

`publickey` means the person signed in with a key file. `password` means a typed password. `sudo` lines show commands run as the administrator, `root`.

## Part 2: The network log

### Step 5: The same addresses, in the other log

```bash
python3 ../../scripts/record.py 09 step5 "grep 198.51.100.77 kestrel_store_firewall.log | head -3; grep 198.51.100.140 kestrel_store_firewall.log"
```

### Step 6: The rules

```bash
python3 ../../scripts/record.py 09 step6 cat firewall_rules.txt
```

### Step 7: What was blocked

```bash
python3 ../../scripts/record.py 09 step7 "grep BLOCK kestrel_store_firewall.log"
```

### Step 8: What left after 02:47

```bash
python3 ../../scripts/record.py 09 step8 "grep 198.51.100.23 kestrel_store_firewall.log | head -3; grep -c 198.51.100.23 kestrel_store_firewall.log; grep 198.51.100.23 kestrel_store_firewall.log | tail -1"
```

You have seen `198.51.100.23` before.

## Step 9: Answer the questions

```bash
gnome-text-editor ../../evidence/Lab09.md &
```

Every output is already in the file. Type each answer after `Answer:`, questions 1 to 12. Save with **Ctrl+S**.

## Step 10: Turn it in

Save the file first, then:

```bash
cd ../..
git add evidence/Lab09.md
git commit -m "Lab 09: evidence"
git push -u origin lab09
gh pr create --fill --base main --reviewer jd12
```

*You should see* a link to your pull request. Do not merge it.

## If it broke

| You see | Fix |
|:--|:--|
| `tail: cannot open 'kestrel_store_auth.log'` | Run the `cd labs/09-reading-a-servers-logs` line from Step 1. If it still fails, merge **Add Lab 09** on GitHub, then `git switch main`, `git pull`, `git switch lab09`, `git merge --no-edit main`. |
| A `grep` prints nothing | Check the address or word. Copy the command from this README. |
| `python3: can't open file` | From the lab folder the script is `../../scripts/record.py`. |
| The editor says the file changed on disk | Choose **Reload**. |
