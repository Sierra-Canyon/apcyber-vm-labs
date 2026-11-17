# Lab 5.5: Lying About Names, and Drowning the Server

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon.

## Part 1: Read the alerts

Riverside Clinic's monitoring system sends an alert when something looks wrong. An alert is a claim. The lines under it are the evidence. For each one, name the attack, copy the line that proves it, and say which leg of the CIA triad it breaks.

### Alert 1, together · 09:14:02 · DNS answer from an unexpected server

```text
09:14:02.110  192.168.10.47 asks: portal.riverside-clinic.example A?
09:14:02.118  answer from 192.168.10.66: portal.riverside-clinic.example A 192.168.10.66
09:14:02.161  answer from 192.168.10.53: portal.riverside-clinic.example A 203.0.113.10 (ignored, arrived second)
```

Riverside's DNS server is 192.168.10.53. The portal is at 203.0.113.10.

**1. The attack.**

Answer:

**2. The evidence line, and what it shows.**

Answer:

**3. The leg of the CIA triad it breaks, and why.**

Answer:

**4. What happens to jrivera the next time she types the portal's name?**

Answer:

### Alert 2 · 10:02:11 · ICMP flood to the store server

```text
10:02:11.000              one ICMP echo request to 198.51.100.255, sender 203.0.113.10
10:02:11.004 to 10:02:11.090  ICMP echo reply to 203.0.113.10 from 58 addresses in 198.51.100.0/24
```

The store server, 203.0.113.10, sent no echo request at 10:02.

**5. The attack.**

Answer:

**6. The evidence line, and what it shows.**

Answer:

**7. The leg of the CIA triad it breaks, and why.**

Answer:

### Alert 3 · 13:30 · Connection flood on port 443

```text
13:30 to 13:31  41,882 new connections to 203.0.113.10 port 443
                from 12,406 different addresses in 61 countries
```

Normal for that minute on a Tuesday: about 300 connections.

**8. The attack.**

Answer:

**9. The evidence line, and what it shows.**

Answer:

**10. The leg of the CIA triad it breaks, and why.**

Answer:

### Alert 4 · 15:12 · One address, one page, every second

```text
15:12 to 15:13  198.51.100.77 requested /search 9,400 times
15:12 to 15:13  every other address combined: 260 requests
15:13           store server processor at 100%, pages taking 40 seconds
```

**11. The attack.**

Answer:

**12. The evidence line, and what it shows.**

Answer:

**13. The leg of the CIA triad it breaks, and why.**

Answer:

### Alert 5 · 16:45 · Staff visiting a new look-alike site

```text
16:41 to 16:45  14 staff computers opened http://riverside-clinic-login.example/portal
                6 of them sent POST /portal with fields username and password
```

The site was registered two days ago. Its page copies the real portal's logo.

**14. The attack.**

Answer:

**15. The evidence line, and what it shows.**

Answer:

**16. The leg of the CIA triad it breaks, and why.**

Answer:

## Part 2: Poison one name, on your own VM

### Step 3: Where does the name go now?

<!-- output: step3 -->

**17. The address `neverssl.com` leads to.**

Answer:

### Step 4: Add one wrong line

<!-- output: step4 -->

### Step 5: Where does the name go now?

<!-- output: step5 -->

**18. The address it leads to now, and what that address is.**

Answer:

### Step 6: Try to reach it

<!-- output: step6 -->

**19. What did `curl` print? What did the page in Firefox say?**

Answer:

### Step 7: Take the line out, and check

<!-- output: step7 -->

**20. Is the real address back? Compare it with Step 3.**

Answer:

**21. How is your one line like DNS poisoning? What would an attacker put at the wrong address?**

Answer:
