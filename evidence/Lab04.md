# Lab 04: Lying to the Switch

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon.

## Part 1: Your VM

### Step 2: Your MAC address now

<!-- output: step2 -->

**1. Your interface's MAC address and IP address before the change.**

Answer:

### Step 4: What changed

<!-- output: step4 -->

**2. Your MAC address and IP address after the change.**

Answer:

**3. Did your IP address change too? The network hands out IP addresses by MAC address. Use that to explain what you see.**

Answer:

### Step 5: The gateway answers

<!-- output: step5 -->

**4. Which MAC address asked for the gateway, and which MAC address did the gateway's reply go to?**

Answer:

**5. What did the gateway check about your new MAC address before it replied?**

Answer:

### Step 6: Changed back

<!-- output: step6 -->

**6. Does your MAC address match Step 2 again?**

Answer:

**7. The roaster controller's switch port only accepts the controller's MAC address. Using what you did today, explain how a stranger's laptop could get through that port.**

Answer:

## Part 2: The break room wall port

Fill in the last two columns. Use the attacks and settings in Part 2 of the lab README.

| Attack | What the stranger gets | Switch setting that stops it |
|:--|:--|:--|
| MAC flooding | | |
| MAC spoofing | | |
| Rogue access point | | |

**A. The break room jack is set by port security to accept one MAC address, the staff tablet's. Which of the three attacks does that setting stop?**

Answer:

**B. Which attack still works against that setting, and when?**

Answer:

**C. The conference room has a jack too, and nothing has been plugged into it for a year. What should Kestrel do with it, and why?**

Answer:
