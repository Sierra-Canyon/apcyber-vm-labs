# Lab 09: Reading a Server's Logs

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon.

## Part 1: The authentication log

### Step 2: The last 30 lines

<!-- output: step2 -->

**1. When did the owner, `lortega`, sign in and out, and from which address?**

Answer:

### Step 3: The failed sign-ins

<!-- output: step3 -->

**2. How many failed sign-ins, from which address, in about how many minutes?**

Answer:

**3. Which accounts did it try most? Why those?**

Answer:

### Step 4: The sign-ins that worked

<!-- output: step4 -->

**4. Which account signed in with a password, from which address, at what time?**

Answer:

**5. What did that account do in the next three minutes? Why is each command a problem?**

Answer:

## Part 2: The network log

### Step 5: The same addresses

<!-- output: step5 -->

### Step 6: The rules

<!-- output: step6 -->

**6. Which rule let 198.51.100.77 and 198.51.100.140 reach SSH? What did whoever wrote that rule probably mean to do?**

Answer:

**7. Rewrite that rule so it does what the owner needed.**

Answer:

### Step 7: What was blocked

<!-- output: step7 -->

**8. Pick the blocked connection to port 3306. Copy its line, and name the rule that blocked it and why.**

Answer:

**9. 203.0.113.77 was blocked on port 22, but 198.51.100.77 was allowed on port 22. Explain the difference using the rules.**

Answer:

### Step 8: What left after 02:47

<!-- output: step8 -->

**10. Where have you seen 198.51.100.23 before? What is the store server doing, how often, and since when?**

Answer:

**11. Which rule allowed it to leave? Write an egress rule that would stop it, and say where in the list it goes.**

Answer:

**12. Put the night in order as a story in four sentences: the knocking, the guessing, the way in, and what happened after. Name the kill chain stage for each.**

Answer:
