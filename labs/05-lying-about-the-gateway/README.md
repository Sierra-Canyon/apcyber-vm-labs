# Lab 05: Lying About the Gateway

**Meeting:** 34 · ARP Poisoning
**Graded:** as part of the Meeting 34 classwork.
**Turn in:** `evidence/Lab05.md` in your lab repository, pushed on the `lab05` branch with a pull request, by the end of the period.

In Lab 01 your VM asked the whole LAN who had the gateway, and believed the first answer. This capture, `02_arp_spoof.pcap`, was recorded on the network at Riverside Clinic a few minutes after Lab 03's. It is made up for this course. Three devices are in it:

| Device | IP address | MAC address |
|:--|:--|:--|
| jrivera's workstation | 192.168.10.47 | 02:1a:2b:3c:4d:5e |
| The clinic's router, the default gateway | 192.168.10.1 | 02:aa:bb:cc:dd:01 |
| A laptop someone plugged in | 192.168.10.66 | 02:66:66:66:66:66 |

Nothing in it is live, and you capture nothing today. You read it with `tcpdump` through `scripts/record.py`, and look at it in Wireshark.

## Step 1: Start a branch

First, on GitHub, merge the pull request **Add Lab 05** in your lab repository. Then, in the VM, with your own GitHub username in place of `<your-username>`:

```bash
cd ~/version_control/apcyber-2026-2027-vm-labs-<your-username>
git switch main
git pull
git switch -c lab05
cd labs/05-lying-about-the-gateway
```

*You should see* `Switched to a new branch 'lab05'`. Every command below runs from this folder, so the script is `../../scripts/record.py`.

## Part 1: The ARP messages

### Step 2: Every ARP message, with MAC addresses

```bash
python3 ../../scripts/record.py 05 step2 tcpdump -nn -e -r 02_arp_spoof.pcap arp
```

`-e` shows the MAC addresses: the first one on each line sent it, and the second one received it. Match each MAC address to a device with the table above.

Read it top to bottom. The first two lines are jrivera's workstation asking for the gateway and the real router answering, the same as your VM in Lab 01. Then the laptop at .66 does the same. Then, from `01:54:03`, it starts answering questions nobody asked.

### Step 3: Wireshark notices

```bash
wireshark 02_arp_spoof.pcap &
```

Type `arp.duplicate-address-detected` in the filter bar and press **Enter**. Wireshark marks every reply that gives an IP address a different MAC address from the one it saw earlier. Click the first one, then open **Address Resolution Protocol** in the bottom left pane: click the ▸ arrow at its left. Then clear the filter.

## Part 2: What went through the laptop

### Step 4: Who carried the web traffic

```bash
python3 ../../scripts/record.py 05 step4 tcpdump -nn -e -r 02_arp_spoof.pcap port 80
```

These are jrivera's packets to the clinic portal on port 80. Look at the MAC addresses on each line, before `01:54:03` and after.

### Step 5: What the laptop could read

In Wireshark, type `http` in the filter bar and press **Enter**. Right-click the `GET /patients/summary` packet, then **Follow** > **TCP Stream**.

Close that window and record the lines that matter:

```bash
python3 ../../scripts/record.py 05 step5 "tcpdump -nn -A -r 02_arp_spoof.pcap port 80 | grep -a -E 'GET|Cookie|Patient'"
```

Each line shows up twice. Step 4 tells you why.

## Step 6: Answer the questions

```bash
gnome-text-editor ../../evidence/Lab05.md &
```

Every output is already in the file. Type each answer after `Answer:`, questions 1 to 10, then A to C in Part 3. Save with **Ctrl+S**.

## Step 7: Turn it in

Save the file first, then:

```bash
cd ../..
git add evidence/Lab05.md
git commit -m "Lab 05: evidence"
git push -u origin lab05
gh pr create --fill --base main --reviewer jd12
```

*You should see* a link to your pull request. Do not merge it.

## If it broke

| You see | Fix |
|:--|:--|
| `tcpdump: 02_arp_spoof.pcap: No such file or directory` | Run the `cd labs/05-lying-about-the-gateway` line from Step 1. If it still fails, merge **Add Lab 05** on GitHub, then `git switch main`, `git pull`, `git switch lab05`, `git merge --no-edit main`. |
| `There is no <!-- output: step2 --> line` | The lab number or step name is typed wrong. Copy the command from this README. |
| The duplicate filter shows nothing | Check the spelling: `arp.duplicate-address-detected`, with two hyphens. |
| Follow is greyed out | Click a packet first, then right-click that packet. |
| The editor says the file changed on disk | Choose **Reload**. |
