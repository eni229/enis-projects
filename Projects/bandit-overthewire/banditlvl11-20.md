#Bandit over the wire

##Level 11

Encoded using letter substitution cipher called ROT13
Moves everything over by 13 places. Used by tr. 
tr 'A-Za-z' 'N-ZA-Mn-za-m'
This covers uppercase and lower case. From normal alphabet to 13 shifted (N-Z etc). then <<< paste the message

password 12: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

##Level 12

The file has been repeatedly compressed. 
So, we know to use file to check the file type. 
They said its useful to create a directory under tmp, so ill do that to create new files.  made directory called eni229. 

Using cp to copy the original file to my directory. Renamed to original. Checked file type said ascii, so i opened it. its a hex dump. So i need to decode that. 
use xxd -r to reverse a hex dump.

Using what i learnt in the pipelining thing, can save the output of a file to a new file using > filename
saved in hexdump.txt - gzip file
gunzip, must be a gz file, so rename to hexdump.gz
hexdump - now a bz2 file, can use bunzip2 to undo, must be named .bz2, gunzip again. 
Tar file. tar combines the files, so tar -xf seperates the files. 
Basically rinse and repeat

Password 13: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

##Level 13

Given the private key. can be used to log in. 
Opening a new ssh link. Use -i and the filepath to the private key. This proves your identity due to knowing the private key. 
must have a private key to match a public key.
used ssh -i /home/... /filename bandit14@etc. 
looking through level 14, to find password. 

Password 14: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

##Level 14

