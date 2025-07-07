#how the web works

##DNS in detail

DNS - domain name system. 

domain hierarchy
TLD (top level domain)
- most right hand part of a domain name. e.g. .com or .co.uk
- two types: gTLD (generic), ccTLD (country code)

second level domain
- the name of the website - e.g. tryhackme

subdomain - extra parts on the left handside if the second level domain. 
so when you have things infront like admin.tryhackme.com (the admin part)
63 max number of characters

limit for whole domain name is 253

DNS record types
-A record - IPv4 addresses
- AAAA record - IPv6 adresses
- CNAME record - i dont know what this means
- MX record - handles emails. 
- TXT record - free text fields. 

DNS requests
1. checks local cache. else recursive DNS server made. 
2. server provided by ISP, cache of recently looked up domain names. 
3. root DNS - directs you to the right tld
4. tld server directs you to the right authoritative server, known as name server. 
5. stores DNS records for particular domain name. 
TTL - time to live value, how long domain name is saved for locally until looking up again. 


##HTTPS in detail

http - hypertext transfer protocol - set of rules used for commincating with web servers
https - secure - encrypted.
url - uniform resource locator
there's explainations on splitting up the url, and what it all means. i get the gist.

making a request  - GET/HTTP/1.1
