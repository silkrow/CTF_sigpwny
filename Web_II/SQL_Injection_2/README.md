---
Added Time: Mar 6 2023
Difficulty: medium
Score: 250
Link: https://ctf.sigpwny.com/challenges#Meetings/SQL%20Injection%202-440
---
Nice job on that last assignment. Unfortunately, you were not covert enough and the MSA realized they were hacked. They recently upped their security game and added a filter to detect OR and || in the fields to prevent SQL injection. They haven't seen the last of us, though. Go to http://sql-2.chal.sigpwny.com to begin your attack.

This time you don't know the username for the president. But you do know that the SQL query being executed is $results = $db->query("SELECT * FROM users WHERE username = '$username' AND password = '$password'");
