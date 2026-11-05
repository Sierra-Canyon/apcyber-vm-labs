# Lab 01: Find Your Own Addresses

**Meeting:** 29 · Addresses
**Graded:** as part of the Meeting 29 classwork.
**Turn in:** `evidence/Lab01.md` in your lab repository, pushed on the `lab01` branch with a pull request, by the end of the period.

Every command in this lab runs in your VM. Each step that prints something you need is run through `scripts/record.py`, which shows the output on the screen and also writes it into your evidence file. You answer the questions in that file at the end.

## Step 1: Get the tools, sign in, and get your repository

Do this once. Later labs start at Step 2.

**1a. Tools.** Open **Terminal** in the VM.

```bash
sudo apt update && sudo apt install -y git tcpdump gh
```

This can take a few minutes. Leave it running.

**1b. Sign the VM in to GitHub.** Use your real name and your school email.

```bash
git config --global user.name "Your Real Name"
git config --global user.email "you@sierracanyon.org"
gh auth login
```

Answer its questions with the arrow keys and Enter:

| It asks | Choose |
|:--|:--|
| Where do you use GitHub? | GitHub.com |
| Preferred protocol for Git operations? | HTTPS |
| Authenticate Git with your GitHub credentials? | Yes |
| How would you like to authenticate GitHub CLI? | Login with a web browser |

It prints a code like `A1B2-C3D4`. On your **Mac**, open [github.com/login/device](https://github.com/login/device), type the code, and approve. Ignore the browser that tries to open inside the VM.

*You should see* `✓ Logged in as` and your username.

**1c. Accept your lab repository.** Every lab from today to May lives in one repository. Accept it once, on your Mac:

**[VM Labs](https://classroom50.org/Sierra-Canyon/apcyber-2026-2027/assignments/vm-labs/accept)**

Then, in the VM, with your own GitHub username in place of `<your-username>`:

```bash
mkdir -p ~/version_control && cd ~/version_control
git clone https://github.com/Sierra-Canyon/apcyber-2026-2027-vm-labs-<your-username>.git
cd apcyber-2026-2027-vm-labs-<your-username>
git switch -c lab01
```

`git clone` signs in with the account from Step 1b, so it asks for no password. *You should see* `Switched to a new branch 'lab01'`. Every command below runs from this folder.

## Step 2: Your IP address

```bash
python3 scripts/record.py 01 step2 ip -br addr
```

Each line is one network interface: its name, its state, and its addresses. `lo` is the VM talking to itself. Ignore it. The other line is your VM's network card. On a Mac with UTM, its name is usually `enp0s1`.

*You should see* lines in this shape. This sample is from one Mac with UTM, so your numbers may differ.

```
lo               UNKNOWN        127.0.0.1/8 ::1/128
enp0s1           UP             192.168.64.2/24 fe80::e47d:9fff:fe44:ec82/64
```

Questions 1 and 2 in your evidence file are about this output. If the line also shows a long address with colons, that is an IPv6 address. Leave it off.

## Step 3: Check which network you are on

On a Mac with UTM, the address usually begins `192.168.64.`. With VirtualBox, it is usually `10.0.2.15`.

**If your address begins with anything else, stop and ask before you go on.** It means your VM is joined straight to the school network, and you capture only on networks you own.

## Step 4: Your MAC address

```bash
python3 scripts/record.py 01 step4 ip -br link
```

On your interface's line, the MAC address is six pairs of characters separated by colons, such as `e6:7d:9f:44:ec:82`.

## Step 5: Your default gateway

```bash
python3 scripts/record.py 01 step5 ip route
```

The line that starts `default via` names your default gateway.

*You should see* (one Mac with UTM):

```
default via 192.168.64.1 dev enp0s1 proto dhcp src 192.168.64.2 metric 100
192.168.64.0/24 dev enp0s1 proto kernel scope link src 192.168.64.2 metric 100
```

Your subnet is the second line, the one that ends in `/24`.

## Step 6: Your ARP table

```bash
python3 scripts/record.py 01 step6 ip neigh
```

Each line is an IP address your VM has already matched to a MAC address. A line that starts `fe80::` is the IPv6 version of a neighbor. Leave it off your answers.

## Step 7: Watch ARP happen

Open a second tab with **Ctrl+Shift+T**. It opens in the same folder. In the second tab, start a capture. The commands below use `enp0s1` and `192.168.64.1`, the usual interface and gateway on a Mac with UTM. If Steps 2 and 5 showed you different ones, type yours:

```bash
python3 scripts/record.py 01 step7 sudo tcpdump -n -e -l -c 2 -i enp0s1 arp
```

It asks for your password, then waits. `-c 2` makes it stop by itself after two packets.

Go back to the first tab. Empty the ARP table, then ping the gateway, using your own interface name and gateway:

```bash
sudo ip neigh flush dev enp0s1
ping -c 3 192.168.64.1
```

Go back to the second tab. *You should see* two lines like these (one Mac with UTM), then `Recorded under step7`:

```
10:41:38.983076 e6:7d:9f:44:ec:82 > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 42: Request who-has 192.168.64.1 tell 192.168.64.2, length 28
10:41:38.984638 7e:f3:4d:ae:88:64 > e6:7d:9f:44:ec:82, ethertype ARP (0x0806), length 42: Reply 192.168.64.1 is-at 7e:f3:4d:ae:88:64, length 28
```

Each line starts with the time. The first MAC address after it is who sent it, and the second is who it was sent to. If your two lines are not one `Request` and one `Reply`, run the capture again, then the flush and the ping again. The new output replaces the old.

## Step 8: Check the table again

```bash
python3 scripts/record.py 01 step8 ip neigh
```

## Step 9: Answer the questions

```bash
gnome-text-editor evidence/Lab01.md &
```

Every output is already in the file. Type each answer after `Answer:`, for questions 1 to 11 in Part 1, then the table and questions A to C in Part 2. Part 2 is about Kestrel and needs no commands. Save with **Ctrl+S**.

If you finish early, run this, then answer question D:

```bash
python3 scripts/record.py 01 stepD ip neigh
```

## Step 10: Turn it in

Save the file first, then:

```bash
git add evidence/Lab01.md
git commit -m "Lab 01: evidence"
git push -u origin lab01
gh pr create --fill --base main --reviewer jd12
```

*You should see* a link to your pull request. Do not merge it.

## If it broke

| You see | Fix |
|:--|:--|
| `tcpdump: enp0s1: You don't have permission to perform this capture on that device` | Put `sudo` in front of `tcpdump`. |
| `Failed to send flush request: Operation not permitted` | Put `sudo` in front of the command. |
| `tcpdump: enp0s9: No such device exists` | The interface name is wrong. Copy it from `ip -br addr`. |
| The capture is still waiting after the ping | The table filled again before the ping. Leave the capture running, then flush and ping again. |
| `remote: Repository not found.` | Accept the assignment on your Mac first, and check the username in the repository name. |
| `git clone` asks for a username and password | Step 1b did not finish. Run `gh auth login` again and answer **Yes** to authenticating Git. |
| `There is no <!-- output: step7 --> line` | The step name is typed wrong. Copy the command from this README. |
| `Cannot find .../evidence/Lab01.md` | Run the command from inside your lab repository folder. |
| `gh: command not found` | Step 1a did not finish. Run it again and read the last line it prints. |
| The editor says the file changed on disk | Choose **Reload**, then type your answers again. Record every step before you start typing. |
