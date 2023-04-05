1. The technique used for this problem is called "crib dragging", the idea is extremely straightforward. I implemented ```generalsearch.py``` to examine the possible plaintext snippets containing some specific string. To start with, I gave "sigpwny{" as the possible string in one of the messages. Fortunately, although the script has a pretty long output, the most important output lays at the very end. 

```
cipher string #10
get at position 0
('Crib dra', 0)
('What you', 1)
('Asymmetr', 2)
('Cryptogr', 3)
('Cryptana', 4)
('Modern c', 5)
('There ar', 6)
('These me', 7)
('Encrypti', 8)
('The grow', 9)
('sigpwny{', 10)
```

2. After this, I modified ```generalsearch.py``` to examine each message with longer strings. If you run the python scripts in this folder with names like ```sixth.py```, you will get outputs like below. The scripts contain the process of me finding out more and more characters in the messages. Eventually, the flag was found. 

```
cipher string #10
get at position 0
('Crib dra', 0)
('What you', 1)
('Asymmetr', 2)
('Cryptogr', 3)
('Cryptana', 4)
('Modern c', 5)
('There ar', 6)
('These me', 7)
('Encrypti', 8)
('The grow', 9)
('sigpwny{', 10)
```

```
cipher string #6
get at position 0
('Crib dragg', 0)
('What you n', 1)
('Asymmetric', 2)
('Cryptograp', 3)
('Cryptanaly', 4)
('Modern cry', 5)
('There are ', 6)
('These mess', 7)
('Encryption', 8)
('The growth', 9)
('sigpwny{th', 10)
```

```
cipher string #7
get at position 0
('Crib dragging', 0)
('What you need', 1)
('Asymmetric sy', 2)
('Cryptography ', 3)
('Cryptanalysis', 4)
('Modern crypto', 5)
('There are two', 6)
('These message', 7)
('Encryption is', 8)
('The growth  o', 9)
('sigpwny{they_', 10)
```

```
cipher string #5
get at position 0
('Crib dragging is ', 0)
('What you need for', 1)
('Asymmetric syst e', 2)
('Cryptography prio', 3)
('Cryptanalysis is ', 4)
('Modern cryptograp', 5)
('There are two typ', 6)
('These messages ho', 7)
('Encryption is the', 8)
('The growth  of cr', 9)
```

```
cipher string #1
get at position 0
('Crib dragging is a', 0)
('What you need for ', 1)
('Asymmetric syst em', 2)
('Cryptography prior', 3)
('Cryptanalysis is t', 4)
('Modern cryptograp ', 5)
('There are two type', 6)
('These messages hon', 7)
('Encryption is the ', 8)
('The growth  of cry', 9)
('sigpwny{they_reboo', 10)
```
```
cipher string #9
get at position 0
('Crib dragging is a kn', 0)
('What you need for a p', 1)
('Asymmetric syst ems u', 2)
('Cryptography prior to', 3)
('Cryptanalysis is the ', 4)
('Modern cryptograp hy ', 5)
('There are two types o', 6)
('These messages honest', 7)
('Encryption is the pro', 8)
('The growth  of crypto', 9)
('sigpwny{they_rebooted', 10)
```

```
cipher string #0
get at position 0
('Crib dragging is a known', 0)
('What you need for a publ', 1)
('Asymmetric syst ems use ', 2)
('Cryptography prior to th', 3)
('Cryptanalysis is the ter', 4)
('Modern cryptograp hy is ', 5)
('There are two types of c', 6)
('These messages honestly ', 7)
('Encryption is the proces', 8)
('The growth  of cryptogra', 9)
('sigpwny{they_rebooted_mt', 10)
```

```
cipher string #9
get at position 0
('Crib dragging is a known p', 0)
('What you need for a public', 1)
('Asymmetric syst ems use a ', 2)
('Cryptography prior to the ', 3)
('Cryptanalysis is the term ', 4)
('Modern cryptograp hy is he', 5)
('There are two types of cry', 6)
('These messages honestly ge', 7)
('Encryption is the process ', 8)
('The growth  of cryptograph', 9)
('sigpwny{they_rebooted_mtv_', 10)
```

```
cipher string #6
get at position 0
('Crib dragging is a known plain text', 0)
('What you need for a public key cryp', 1)
("Asymmetric syst ems use a 'public k", 2)
('Cryptography prior to the modern ag', 3)
('Cryptanalysis is the term used for ', 4)
('Modern cryptograp hy is heavily bas', 5)
('There are two types of cryptography', 6)
('These messages honestly get really ', 7)
('Encryption is the process of conver', 8)
('The growth  of cryptographic techno', 9)
('sigpwny{they_rebooted_mtv_cribs_in_', 10)
```

```
cipher string #1
get at position 0
('Crib dragging is a known plain text atta', 0)
('What you need for a public key cryptogra', 1)
("Asymmetric syst ems use a 'public key' t", 2)
('Cryptography prior to the modern age was', 3)
('Cryptanalysis is the term used for the s', 4)
('Modern cryptograp hy is heavily based on', 5)
('There are two types of cryptography - th', 6)
('These messages honestly get really annoy', 7)
('Encryption is the process of converting ', 8)
('The growth  of cryptographic technology ', 9)
// Here locates the real flag, please find out that by yourself, ;)
```

3. In fact, I stuck at this problem for a long time, with ```generalsearch.py``` giving no valuable information. In the end, I realized that ```ord(' ')``` was out of range of ```[ord('!'), ord('~')]```, so my original script failed to catch messages with space in it. :(
