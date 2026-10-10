# Lab 00: VM Setup

**Graded:** completion only. Done or not done.
**Due:** the date on the LMS assignment.
**Turn in:** one full-screen screenshot, uploaded to the LMS.

Starting in Unit 3 you will do hands-on work on a Linux machine running as a virtual machine (VM). This lab gets that machine working. Start early: when this goes wrong, it goes wrong in ways that take more than one evening to fix.

## Step 1: Find out what computer you have

**Mac:** Apple menu, then **About This Mac**.

- "Chip: Apple M1" (or M2, M3, M4, and so on): you have **Apple Silicon**. Follow the Apple Silicon path below.
- "Processor: Intel": you have an **Intel Mac**. Follow the Windows and Intel Mac path below.

While you are there, note your **Memory** (for example 8 GB or 16 GB). You will need it in Step 3.

**Windows PC:** follow the Windows and Intel Mac path below.

**Chromebook, no personal computer, or a school-managed laptop that blocks installs:** say so right away, before you try anything else. A lab machine is available, and it is only easy to arrange if it is known early.

## Step 2: Download two things

### Apple Silicon Mac

1. **UTM**, free, from [mac.getutm.app](https://mac.getutm.app/). The Mac App Store copy is the same app for a fee; you do not need it.
2. **Ubuntu Desktop 24.04.5 LTS for ARM**, from [cdimage.ubuntu.com/releases/noble/release](https://cdimage.ubuntu.com/releases/noble/release/). The file is named `ubuntu-24.04.5-desktop-arm64.iso` (about 3.7 GB).

The file name must end in **arm64**. An `amd64` file will not boot on an Apple Silicon Mac. Downloading the wrong build is the most common mistake on this lab.

Do not use VirtualBox on an Apple Silicon Mac for this course. Use UTM.

### Windows PC or Intel Mac

1. **VirtualBox**, free, from [virtualbox.org](https://www.virtualbox.org/wiki/Downloads). Choose the download for your operating system.
2. **Ubuntu Desktop 24.04.5 LTS**, from [cdimage.ubuntu.com/releases/noble/release](https://cdimage.ubuntu.com/releases/noble/release/). The file is named `ubuntu-24.04.5-desktop-amd64.iso`.

## Step 3: Create the virtual machine

Use these settings. If your computer has 8 GB of memory, use 4 GB for the VM and close other apps while it runs.

| Setting | Value |
|:--------|:------|
| Memory | 4096 MB (4 GB) |
| CPU cores | 2 (4 if your computer has 8 or more) |
| Disk | 25 GB |

### Apple Silicon Mac (UTM)

1. Open UTM and click **Create a New Virtual Machine**.
2. Choose **Virtualize** (not Emulate), then **Linux**.
3. Under **Boot ISO Image**, click **Browse** and choose the `arm64` ISO you downloaded.
4. Enter the memory, CPU, and disk values from the table. Skip the shared directory.
5. Name the VM `apcyber` and click **Save**.

### Windows PC or Intel Mac (VirtualBox)

1. Open VirtualBox and click **New**.
2. Name it `apcyber`, choose the `amd64` ISO you downloaded, and check **Skip Unattended Installation**.
3. Enter the memory, CPU, and disk values from the table, then click **Finish**.

## Step 4: Install Ubuntu

1. Start the VM. Choose **Try or Install Ubuntu**.
2. Follow the installer: language, keyboard, network, then **Install Ubuntu** and **Interactive installation**.
3. When it asks how to install, choose **Erase disk and install Ubuntu**. This erases only the VM's virtual disk. Nothing on your real computer is touched.
4. Create your account. Use your first name as the username and a password you will remember.
5. Wait for the install to finish, then choose **Restart now**.

**If the screen goes black after the restart:** shut the VM down, remove the installer from the virtual CD drive (in UTM: the CD/DVD drive, then **Clear**; in VirtualBox: Settings, Storage, then remove the disk), and start the VM again. This is normal.

## Step 5: Prove it works

When the Ubuntu desktop comes up, open **Terminal** and run these two lines, with your own real name in the first one:

```bash
echo "Firstname Lastname"
uname -a && date
```

Take a screenshot of your **whole screen**, not a crop of the terminal. It must show the Ubuntu desktop running inside a window on your computer, with your name and that output in the terminal.

- Mac: Command + Shift + 3
- Windows: Windows key + Print Screen

Upload the screenshot to the LMS assignment. On an Apple Silicon Mac, the `uname` line should include `aarch64`. On a Windows PC or Intel Mac, it should include `x86_64`.

## Step 6 (optional): Get ready for the next lab

Later labs use `git`. Install it now while you are here:

```bash
sudo apt update && sudo apt install -y git
git --version
```

## Help

Most problems have a known fix. See [troubleshooting.md](troubleshooting.md).

Use whatever help you want on this lab, including a chatbot. It is setup, not assessment. If you are stuck, get stuck early and say so. Every failure here is fixable with time, and none of them is fixable the night before.
