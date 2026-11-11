# Lab 06: Knocking on Every Door

Every `<!-- output: ... -->` line is filled in for you by `scripts/record.py`. Do not type in those code blocks. Type each answer on the line that starts `Answer:`, after the colon. The port card is at the bottom of the lab README.

## Part 1: The scan

### Step 2: Every knock and every answer

<!-- output: step2 -->

**1. How many ports did the laptop knock on, and how long did the whole scan take? Use the first and last times before 01:54:01.**

Answer:

**2. A closed port answers with which flags?**

Answer:

**3. An open port answers with which flags, and what does the laptop send right after that?**

Answer:

**4. The laptop never finishes the handshake on an open port during the scan. Why would a scanner stop there?**

Answer:

### Step 3: The doors that opened

<!-- output: step3 -->

**5. The open ports, and the program on each.**

Answer:

**6. Port 22 shows up twice in Step 3. Why?**

Answer:

### Step 4: The banner

<!-- output: step4 -->

**7. The program and version the banner gave away.**

Answer:

**8. Why is that one line useful to an attacker?**

Answer:

**9. Which kill chain stage is a port scan, and what stage could the banner lead to next?**

Answer:

## Part 2: The scanner report

| # | Finding | High, Medium, or Low | Reason |
|:--|:--|:--|:--|
| 1 | Telnet open on port 23 | | |
| 2 | MySQL open to the internet on port 3306 | | |
| 3 | `/admin` accepts admin / admin | | |
| 4 | SSH version with a published weakness that needs an account | | |
| 5 | Customer sign-in on port 80 without HTTPS | | |
| 6 | Web server banner names `nginx/1.18.0` | | |
| 7 | HTTPS certificate expires in 21 days | | |

**A. Which finding would you fix first, and why that one?**

Answer:

**B. Pick one finding you rated Low. What would have to be true for it to become High?**

Answer:
