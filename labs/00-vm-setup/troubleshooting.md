# Lab 00: Troubleshooting

## The VM will not start, or the installer never appears

- **Apple Silicon Mac:** check the ISO name. It must end in `arm64`. If it ends in `amd64`, download the ARM build and choose it again under the VM's CD/DVD drive.
- **Windows PC:** virtualization may be turned off in your computer's BIOS or UEFI settings. Search for your laptop model plus "enable virtualization". If you have never been in a BIOS before, ask for help instead of guessing.
- **Windows PC:** Hyper-V or WSL can conflict with VirtualBox. If VirtualBox reports an error about Hyper-V, ask for help.

## The install finished, but the VM shows a black screen

Shut the VM down, remove the installer from the virtual CD drive, and start it again.

- UTM: select the VM, find the CD/DVD drive, and choose **Clear**.
- VirtualBox: **Settings**, **Storage**, select the disk under the controller, and remove it.

## The VM is very slow

- Close other apps while the VM runs, especially browsers with many tabs.
- Check the VM's memory. 4 GB is the minimum that works well.
- On an 8 GB computer, do not give the VM more than 4 GB.

## Not enough disk space

The VM needs about 25 GB free, plus room for the 4 GB ISO while you install. You can delete the ISO once Ubuntu is installed.

## The download is slow or keeps failing

The ISO is large. Use a wired or strong connection, and do not start the download the night before.

## Something else

Write down the exact error message, take a screenshot of it, and ask. A screenshot of the error is the fastest way to a fix.
