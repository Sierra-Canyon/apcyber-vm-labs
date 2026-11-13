# Lab 08: A Firewall on Your VM

**Meetings:** 40, 41, and 42 · Firewalls
**Graded:** as part of the classwork for each of the three meetings.
**Turn in:** `evidence/Lab08.md` in your lab repository, on the `lab08` branch. Open the pull request at the end of Meeting 40, then push to it again at the end of Meetings 41 and 42.

A firewall reads a list of rules from the top, and the first rule that matches a packet decides what happens to it. This lab runs over three meetings:

| Meeting | Part | What you do |
|:--|:--|:--|
| 40 | Part 1 | Trace twelve packets through Kestrel's store firewall on paper, then turn on `ufw`, the firewall built into Ubuntu, and watch it block your own Mac |
| 41 | Part 2 | Watch rule order decide in `ufw`, then write the web store's rules yourself |
| 42 | Part 3 | Write egress rules: rules for what leaves |

Every test in this lab goes between your own Mac and your own VM. To your VM, your Mac is `192.168.64.1`. The commands use `192.168.64.2` for the VM, from Lab 01. If yours is different, type yours.

## Part 1 (Meeting 40): Rules from the top

### Step 1: Start a branch

First, on GitHub, merge the pull request **Add Lab 08** in your lab repository. Then, in the VM:

```bash
cd ~/version_control/apcyber-2026-2027-vm-labs-<your-username>
git switch main
git pull
git switch -c lab08
cd labs/08-a-firewall-on-your-vm
```

*You should see* `Switched to a new branch 'lab08'`. Every command below runs from this folder, so the script is `../../scripts/record.py`. A second tab opened with **Ctrl+Shift+T** starts in the same folder.

### Step 2: Trace twelve packets

These are the inbound rules on Kestrel's store firewall. The store server is `203.0.113.10`, the cafe DNS server is `203.0.113.53`, and the roastery is `192.168.10.0/24`. `any` means any address or any port.

| Rule | Action | Protocol | From | To | Port |
|--:|:--|:--|:--|:--|:--|
| 1 | Allow | TCP | any | 203.0.113.10 | 443 |
| 2 | Allow | TCP | any | 203.0.113.10 | 80 |
| 3 | Block | TCP | any | 203.0.113.10 | 22 |
| 4 | Allow | TCP | 198.51.100.40 | 203.0.113.10 | 22 |
| 5 | Allow | TCP | 192.168.10.0/24 | 203.0.113.10 | 3306 |
| 6 | Block | TCP | 198.51.100.0/24 | any | 3389 |
| 7 | Allow | UDP | any | 203.0.113.53 | 53 |
| 8 | Allow | ICMP | 192.168.10.0/24 | any | any |
| 9 | Block | any | any | any | any |

Read each packet in the evidence file against the rules from the top. The first rule that matches decides. Write the rule number and Allow or Block.

### Step 3: Your VM's firewall now

```bash
python3 ../../scripts/record.py 08 step3 sudo ufw status verbose
```

### Step 4: Start a small web server

Open a second tab with **Ctrl+Shift+T**:

```bash
python3 -m http.server 8080
```

Leave it running. Each request it gets prints a line here.

### Step 5: Reach it from your Mac

On your **Mac**, open the Terminal app (Finder, Applications, Utilities) and type:

```bash
curl -m 3 http://192.168.64.2:8080
```

*You should see* a short web page that lists the files in your lab folder, and a new line in the VM's second tab with `192.168.64.1` at the start. Write down what happened for question 3.

### Step 6: Turn the firewall on

