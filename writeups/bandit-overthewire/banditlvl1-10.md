#Bandit over the wire

-- note to self--
to enter the next level, gotta leave the current, and do ssh again. 

ssh bandit0@bandit.labs.overthewire.org -p 2220

##Level 0

Simple level. Just about finding the file and opening the file. 
used ls, cat readme
password 1: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

##Level 1

ls, a folder called -
can't open with -

gotta use cat < - to open
password 2: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

##Level 2

open spaces in filename. 
use cat "spaces in filename"
password 3: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

##Level 3
in a file, use cd to move through files. 
used ls, no file appeared. 

use ls -a to show all files, includes the hidden ones. 
password 4: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

##Level 4

only human readable file in here. 
file shows the type of file. so im looking for one thats readable. 
Tried using file * but all the files have a dash, so it didn't like that. 
Tried file < *, again, didnt like that.
I think i have to go through them one by one. 
< doesn't work, instead using --
file -- -file00
file -- * workssssss

file07 contains an ascii text.
password 5: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

##Level 5

went into inhere file. Theres a lot of files. 
Have 3 clues: 
1. human readable - so ascii text
2. 1033 bytes in size
3. not executable - cant run it like ./
these are all folders, so i probably have to use find?

using du -ab shows size of file in bytes. the a shows everything, including files in all the directories. 
password 6: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

theres proabably a more efficient way to do that level
yeah: find -size 1033c

##Level 6

on the server - so went to home directory
group owned by 6, user owned by 7
using: find / -user bandit7 -group bandit6  
only comes up with permission denied. 
use find / -user bandit7 -group bandit6 2>/dev/null to get rid of errors. 
in folder var/lib.dpkg/bandit7.password  - so random lmao

password 7: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

##Level 7

saved next to the word millionth
used grep "millionth" filename
surprisingly worked. 

password 8: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

##Level 8
the only line of text that is stored once. 

sort puts the file in alphabetical

can look through until you find one thats different, but no efficient. 
Found that password tho, it was not many down. I don't know the proper way to do it. 
if you use pipelining and use uniq and sort. Oh uniq has a -u argument which shows uniq lines. Can also show number of appearances with -c. 

password 9: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

##Level 9

one of the few human readable strings.
Use strings, this shows human readable ones. 

password 10: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

##Level 10

Encoded using base64. 
So just run base64 to decode. okay this gives a string thats way too long. 
Has 2 = at the end, which means its been padded by 2. This means it didn't have enough letters to fill the section at the end. 

To decode, must use base64 -d instead of just base64. base64 encodes. 
pasword 11: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
