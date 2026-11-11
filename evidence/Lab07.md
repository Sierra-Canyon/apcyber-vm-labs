# Lab 07: Encrypt a File With AES

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon.

## Part 1: AES on one file

### Step 2: The file in plain text

<!-- output: step2 -->

### Step 3: Locked

<!-- output: step3 -->

**1. Can you read any of the prices in the locked file? What do the first eight bytes say?**

Answer:

**2. The plain file and the locked file are different sizes. Which is bigger, by how much?**

Answer:

### Step 4: The right password

<!-- output: step4 -->

**3. What came back?**

Answer:

### Step 5: The wrong password

<!-- output: step5 -->

**4. One letter was different. What did openssl say?**

Answer:

### Step 6: Locked again

<!-- output: step6 -->

**5. Same file, same password. Are the two locked files the same?**

Answer:

**6. Why not? Use what `-salt` does.**

Answer:

**7. Someone captures Kestrel's staff Wi-Fi traffic, protected by WPA3 with AES. Compare what they see with what you read in Lab 03's HTTP sign-in.**

Answer:

## Part 2: Kestrel's wireless and VPN policy

For each row, write your choice and one sentence of reason.

| Rule | Choices | Your choice | Reason |
|:--|:--|:--|:--|
| Staff Wi-Fi security | WPA3 with AES, or WPA2, or open | | |
| How staff sign in | Each person's own account through EAP, or one shared password | | |
| Guest Wi-Fi | On the staff network, or its own network with its own password | | |
| WPS | On or off | | |
| MAC filtering on the staff Wi-Fi | The only control, or one extra layer, or not used | | |
| Dana at home | VPN to Kestrel, or straight over her home internet | | |
| Split tunneling for Dana | On or off | | |

**A. Why does MAC filtering alone fail to keep a stranger off the staff Wi-Fi? Use Lab 04.**

Answer:

**B. Dana's VPN is on and split tunneling is on. She opens a fake sign-in page from an email. Does the VPN protect her? Why or why not?**

Answer:
