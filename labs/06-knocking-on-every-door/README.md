# Lab 06: Knocking on Every Door

**Meeting:** 36 · Port Scans
**Graded:** as part of the Meeting 36 classwork.
**Turn in:** `evidence/Lab06.md` in your lab repository, pushed on the `lab06` branch with a pull request, by the end of the period.

A port scan knocks on one door after another and writes down which ones answer. `03_port_scan.pcap` was recorded at Riverside Clinic. It is made up for this course. The laptop at 192.168.10.66, the one from Lab 05, knocks on twenty ports of jrivera's workstation at 192.168.10.47. Then it goes back to one door that answered. Part 2 is a vulnerability scanner's report on Kestrel's store server.

You read the capture, and you scan nothing. Pointing a scanner at a device you do not own is against the lab rules you signed in Lab 03, and against the law.

## Step 1: Start a branch

First, on GitHub, merge the pull request **Add Lab 06** in your lab repository. Then, in the VM, with your own GitHub username in place of `<your-username>`:

```bash
cd ~/version_control/apcyber-2026-2027-vm-labs-<your-username>
git switch main
git pull
git switch -c lab06
cd labs/06-knocking-on-every-door
```

*You should see* `Switched to a new branch 'lab06'`. Every command below runs from this folder, so the script is `../../scripts/record.py`.

## Part 1: The scan

### Step 2: Every knock and every answer

```bash
python3 ../../scripts/record.py 06 step2 tcpdump -nn -r 03_port_scan.pcap
```

Every line from `192.168.10.66` is a knock. Every line from `192.168.10.47` is an answer. The number after the last dot of `192.168.10.47` is the port being knocked on. Look at the flags in each answer: some ports answer one way, and a few answer another.

### Step 3: The doors that opened

```bash
wireshark 03_port_scan.pcap &
```

Type `tcp.flags.syn == 1 && tcp.flags.ack == 1` in the filter bar and press **Enter**. That keeps only the answers that carry both SYN and ACK. Then record the same thing:

```bash
python3 ../../scripts/record.py 06 step3 "tcpdump -nn -r 03_port_scan.pcap 'tcp[tcpflags] & (tcp-syn|tcp-ack) == (tcp-syn|tcp-ack)'"
```

Use the port card at the bottom of this README to name each program.

### Step 4: What one door said about itself

After the scan, the laptop went back to one open port and finished the handshake. The workstation's first message gave away the program behind that port, and its version. That first message is the banner.

```bash
python3 ../../scripts/record.py 06 step4 "tcpdump -nn -A -r 03_port_scan.pcap port 22 | grep -a SSH-"
```

In Wireshark, filter `ssh` and click the one packet to see the same line.

## Part 2: The scanner report

Kestrel paid for a vulnerability scan of its store server, 203.0.113.10, from outside the network. This is the report.

| # | Finding |
|:--|:--|
| 1 | Port 23 is open. Telnet answers with a sign-in prompt for the server's admin account. |
| 2 | Port 3306 is open to the internet. The store's MySQL database accepts connections from any address. |
| 3 | The sign-in page at `/admin` accepts the user name `admin` with the password `admin`. |
| 4 | Port 22 is open. The SSH banner names a version with a published weakness that needs a valid account to use. |
| 5 | Port 80 serves the customer sign-in page without moving visitors to HTTPS first. |
| 6 | The web server's banner names its program and version: `nginx/1.18.0`. |
| 7 | The HTTPS certificate expires in 21 days. |

Rate each finding **High**, **Medium**, or **Low**:

- **High:** someone on the internet could get in, take data, or read passwords now, with no other step.
- **Medium:** it is a real weakness, but using it takes something else first, such as an account, or a person on the same network.
- **Low:** it gives away information or will cause trouble later, but does not let anyone in by itself.

Your reason matters more than your rating. A good reason names what an attacker could do.

## Step 5: Answer the questions

```bash
gnome-text-editor ../../evidence/Lab06.md &
```

Every output is already in the file. Type each answer after `Answer:`, questions 1 to 9, then the ratings table and questions A and B in Part 2. Save with **Ctrl+S**.

## Step 6: Turn it in

Save the file first, then:

```bash
cd ../..
git add evidence/Lab06.md
git commit -m "Lab 06: evidence"
git push -u origin lab06
gh pr create --fill --base main --reviewer jd12
```

*You should see* a link to your pull request. Do not merge it.

## If it broke

| You see | Fix |
|:--|:--|
| `tcpdump: 03_port_scan.pcap: No such file or directory` | Run the `cd labs/06-knocking-on-every-door` line from Step 1. If it still fails, merge **Add Lab 06** on GitHub, then `git switch main`, `git pull`, `git switch lab06`, `git merge --no-edit main`. |
| `tcpdump: syntax error` in Step 3 | The whole command after `step3` goes inside double quotation marks, and the filter inside single ones. Copy it from this README. |
| The Wireshark filter bar turns red | The filter is typed wrong. Copy it from Step 3. |
| The editor says the file changed on disk | Choose **Reload**. |

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
| 135, 139, 445 | Windows file and printer sharing |
| 143, 993 | IMAP, reading email (993 encrypted) |
| 443 | HTTPS, secure web pages |
| 995 | POP3, encrypted |
| 1433 | Microsoft SQL Server, a database |
| 3306 | MySQL, a database |
| 3389 | RDP, remote desktop |
| 5900 | VNC, remote desktop |
| 8080, 8443 | Web servers on other ports |
