# Lab 04: Lying to the Switch

**Meeting:** 33 · Lying to the Switch
**Graded:** as part of the Meeting 33 classwork.
**Turn in:** `evidence/Lab04.md` in your lab repository, pushed on the `lab04` branch with a pull request, by the end of the period.

A switch delivers packets by MAC address, and it believes whatever MAC address a device says it has. In Part 1 you change your own VM's MAC address and watch the gateway answer the new one. That is MAC spoofing, done on the one machine you own. In Part 2 you work out what a stranger could do from the empty wall jack in Kestrel's break room, and which switch setting stops each thing.

The commands below use `enp0s1` and `192.168.64.1`, the interface and gateway on a Mac with UTM. If Lab 01 showed you different ones, type yours.

## Step 1: Start a branch

First, on GitHub, merge the pull request **Add Lab 04** in your lab repository. Then, in the VM, with your own GitHub username in place of `<your-username>`:

```bash
cd ~/version_control/apcyber-2026-2027-vm-labs-<your-username>
git switch main
git pull
git switch -c lab04
```

*You should see* `Switched to a new branch 'lab04'`. Every command below runs from this folder.

## Part 1: Your VM

### Step 2: Your MAC address now

```bash
python3 scripts/record.py 04 step2 "ip -br link; ip -br addr"
```

On your interface's line, the MAC address is the six pairs of characters with colons, such as `e6:7d:9f:44:ec:82`. **Copy it onto paper or into a note now.** You need it in Step 6 to change it back.

### Step 3: Change it

Your new MAC address is `02:00:00:00:04:04`. A first pair of `02` marks an address someone set by hand instead of one built into a network card.

```bash
sudo ip link set dev enp0s1 down
sudo ip link set dev enp0s1 address 02:00:00:00:04:04
sudo ip link set dev enp0s1 up
```

The network drops for a few seconds while the interface is down. Wait about ten seconds, then check:

```bash
ip -br addr
```

Run `ip -br addr` again until your interface's line shows an address that begins `192.168.64.`. If it still has none after a minute, run `sudo nmcli device connect enp0s1`.

### Step 4: What changed

```bash
python3 scripts/record.py 04 step4 "ip -br link; ip -br addr"
```

Compare it with Step 2: the MAC address, and the IP address.

### Step 5: Watch the gateway answer the new address

Open a second tab with **Ctrl+Shift+T**. In the second tab:

```bash
python3 scripts/record.py 04 step5 sudo tcpdump -n -e -l -c 2 -i enp0s1 arp and host 192.168.64.1
```

It asks for your password, then waits. In the first tab, empty the ARP table and ping the gateway, as in Lab 01:

```bash
sudo ip neigh flush dev enp0s1
ping -c 3 192.168.64.1
```

Go back to the second tab. *You should see* a `Request` and a `Reply` in this shape. The first MAC address on each line is who sent it, and the second is who it went to. The address after `tell` is your VM's, from Step 4:

```
09:12:40.118204 02:00:00:00:04:04 > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 42: Request who-has 192.168.64.1 tell 192.168.64.2, length 28
09:12:40.118422 7e:f3:4d:ae:88:64 > 02:00:00:00:04:04, ethertype ARP (0x0806), length 42: Reply 192.168.64.1 is-at 7e:f3:4d:ae:88:64, length 28
```

If the two lines are not one `Request` and one `Reply`, run the capture again, then the flush and the ping again.

### Step 6: Change it back

In the first tab, with the MAC address you copied in Step 2 in place of `<your-original-mac>`:

```bash
sudo ip link set dev enp0s1 down
sudo ip link set dev enp0s1 address <your-original-mac>
sudo ip link set dev enp0s1 up
```

Wait until `ip -br addr` shows a `192.168.64.` address again, then record it:

```bash
python3 scripts/record.py 04 step6 "ip -br link; ip -br addr"
```

The MAC address should match Step 2. If you lost the original, restart the VM: a MAC address set with `ip link` does not survive a restart.

## Part 2: The break room wall port

Kestrel's roastery has a wall jack in the break room. It is a data port on the office switch, the same switch as the bookkeeper's laptop, the bookkeeping server, and the roaster controller. The staff tablet usually plugs in there, but nobody checks who else does. Customers on roastery tours walk past it.

A stranger with a laptop and ten minutes could try three things from that jack:

| Attack | What the stranger does |
|:--|:--|
| MAC flooding | Sends the switch thousands of made-up MAC addresses until its table is full |
| MAC spoofing | Copies the roaster controller's MAC address while the controller is switched off for cleaning |
| Rogue access point | Plugs a small Wi-Fi box into the jack and leaves it behind the coffee machine |

Two switch settings answer them:

- **Port security** on a data port limits how many MAC addresses may use it, and which ones. A port set to one known MAC address shuts itself off when a different device appears.
- **Disabling unused data ports** turns a jack off at the switch, so whatever is plugged into it reaches nothing.

The questions are at the end of your evidence file.

## Step 7: Answer the questions

```bash
gnome-text-editor evidence/Lab04.md &
```

Every output is already in the file. Type each answer after `Answer:`, questions 1 to 7, then the table and questions A to C in Part 2. Save with **Ctrl+S**.

## Step 8: Turn it in

Save the file first, then:

```bash
git add evidence/Lab04.md
git commit -m "Lab 04: evidence"
git push -u origin lab04
gh pr create --fill --base main --reviewer jd12
```

*You should see* a link to your pull request. Do not merge it.

## If it broke

| You see | Fix |
|:--|:--|
| No `192.168.64.` address a minute after Step 3 or Step 6 | Run `sudo nmcli device connect enp0s1`, wait ten seconds, and check `ip -br addr` again. |
| `RTNETLINK answers: Device or resource busy` | The interface was still up. Run the `down` line, then the `address` line again. |
| `Cannot find device "enp0s1"` | The interface name is different. Copy it from Step 2. |
| `git push` fails with `Could not resolve host` | The network is still coming back. Wait for a `192.168.64.` address, then push again. |
| The capture is still waiting after the ping | The table filled before the ping. Leave the capture running, then flush and ping again. |
| You lost your original MAC address | Restart the VM. The built-in address comes back by itself. |
