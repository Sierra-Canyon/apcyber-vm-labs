# Lab 05: Lying About the Gateway

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon. The device table is at the top of the lab README.

## Part 1: The ARP messages

### Step 2: Every ARP message

<!-- output: step2 -->

**1. The real gateway's MAC address. Which line proves it?**

Answer:

**2. Copy the first line where the laptop at .66 says it is 192.168.10.1. Who did it send that reply to?**

Answer:

**3. What else does the laptop tell the router, and why does it need to tell both sides?**

Answer:

**4. How often does it repeat the lie, and why does it keep repeating it?**

Answer:

**5. What did Wireshark say about the first reply the duplicate filter found?**

Answer:

## Part 2: What went through the laptop

### Step 4: Who carried the web traffic

<!-- output: step4 -->

**6. Before 01:54:03, which MAC address did jrivera's workstation send its packets to?**

Answer:

**7. At 01:54:09, follow the GET request: which MAC address did it go to first, and where did that device send it next?**

Answer:

### Step 5: What the laptop could read

<!-- output: step5 -->

**8. Why does each line show up twice?**

Answer:

**9. Name two things the laptop at .66 read. Compare the cookie with Lab 03's: what does that tell you?**

Answer:

**10. The laptop only read the page this time. Which leg of the CIA triad would it break if it changed the page before passing it on?**

Answer:

## Part 3: Kestrel

The same thing happens on Kestrel's roastery LAN: a device plugged into the break room jack poisons the bookkeeper's laptop.

**A. Where does the bookkeeper's next packet to the online store go first?**

Answer:

**B. The online store uses HTTPS. What can the attacker still learn from the traffic it relays? Use Lab 03.**

Answer:

**C. Name one control from this unit that would have stopped the device from getting on the LAN in the first place.**

Answer:
