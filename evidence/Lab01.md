# Lab 01: Find Your Own Addresses

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon.

## Part 1: Your VM

### Step 2: Your IP address

<!-- output: step2 -->

**1. The interface name (not `lo`).**

Answer:

**2. The IP address with four numbers and dots, and the number after the slash.**

Answer:

### Step 4: Your MAC address

<!-- output: step4 -->

**3. Your MAC address.**

Answer:

### Step 5: Your default gateway

<!-- output: step5 -->

**4. Your gateway's IP address.**

Answer:

**5. Your subnet: the line that ends in `/24`.**

Answer:

### Step 6: Your ARP table, before

<!-- output: step6 -->

**6. The gateway's line, or "not listed."**

Answer:

### Step 7: ARP caught in the act

<!-- output: step7 -->

**7. Who the request was sent to, and what that address means.**

Answer:

**8. What the request asked.**

Answer:

**9. What the reply said.**

Answer:

### Step 8: Your ARP table, after

<!-- output: step8 -->

**10. The gateway's line now, and where its MAC address came from.**

Answer:

**11. What did your VM check about the reply before it wrote it in the table?**

Answer:

## Part 2: Kestrel's addresses

Kestrel's roastery office is one LAN. Its subnet is **192.168.10.0/24**: every device in the office has an address that starts 192.168.10. The default gateway is the office router, **192.168.10.1**. The bookkeeper's laptop is **192.168.10.47**.

The bookkeeper's laptop sends a packet to each device below. Fill in the last two columns: **Yes** or **No**, and **Switch** or **Gateway**.

| Device | IP address | Same subnet as the laptop? | First stop: switch or gateway? |
|:--|:--|:--|:--|
| Bookkeeping server | 192.168.10.20 | | |
| Office printer | 192.168.10.30 | | |
| Roaster controller | 192.168.10.60 | | |
| Cafe 1 payment terminal | 192.168.20.11 | | |
| Online store | 203.0.113.10 | | |

**A. The laptop broadcasts "Who has 192.168.10.1?" Which of the five devices receive it?**

Answer:

**B. The roaster controller replies "192.168.10.1 is at" its own MAC address. Where does the laptop's next packet to the online store go?**

Answer:

**C. Who checked that reply?**

Answer:

### If you finish early

<!-- output: stepD -->

**D. Which addresses are in your VM's table now, and what put each one there?**

Answer:
