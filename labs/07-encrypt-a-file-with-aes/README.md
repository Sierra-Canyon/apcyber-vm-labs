# Lab 07: Encrypt a File With AES

**Meeting:** 38 · Locking the Wireless
**Graded:** as part of the Meeting 38 classwork.
**Turn in:** `evidence/Lab07.md` in your lab repository, pushed on the `lab07` branch with a pull request, by the end of the period.

WPA3 scrambles everything that crosses Kestrel's staff Wi-Fi with AES. In Part 1 you use AES yourself, on one file in your own VM, with `openssl`: lock it, look at it, unlock it with the right password, and try the wrong one. In Part 2 you write Kestrel's wireless and VPN policy.

## Step 1: Start a branch

First, on GitHub, merge the pull request **Add Lab 07** in your lab repository. Then, in the VM, with your own GitHub username in place of `<your-username>`:

```bash
cd ~/version_control/apcyber-2026-2027-vm-labs-<your-username>
git switch main
git pull
git switch -c lab07
cd labs/07-encrypt-a-file-with-aes
```

*You should see* `Switched to a new branch 'lab07'`. Every command below runs from this folder, so the script is `../../scripts/record.py`.

## Part 1: AES on one file

### Step 2: The file in plain text

Kestrel's wholesale prices are the kind of thing a competitor would want.

```bash
python3 ../../scripts/record.py 07 step2 "echo 'Kestrel wholesale prices: Ethiopia Guji 14.20/lb, Colombia Huila 11.85/lb' > prices.txt; cat prices.txt; ls -l prices.txt"
```

### Step 3: Lock it

```bash
python3 ../../scripts/record.py 07 step3 "openssl enc -aes-256-cbc -pbkdf2 -salt -in prices.txt -out prices.enc -pass pass:Roastery2026; ls -l prices.enc; od -A d -c prices.enc | head -5"
```

`openssl enc -aes-256-cbc` encrypts with AES and a 256-bit key. `-pbkdf2` turns the password into that key. `-salt` mixes in random bytes, so the same password never makes the same key twice. `od -c` shows the file one byte at a time: a printable character where there is one, and a number where there is not.

### Step 4: Unlock it with the right password

```bash
python3 ../../scripts/record.py 07 step4 "openssl enc -d -aes-256-cbc -pbkdf2 -in prices.enc -pass pass:Roastery2026"
```

`-d` means decrypt.

### Step 5: Try the wrong password

One letter is different: a lowercase `r`.

```bash
python3 ../../scripts/record.py 07 step5 "openssl enc -d -aes-256-cbc -pbkdf2 -in prices.enc -out wrong.txt -pass pass:roastery2026"
```

### Step 6: Lock it again

Same file, same password, a second time:

```bash
python3 ../../scripts/record.py 07 step6 "openssl enc -aes-256-cbc -pbkdf2 -salt -in prices.txt -out prices2.enc -pass pass:Roastery2026; cmp prices.enc prices2.enc"
```

`cmp` compares two files and says where they first differ. If they were the same, it would print nothing.

## Part 2: Kestrel's wireless and VPN policy

Luis Ortega, Kestrel's owner, wants one page of rules for the cafes' Wi-Fi and for Dana Whitfield, the operations manager who also runs Kestrel's computers. She works from home on Fridays. The choices are in the evidence file. For each one, pick a choice and give the reason.

Three facts you need:

- WPA3 encrypts every staff device's traffic with AES. WPA2 is older and easier to attack by guessing the password.
- EAP lets each person sign in with their own account, so one person leaving means one account turned off, not a new password for everyone.
- With **split tunneling**, only traffic for Kestrel goes through the VPN, and everything else goes straight out of Dana's home internet. Without it, everything goes through the VPN.

## Step 7: Answer the questions

```bash
gnome-text-editor ../../evidence/Lab07.md &
```

Every output is already in the file. Type each answer after `Answer:`, questions 1 to 7, then the policy table and questions A and B in Part 2. Save with **Ctrl+S**.

## Step 8: Turn it in

Save the file first, then:

```bash
cd ../..
git add evidence/Lab07.md
git commit -m "Lab 07: evidence"
git push -u origin lab07
gh pr create --fill --base main --reviewer jd12
```

Add only the evidence file. `prices.txt` and the `.enc` files stay in your VM.

*You should see* a link to your pull request. Do not merge it.

## If it broke

| You see | Fix |
|:--|:--|
| `Can't open prices.txt for reading` | Run Step 2 first, from the lab folder. |
| `bad magic number` | The file you are decrypting is not an `openssl enc` file. Check the name after `-in`. |
| `python3: can't open file` | From the lab folder the script is `../../scripts/record.py`. |
| `There is no <!-- output: step3 --> line` | The step name is typed wrong. Copy the command from this README. |
| The editor says the file changed on disk | Choose **Reload**. |
