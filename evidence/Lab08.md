# Lab 08: A Firewall on Your VM

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon. The rules for Step 2 are in the lab README.

## Part 1 (Meeting 40): Rules from the top

### Step 2: Twelve packets

| Packet | Protocol | From | To | Port | Rule that decides | Allow or Block |
|:--|:--|:--|:--|:--|:--|:--|
| a | TCP | 203.0.113.77 | 203.0.113.10 | 443 | | |
| b | TCP | 198.51.100.40 | 203.0.113.10 | 22 | | |
| c | TCP | 192.168.10.20 | 203.0.113.10 | 3306 | | |
| d | TCP | 203.0.113.77 | 203.0.113.10 | 3306 | | |
| e | TCP | 198.51.100.140 | 203.0.113.40 | 3389 | | |
| f | TCP | 192.168.10.47 | 203.0.113.10 | 80 | | |
| g | TCP | 203.0.113.77 | 203.0.113.10 | 23 | | |
| h | UDP | 198.51.100.9 | 203.0.113.53 | 53 | | |
| i | UDP | 203.0.113.77 | 203.0.113.10 | 53 | | |
| j | ICMP | 192.168.10.47 | 203.0.113.10 | any | | |
| k | ICMP | 198.51.100.9 | 203.0.113.10 | any | | |
| l | TCP | 203.0.113.77 | 203.0.113.10 | 8443 | | |

**1. Packet b is the owner, Luis Ortega, signing in from home. What happened to him, and why? Which rule never gets to do its job?**

Answer:

**2. Fix it: which two rules would you swap?**

Answer:

### Step 3: Your VM's firewall before

<!-- output: step3 -->

**3. What did `curl` on your Mac show in Step 5, before the firewall was on?**

Answer:

### Step 6: The firewall on

<!-- output: step6 -->

**4. What did `curl` on your Mac do after Step 6? Which line of the status explains it?**

Answer:

### Step 7: What the firewall wrote down

<!-- output: step7 -->

**5. Copy the `SRC` and `DPT` from one line. Whose packet was it?**

Answer:

### Step 8: One door open

<!-- output: step8 -->

**6. What did `curl` on your Mac do after Step 8, and why?**

Answer:

## Part 2 (Meeting 41): Rule order

### Step 10: Block at the top

<!-- output: step10 -->

### Step 11: Block at the bottom

<!-- output: step11 -->

**7. The same Block rule was in both lists. What did `curl` do in Step 10, and in Step 11? Explain the difference.**

Answer:

### Step 12: The web store's rules

| Rule | Action | Protocol | From | To | Port |
|--:|:--|:--|:--|:--|:--|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**8. Which requirement does your last rule meet, and why does it have to be last?**

Answer:

**9. Swap your Block rule with your HTTPS rule. What breaks?**

Answer:

**10. Your rule 3 lets the owner in over SSH from one address. A stranger copies that address onto their packets. What else would you want, besides this rule?**

Answer:

## Part 3 (Meeting 42): What leaves

### Step 13: Out, before

<!-- output: step13 -->

### Step 14: Web traffic blocked leaving

<!-- output: step14 -->

### Step 15: The rule Kestrel needed

<!-- output: step15 -->

### Step 16: Put back

<!-- output: step16 -->

**11. What changed between Step 13 and Step 14, and which rule caused it?**

Answer:

**12. Write the rule from Step 15 in the same columns as the Step 2 table. Which way does it face: ingress or egress?**

Answer:

**13. Would the Step 15 rule have stopped the bookkeeper's laptop in Lab 02 from calling out? Which firewall at Kestrel should hold it: the perimeter firewall at the edge, or an internal firewall between segments? Why?**

Answer:
