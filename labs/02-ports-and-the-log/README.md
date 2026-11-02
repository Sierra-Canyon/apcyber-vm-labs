# Lab 02: Ports and the Log

**Meeting:** 30 · Ports and the Log
**Graded:** as part of the Meeting 30 classwork.
**Turn in:** the Lab 02 record sheet, by hand, at the end of the period. Nothing is uploaded.

Every command in this lab runs in your VM. You need your interface name and gateway from Lab 01. Write each answer on your record sheet as you go.

## Step 1: Get today's file

```bash
cd ~/version_control/apcyber-vm-labs && git pull
```

*You should see* `labs/02-ports-and-the-log/kestrel_roastery.log` in the list of changed files, or `Already up to date.`

## Part 1: Your VM

### Step 2: What is listening

```bash
ss -tuln
```

Each line is a port a program on your VM is listening on. `Netid` says TCP or UDP. `Local Address:Port` says the address and the port.

**Sheet, line 1:** how many lines start with `tcp`, and how many with `udp`. **Line 2:** copy one line whose port is `53`. **Line 3:** the address on that line.

### Step 3: ICMP

In a second tab (**Ctrl+Shift+T**):

```bash
sudo tcpdump -n -i any icmp
```

In the first tab, with your gateway from Lab 01:

```bash
ping -c 3 192.0.2.1
```

*You should see* (different machine):

```
05:59:12.349152 eth0  Out IP 192.0.2.2 > 192.0.2.1: ICMP echo request, id 988, seq 1, length 64
05:59:12.349312 eth0  In  IP 192.0.2.1 > 192.0.2.2: ICMP echo reply, id 988, seq 1, length 64
```

Press **Ctrl+C** in the second tab.

**Sheet, line 4:** the words after `ICMP` on the line going out, and on the line coming back.

### Step 4: DNS

Second tab:

```bash
sudo tcpdump -n -i any udp port 53
```

First tab:

```bash
resolvectl query wikipedia.org
```

In the capture, a question line has `A?` in it. *You should see* a line like this one (different machine):

```
06:23:24.861593 eth0  Out IP 192.0.2.2.53462 > 8.8.8.8.53: 64219+ [1au] A? example.com. (52)
```

The number after the last dot of an address is the port: `192.0.2.2.53462` is address `192.0.2.2`, port `53462`. Press **Ctrl+C**.

**Sheet, line 5:** copy one question line. **Line 6:** the port the question went to. **Line 7:** which protocol carried it. The capture filter you typed tells you.

### Step 5: TCP

Close any web browser in the VM. Second tab:

```bash
sudo tcpdump -n -i any -c 3 tcp port 443
```

First tab:

```bash
wget -q --spider https://www.wikipedia.org
```

The capture stops by itself after three packets. *You should see* (different machine):

```
05:59:08.247789 eth0  Out IP 192.0.2.2.59936 > 151.101.64.223.443: Flags [S], seq 3340976614, win 65280, options [mss 1360,sackOK,TS val 1429942066 ecr 0,nop,wscale 10], length 0
05:59:08.247959 eth0  In  IP 151.101.64.223.443 > 192.0.2.2.59936: Flags [S.], seq 1125544719, ack 3340976615, win 43440, options [mss 1460,sackOK,TS val 3676738178 ecr 1429942066,nop,wscale 7], length 0
05:59:08.247974 eth0  Out IP 192.0.2.2.59936 > 151.101.64.223.443: Flags [.], ack 1, win 64, options [nop,nop,TS val 1429942066 ecr 3676738178], length 0
```

**Sheet, line 8:** the `Flags` on each of the three lines, in order. **Line 9:** how much data the three packets carried. Look at `length`.

## Part 2: Kestrel's log

`kestrel_roastery.log` is the log file from the router at Kestrel's roastery, for one night. The first line names the columns. Every line after it is one connection.

```bash
cd ~/version_control/apcyber-vm-labs/labs/02-ports-and-the-log
head -5 kestrel_roastery.log
```

### Step 6: Count it

```bash
wc -l kestrel_roastery.log
grep -c BLOCK kestrel_roastery.log
grep -c ACCEPT kestrel_roastery.log
```

**Sheet, line 10:** the three numbers.

### Step 7: What was knocked on

This pipes the blocked lines into `cut`, which keeps column 6, the port. `sort | uniq -c` counts each port.

```bash
grep BLOCK kestrel_roastery.log | cut -d' ' -f6 | sort | uniq -c | sort -rn
```

**Sheet, lines 11 and 12:** the port blocked most often, and the program it belongs to. Use the port card on your sheet.

### Step 8: Who knocked

Change the column to 3, the source address.

```bash
grep BLOCK kestrel_roastery.log | cut -d' ' -f3 | sort | uniq -c
```

**Sheet, line 13:** each address and its count.

### Step 9: What got in from outside

Every address inside Kestrel starts `192.168.10.`. This keeps columns 2, 3, and 6 (time, source address, port) of the accepted lines, then drops the ones from inside:

```bash
grep ACCEPT kestrel_roastery.log | cut -d' ' -f2,3,6 | grep -v ' 192\.168\.10\.'
```

**Sheet, line 14:** the time, the address, and the port. **Line 15:** the program on that port.

### Step 10: The bookkeeper's laptop

The bookkeeper's laptop is `192.168.10.47`. Look at where it connected.

```bash
grep 192.168.10.47 kestrel_roastery.log | cut -d' ' -f5 | sort | uniq -c
grep 198.51.100.23 kestrel_roastery.log | head -3
grep 198.51.100.23 kestrel_roastery.log | tail -1
```

**Sheet, lines 16 to 18:** how many times it connected to `198.51.100.23`, the first and last times, and how far apart the connections are. **Line 19:** which kill chain stage this looks like, and why.

## If it broke

| You see | Fix |
|:--|:--|
| `tcpdump: any: You don't have permission to perform this capture on that device` | Put `sudo` in front of the command. |
| `grep: kestrel_roastery.log: No such file or directory` | Run the `cd` line at the top of Part 2, then try again. |
| `Already up to date.` and no `labs/02-ports-and-the-log` folder | Check that you are in `~/version_control/apcyber-vm-labs`, then run `git pull` again. |
| The TCP capture never stops | Close the browser, press **Ctrl+C**, and start the capture again before running `wget`. |

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
