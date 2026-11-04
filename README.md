# AP Cybersecurity: VM Labs

Sierra Canyon School · AP Cybersecurity

Starting in Unit 3, the hands-on work in this course happens on a Linux virtual machine: a whole computer running in a window on your own computer. This repository holds the setup instructions and every lab that uses that machine.

## Labs

| # | Lab | What you do |
|:--|:----|:------------|
| 00 | [VM setup](labs/00-vm-setup/README.md) | Install a virtualization tool and Ubuntu, then prove the machine runs |
| 01 | [Find your own addresses](labs/01-find-your-own-addresses/README.md) | Your VM's IP address, MAC address, gateway, and subnet, and ARP caught in the act |
| 02 | [Ports and the log](labs/02-ports-and-the-log/README.md) | What your VM listens on, ICMP, DNS, and TCP on the wire, then one night of Kestrel's router log |

New labs are added here as the course reaches them.

## How each lab works

You work in your own copy of this repository, made for you by Classroom 50 when you accept the lab assignment. Lab 01, Step 1 signs your VM in to GitHub and clones it.

Each lab has its own folder under `labs/` with a `README.md` that tells you what to do. Each lab also has an evidence file, `evidence/Lab<nn>.md`, holding every question you answer. You run each command through `scripts/record.py`, which shows the output and writes it into the evidence file under that step's marker. Then you type your answers in the file, push it on the lab's own branch, and open a pull request. Read the whole README before you start.

## Lab rules

These apply to every lab in this repository, every time.

- **Analyze only the files you are given.** Every lab file is made up for this course.
- **Never scan, probe, or test a network or device you do not own,** including the school network and your home router. The VM is yours; nothing outside it is.
- **Curiosity is not authorization.** "I just wanted to see if it worked" is not permission.

If a lab ever seems to ask you to point a tool at something outside your own VM, stop and ask first.
