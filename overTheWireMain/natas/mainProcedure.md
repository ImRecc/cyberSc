#### l1. 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq
basic f12 trick
`curl.exe -u natas0:natas0 http://natas0.natas.labs.overthewire.org` to avoid powershell's trap\

#### l2. TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI 
意味不明な\

#### l3. 3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
文件路径还真是一个值得看看的地方，比如图在/files/img.img\
那就可以看看/files，类似bandit

#### l4. natas4:JDrPnuZAKyl6MkiqQGFIddrqpvgOASth
robots.txt, when good bot like googleCrawler read this, it just ignores that\
this is not a firewall, edge/chrome browser dont read that\
The folder /s3cr3t/ was "hidden" from you simply because there were no buttons or links pointing to it on the main page.\
browser are simple directly tool, only view where links put to\
to get directories, gobuster is the way\


#### l5. natas5:e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M
the oldest way of verification: header's referrer;
`curl.exe -u natas4:[PASSWORD] -H "Referer: http://natas5.natas.labs.overthewire.org/" http://natas4.natas.labs.overthewire.org/`
to change referrer\
curl not like browser's "edit and resend", don't care any rule so modify header are viable

#### l6. natas6:7mhjtShJAcld2NYbKHEadnhEwRn2P8VT
HTTP are stateless protocol\
visit a website for the first time, the server gives your browser a tiny text file (a Cookie) that says something like user_role=guest.\
cookies maybe the key. 
`devTool->application->cookie`
`curl.exe -u natas5:[PASSWORD] -b "cookie_name=cookie_value" http://natas5.natas.labs.overthewire.org/`
or a cookie editor can do the trick
`curl.exe -u natas5:[PASSWORD] -b "cookie_name=cookie_value" http://natas5.natas.labs.overthewire.org/`


#### l7.B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0
<?...?> are for php\
server side language\
Developers often put sensitive configuration files (like .inc or .env or .bak) on the web server, \
forgetting that anyone can just type the URL and download them\
include "includes/secret.inc", this is the way\
