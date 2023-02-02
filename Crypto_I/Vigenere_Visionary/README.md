---
Added Time: Feb 2 2023
Difficulty: easy
Score: 100
Link: https://ctf.sigpwny.com/challenges#Meetings/Vigen%C3%A8re%20Visionary-125
---
I guess some people eventually realized that Caesar cipher really wasn't that secure. You'll have to give them some slack - at the time, it was rare for people to even know how to read. Vigenere cipher is an upgrade, with the same alphabet shifting principle, but instead of a single character key or number, it now consists of a keyword, and cycles through this keyword to shift.

I have provided with you the keyword and the encryption function. Create the decryption function and crack the ciphertext. Once you have the plaintext, the flag is sigpwny{[plaintext goes here]}

Note: consider this an introduction to repeated key encryption, where the key is extended to match the plaintext/ciphertext length.
