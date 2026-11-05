# Lab 02: Ports and the Log

**Meeting:** 31 · Ports and the Log
**Graded:** as part of the Meeting 31 classwork.
**Turn in:** `evidence/Lab02.md` in your lab repository, pushed on the `lab02` branch with a pull request, by the end of the period.

Every command in this lab runs in your VM. You need your interface name and gateway from Lab 01. Each step that prints something you need runs through `scripts/record.py`, which writes the output into your evidence file. You answer the questions in that file at the end.

## Step 1: Start a branch

With your own GitHub username in place of `<your-username>`:

```bash
cd ~/version_control/apcyber-2026-2027-vm-labs-<your-username>
git switch main
git switch -c lab02
```

*You should see* `Switched to a new branch 'lab02'`. Every command below runs from this folder until Part 2 says otherwise.

## Part 1: Your VM

### Step 2: What is listening

```bash
python3 scripts/record.py 02 step2 ss -tuln
```

Each line is a port a program on your VM is listening on. `Netid` says TCP or UDP. `Local Address:Port` says the address and the port.

### Step 3: ICMP

In a second tab (**Ctrl+Shift+T**):

```bash
python3 scripts/record.py 02 step3 sudo tcpdump -n -l -c 2 -i any icmp
```

It asks for your password, then waits. It stops by itself after two packets.

In the first tab, with your gateway from Lab 01:

```bash
ping -c 3 192.168.64.1
```

*You should see* (one Mac with UTM):

```
05:59:12.349152 enp0s1 Out IP 192.168.64.2 > 192.168.64.1: ICMP echo request, id 988, seq 1, length 64
05:59:12.349312 enp0s1 In  IP 192.168.64.1 > 192.168.64.2: ICMP echo reply, id 988, seq 1, length 64
```

### Step 4: DNS

Second tab:

```bash
python3 scripts/record.py 02 step4 sudo tcpdump -n -l -c 2 -i any udp port 53
```

First tab:

```bash
resolvectl query wikipedia.org
```

In the capture, a question line has `A?` in it. *You should see* a line like this one (one Mac with UTM):

```
06:23:24.861593 enp0s1 Out IP 192.168.64.2.53462 > 192.168.64.1.53: 64219+ [1au] A? example.com. (52)
```

The number after the last dot of an address is the port: `192.168.64.2.53462` is address `192.168.64.2`, port `53462`.

### Step 5: TCP

Close any web browser in the VM. Second tab:

```bash
python3 scripts/record.py 02 step5 sudo tcpdump -n -l -i any -c 3 tcp port 443
```

First tab:

```bash
wget -q --spider https://www.wikipedia.org
```

The capture stops by itself after three packets. *You should see* (one Mac with UTM):

```
05:59:08.247789 enp0s1 Out IP 192.168.64.2.59936 > 151.101.64.223.443: Flags [S], seq 3340976614, win 65280, options [mss 1360,sackOK,TS val 1429942066 ecr 0,nop,wscale 10], length 0
05:59:08.247959 enp0s1 In  IP 151.101.64.223.443 > 192.168.64.2.59936: Flags [S.], seq 1125544719, ack 3340976615, win 43440, options [mss 1460,sackOK,TS val 3676738178 ecr 1429942066,nop,wscale 7], length 0
05:59:08.247974 enp0s1 Out IP 192.168.64.2.59936 > 151.101.64.223.443: Flags [.], ack 1, win 64, options [nop,nop,TS val 1429942066 ecr 3676738178], length 0
```

## Part 2: Kestrel's log

`kestrel_roastery.log` is the log file from the router at Kestrel's roastery, for one night. The first line names the columns. Every line after it is one connection.

```bash
cd labs/02-ports-and-the-log
head -5 kestrel_roastery.log
```

The rest of the lab runs from this folder. `record.py` still finds your evidence file from here, as `../../scripts/record.py`.

### Step 6: Count it

Three counts in one step. The quotation marks keep them together:

```bash
python3 ../../scripts/record.py 02 step6 "wc -l kestrel_roastery.log; grep -c BLOCK kestrel_roastery.log; grep -c ACCEPT kestrel_roastery.log"
```

### Step 7: What was knocked on

This pipes the blocked lines into `cut`, which keeps column 6, the port. `sort | uniq -c` counts each port. A command with pipes goes inside double quotation marks.

```bash
python3 ../../scripts/record.py 02 step7 "grep BLOCK kestrel_roastery.log | cut -d' ' -f6 | sort | uniq -c | sort -rn"
```

Use the port card at the bottom of this README for question 12.

### Step 8: Who knocked

Change the column to 3, the source address.

```bash
python3 ../../scripts/record.py 02 step8 "grep BLOCK kestrel_roastery.log | cut -d' ' -f3 | sort | uniq -c"
```

### Step 9: What got in from outside

Every address inside Kestrel starts `192.168.10.`. This keeps columns 2, 3, and 6 (time, source address, port) of the accepted lines, then drops the ones from inside:

```bash
python3 ../../scripts/record.py 02 step9 "grep ACCEPT kestrel_roastery.log | cut -d' ' -f2,3,6 | grep -v ' 192\.168\.10\.'"
```

### Step 10: The bookkeeper's laptop

The bookkeeper's laptop is `192.168.10.47`. Look at where it connected.

```bash
python3 ../../scripts/record.py 02 step10 "grep 192.168.10.47 kestrel_roastery.log | cut -d' ' -f5 | sort | uniq -c; grep 198.51.100.23 kestrel_roastery.log | head -3; grep 198.51.100.23 kestrel_roastery.log | tail -1"
```

## Step 11: Answer the questions

```bash
gnome-text-editor ../../evidence/Lab02.md &
```

Every output is already in the file. Type each answer after `Answer:`, questions 1 to 19. Save with **Ctrl+S**.

## Step 12: Turn it in

Save the file first, then:

```bash
cd ../..
git add evidence/Lab02.md
git commit -m "Lab 02: evidence"
git push -u origin lab02
gh pr create --fill --base main --reviewer jd12
```

*You should see* a link to your pull request. Do not merge it.

## If it broke

| You see | Fix |
|:--|:--|
| `tcpdump: any: You don't have permission to perform this capture on that device` | Put `sudo` in front of `tcpdump`. |
| `grep: kestrel_roastery.log: No such file or directory` | Run the `cd` line at the top of Part 2, then try again. |
| `python3: can't open file` | In Part 1 the script is `scripts/record.py`. In Part 2, from the lab folder, it is `../../scripts/record.py`. |
| `There is no <!-- output: step7 --> line` | The step name is typed wrong. Copy the command from this README. |
| A capture never stops | Close the browser, press **Ctrl+C**, start the capture again, then run the command in the first tab again. |

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
