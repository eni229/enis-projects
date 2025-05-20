#linux commands

ls lists all the file in directory
ls -a lists all including hidden
ls -l look at permissions of files

cd change directory
cd .. go back to previous directory

cat open file
cat < -file  opens file with a - at the start. 

file * shows all file types in directory
file -- * works for files with special characters at the start. 

find filename can be used to find a file
find -size numc can be used to find a file thats num bytes

grep  can be used to find key words in the file.

sort filename   puts it alphabetical order.
uniq filename   removes duplicates. 
uniq -u  show unique lines
uniq -c  shows number of occurences

piping - you immediately edit the output of the previous command. 
so sort data.txt | uniq  first sorts data, then the output of that is run through the uniq command. 

tr - used for ciphers, can change the letters. e.g. ROT13 was tr 'A-Za-z' 'N-ZA-Mn-za-m'

cp - copy file
mv - rename file