#TryHackMe Challenges

offensive security intro room 
used something called gobuster to hack a bank account, ran it in the terminal. used the command:
gobuster -u http://fakebank.thm -w wordlist.txt dir
the -u is used to state the website we are scanning, and -w takes a list of words to iterate through to find hidden pages. 

defensive security intro room
alert log - bad ip address - 143.110.250.149 port 22


##Pickle rick
- find 3 ingrediants to help rick make his potion and transform back into human from a pickle

looked in the source code of the website and found the user name. 
R1ckRul3s
okay. tried to find another hidden website on the other thing. used the gobuster command. 
so i decided to look around the file tabs, and i found that there are loads of wordlists. so i used one that had wordlists called common.txt
used: gobuster dir -u http://10.10.120.209 -w Tools/wordlists/dirb/common.txt

it came back with 2 that worked, index.html, and robots.txt. these had the code 200. meaning success i think.
robots.txt just says wubbalubbadubdub  nothing in the source code. 
index.html didnt change anything so i assume its just the home page. 
There was also /assets. which had code 301. codes in the 300 mean redirection. codes in 400 means error client side. so assets might be something. 
yes assests has a list of other places that work on thw website. ill test them. Nope, just lead to a bunch of gifs, one was a fail gif. rip. thats so sad. okay. next. 
started running the rockyou.txt. moving really slowly tho, looks like it could take a while. i imagine there is a quicker way to do it?
okay. theres something called -x where you can look for ones that specifically end in a certain thing. i put html,txt,php,js,css. all the ones i could think of. there was an early match of login.php so im going to try that while it continues to run in the background. 

i think it runs slow because im on an attackbox machine thing. 
oh no it froze. i tried to cancel it. may have to reload. 
oh i ran out of free time. to be continued. 

im gonna check the login.php page. Then ill put the username R1ckRul3s and i'm gonna try the password as Wubbalubbadubdub. then ill  brute force it with the list of fasttrack.txt
until next time. gotta wait til tomorrow. 