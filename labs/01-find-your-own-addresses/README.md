# Lab 01: Find Your Own Addresses

**Meeting:** 29 · Addresses
**Graded:** as part of the Meeting 29 classwork.
**Turn in:** the Lab 01 record sheet, by hand, at the end of the period. Nothing is uploaded.

Every command in this lab runs in your VM. Write each answer on your record sheet as you go.

## Step 1: Get the tools and this repository

Open **Terminal** in the VM.

```bash
sudo apt update && sudo apt install -y git tcpdump
mkdir -p ~/version_control && cd ~/version_control
git clone https://github.com/Sierra-Canyon/apcyber-vm-labs.git
```

*If it says* `destination path 'apcyber-vm-labs' already exists`, run this instead:

```bash
cd ~/version_control/apcyber-vm-labs && git pull
```

## Step 2: Your IP address

```bash
ip -br addr
```

Each line is one network interface: its name, its state, and its addresses. `lo` is the VM talking to itself. Ignore it. The other line is your VM's network card.

*You should see* lines in this shape. This sample is from a different machine, so your names and numbers differ.

```
lo               UNKNOWN        127.0.0.1/8
eth0             UP             192.0.2.2/24
```

**Sheet, line 1:** the interface name. **Line 2:** the IP address that has four numbers separated by dots, and the number after the slash. If the line also shows a long address with colons, that is an IPv6 address. Leave it off.

## Step 3: Check which network you are on

On a Mac with UTM, the address usually begins `192.168.64.`. With VirtualBox, it is usually `10.0.2.15`.

**If your address begins with anything else, stop and ask before you go on.** It means your VM is joined straight to the school network, and you capture only on networks you own.

## Step 4: Your MAC address

```bash
ip -br link
```

On your interface's line, the MAC address is six pairs of characters separated by colons, such as `02:fc:00:00:00:01`.

**Sheet, line 3:** your MAC address.

## Step 5: Your default gateway

```bash
ip route
```

The line that starts `default via` names your default gateway.

*You should see* (different machine):

```
default via 192.0.2.1 dev eth0
192.0.2.0/24 dev eth0 proto kernel scope link src 192.0.2.2
```

**Sheet, line 4:** your gateway's IP address. **Line 5:** your subnet. It is the second line of the output, the one that ends in `/24`.

## Step 6: Your ARP table

```bash
ip neigh
```

Each line is an IP address your VM has already matched to a MAC address.

**Sheet, line 6:** the gateway's line, if it is there. If it is not, write "not listed."

## Step 7: Watch ARP happen

Open a second tab with **Ctrl+Shift+T**. In the second tab, start a capture, using your interface name from Step 2:

```bash
sudo tcpdump -n -e -i eth0 arp
```

Go back to the first tab. Empty the ARP table, then ping the gateway, using your own interface name and gateway:

```bash
sudo ip neigh flush dev eth0
ping -c 3 192.0.2.1
```

Go back to the second tab. *You should see* two lines like these (different machine):

```
05:56:18.349290 02:fc:00:00:00:01 > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 42: Request who-has 192.0.2.1 tell 192.0.2.2, length 28
05:56:18.349382 02:fc:00:00:00:05 > 02:fc:00:00:00:01, ethertype ARP (0x0806), length 42: Reply 192.0.2.1 is-at 02:fc:00:00:00:05, length 28
```

Each line starts with the time. The first MAC address after it on a line is who sent it, and the second is who it was sent to. Press **Ctrl+C** to stop the capture.

**Sheet, lines 7 to 9:** who the request was sent to, what it asked, and what the reply said.

## Step 8: Check the table again

```bash
ip neigh
```

**Sheet, line 10:** the gateway's line now. **Line 11:** what your VM checked about the reply before it wrote it in the table.

## Step 9: Kestrel's addresses

Part 2 of the record sheet is on paper. No VM.

## If it broke

| You see | Fix |
|:--|:--|
| `tcpdump: eth0: You don't have permission to perform this capture on that device` | Put `sudo` in front of the command. |
| `Failed to send flush request: Operation not permitted` | Put `sudo` in front of the command. |
| `tcpdump: enp0s9: No such device exists` | The interface name is wrong. Copy it from `ip -br addr`. |
| No ARP lines in the capture after the ping | The table filled again before the ping. Leave the capture running, then flush and ping again. |
| `git: command not found` | Step 1 did not finish. Run it again and read the last line it prints. |
