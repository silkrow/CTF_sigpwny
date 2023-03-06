---
Added Time: Mar 5 2023
Difficulty: beginner
Score: 100
Link: https://ctf.sigpwny.com/challenges#Meetings/SQL%20Injection%201-439
---
We recently learned that the MSA (Midwest Security Agency) has been spying on midwest citizens by hacking their webcams. Your mission is to hack into their database and gather intel about who they have been spying on. Go to http://sql-1.chal.sigpwny.com to begin your attack.

You know that the admin's username is mrprez420. You also know that the SQL query that is being executed is $results = $db->query("SELECT * FROM users WHERE username = '$username' AND password = '$password'");.