Back in the VM's first tab:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
python3 ../../scripts/record.py 08 step6 sudo ufw status verbose
```

`sudo ufw enable` asks `Command may disrupt existing ssh connections. Proceed with operation (y|n)?` Type `y` and press **Enter**. It answers `Firewall is active and enabled on system startup`.

Run the same `curl` on your Mac again. Wait the three seconds.

### Step 7: What the firewall wrote down

```bash
python3 ../../scripts/record.py 08 step7 "sudo journalctl -k --no-pager | grep 'DPT=8080' | tail -n 3"
```

Each line is a packet the firewall blocked. `SRC` is where it came from and `DPT` is the port it was for.

### Step 8: Open one door

```bash
sudo ufw allow 8080/tcp
python3 ../../scripts/record.py 08 step8 sudo ufw status numbered
```

Run the `curl` on your Mac a third time.

### Step 9: Turn in Part 1

Open the evidence file:

```bash
gnome-text-editor ../../evidence/Lab08.md &
```

Answer questions 1 to 6 and the Part 1 table, save with **Ctrl+S**, then:

```bash
git add ../../evidence/Lab08.md
git commit -m "Lab 08: Part 1"
git push -u origin lab08
gh pr create --fill --base main --reviewer jd12
```

Leave the firewall on. Part 2 starts from here.

## Part 2 (Meeting 41): Rule order

Start the web server again in a second tab if it is not running (`python3 -m http.server 8080`), and in the first tab `cd` to your lab folder, `~/version_control/apcyber-2026-2027-vm-labs-<your-username>/labs/08-a-firewall-on-your-vm`.

### Step 10: A Block rule at the top

```bash
sudo ufw insert 1 deny from 192.168.64.1 to any port 8080 proto tcp
python3 ../../scripts/record.py 08 step10 sudo ufw status numbered
```

Run the `curl` on your Mac.

### Step 11: The same Block rule at the bottom

Remove rule 1, then add the same rule again without `insert`, so it goes at the end:

```bash
sudo ufw --force delete 1
sudo ufw deny from 192.168.64.1 to any port 8080 proto tcp
python3 ../../scripts/record.py 08 step11 sudo ufw status numbered
```

Run the `curl` on your Mac again.

### Step 12: Write the web store's rules

Kestrel's owner wrote down what the store server needs, in plain English:

1. Customers anywhere reach the store over HTTPS. Anyone who types plain `http://` is let in on port 80 so the server can send them on to HTTPS.
2. The owner, Luis Ortega, manages the server over SSH, only from his home address, `198.51.100.40`.
3. Staff computers at the roastery, `192.168.10.0/24`, reach the order database on the store server on port 3306. Nobody else does.
4. Nothing else gets in.

Write the rules in the Part 2 table of your evidence file. Then answer questions 7 to 10, save, and push:

```bash
git add ../../evidence/Lab08.md
git commit -m "Lab 08: Part 2"
git push
```

## Part 3 (Meeting 42): What leaves

Firewalls usually let everything out. In Lab 02, the bookkeeper's laptop called `198.51.100.23` every four minutes, all night, and the router let every one of those calls leave. An egress rule is a rule for what leaves.

Start in your lab folder, as in Part 2, with the web server running in a second tab.

### Step 13: Out, before

```bash
python3 ../../scripts/record.py 08 step13 "curl -s -m 5 -o /dev/null -w '%{http_code}\n' http://neverssl.com"
```

`200` means the page came back.

### Step 14: Block web traffic leaving

```bash
sudo ufw deny out 80/tcp
python3 ../../scripts/record.py 08 step14 "curl -s -m 5 -o /dev/null -w '%{http_code}\n' http://neverssl.com; sudo ufw status numbered"
```

`000` means nothing came back. Now take that rule out again, so your VM can reach the web:

```bash
sudo ufw delete deny out 80/tcp
```

### Step 15: The rule Kestrel needed

```bash
sudo ufw deny out to 198.51.100.23
python3 ../../scripts/record.py 08 step15 sudo ufw status numbered
```

### Step 16: Put your VM back

Stop the web server in the second tab with **Ctrl+C**. Then, in the first tab:

```bash
sudo ufw --force reset
python3 ../../scripts/record.py 08 step16 sudo ufw status
```

*You should see* `Status: inactive`. Answer questions 11 to 13, save, and push:

```bash
git add ../../evidence/Lab08.md
git commit -m "Lab 08: Part 3"
git push
```

## If it broke

| You see | Fix |
|:--|:--|
| `curl: (7) Failed to connect` from the Mac before Step 6 | The web server is not running. Start it in the second tab. |
| `curl: (28) Connection timed out` | The firewall dropped it. That is what Step 6 is supposed to show. |
| Step 7 prints nothing | Run the Mac's `curl` again, then Step 7 again. |
| `ERROR: Could not delete non-existent rule` | Check the rule numbers with `sudo ufw status numbered`. |
| `python3: can't open file` | From the lab folder the script is `../../scripts/record.py`. Run the `cd labs/08-a-firewall-on-your-vm` line from Step 1. |
| `OSError: [Errno 98] Address already in use` | The web server is already running in another tab. Use that one. |
| Your VM cannot reach the internet after Part 3 | Run Step 16. `sudo ufw --force reset` turns the firewall off and removes every rule you added. |
