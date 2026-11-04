# Lab 02: Ports and the Log

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon. The port card is at the bottom of the lab README.

## Part 1: Your VM

### Step 2: What is listening

<!-- output: step2 -->

**1. How many lines start with `tcp`, and how many with `udp`.**

Answer:

**2. Copy one line whose port is `53`.**

Answer:

**3. The address on that line.**

Answer:

### Step 3: ICMP

<!-- output: step3 -->

**4. The words after `ICMP` on the line going out, and on the line coming back.**

Answer:

### Step 4: DNS

<!-- output: step4 -->

**5. Copy one question line (it has `A?` in it).**

Answer:

**6. The port the question went to.**

Answer:

**7. Which protocol carried it. The capture filter you typed tells you.**

Answer:

### Step 5: TCP

<!-- output: step5 -->

**8. The `Flags` on each of the three lines, in order.**

Answer:

**9. How much data the three packets carried. Look at `length`.**

Answer:

## Part 2: Kestrel's log

### Step 6: Count it

<!-- output: step6 -->

**10. Lines in the file, BLOCK lines, and ACCEPT lines.**

Answer:

### Step 7: What was knocked on

<!-- output: step7 -->

**11. The port blocked most often.**

Answer:

**12. The program on that port.**

Answer:

### Step 8: Who knocked

<!-- output: step8 -->

**13. Each address that was blocked, and its count.**

Answer:

### Step 9: What got in from outside

<!-- output: step9 -->

**14. The time, the address, and the port.**

Answer:

**15. The program on that port.**

Answer:

### Step 10: The bookkeeper's laptop

<!-- output: step10 -->

**16. How many times the laptop connected to `198.51.100.23`.**

Answer:

**17. The first and last times.**

Answer:

**18. How far apart the connections are.**

Answer:

**19. Which kill chain stage this looks like, and why.**

Answer:
