# Lab 03: What Anyone on Your Network Can Read

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon. The port card is at the bottom of the lab README.

## Lab rules

- Analyze only the files you are given. Every lab file is made up for this course.
- Never scan, probe, or capture on a network or device you do not own, including the school network and your home network. Your VM is yours. Nothing outside it is.
- Run tools only against your own VM, from your own VM.
- Curiosity is not authorization. "I just wanted to see if it worked" is not permission.
- If you find a real weakness somewhere, report it to the owner and tell no one else.

I have read these rules and I will follow them in every lab.

Signed:

## Part 1: The whole conversation

### Step 3: Every packet

<!-- output: step3 -->

**1. How many packets are in the file?**

Answer:

**2. The two server ports, and the program on each. Use the port card.**

Answer:

**3. The flags on the first three packets of each conversation. What are those three packets doing?**

Answer:

## Part 2: The HTTP sign-in

### Step 5: What crossed the network

<!-- output: step5 -->

**4. The username and the password, with `%21` written as it was typed.**

Answer:

**5. The `SESSIONID` in the server's reply. What could someone do with it, even without the password?**

Answer:

**6. Which leg of the CIA triad does reading this traffic break?**

Answer:

## Part 3: The HTTPS sign-in

### Step 7: What HTTPS still shows

<!-- output: step7 -->

**7. What did Follow TCP Stream show for the port 443 conversation?**

Answer:

**8. The site name you can still read, and where in Wireshark you found it.**

Answer:

**9. What does the number on the last line of Step 7 tell you?**

Answer:

**10. Name three things someone capturing this traffic still learns about the HTTPS visit.**

Answer:

## Part 4: Kestrel

Kestrel's roastery router has a policy: a short list of rules for which traffic it lets through.

**A. Which ports on the port card carry a password across the network the way port 80 did today?**

Answer:

**B. In Lab 02, port 23 was the port knocked on most. Why would an attacker want Telnet open?**

Answer:

**C. Write one line for Kestrel's router policy that would have kept jrivera's password off the network.**

Answer:
