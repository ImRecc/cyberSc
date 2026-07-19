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
`in php
/var/www/html/index.php if it's mainpage's loc
include "includes/secret.inc",is a Relative Path. file must be physically located at /var/www/html/includes/secret.inc.
` 
but point is:\
.bak、.swp、.inc \
those temp file, not .php, often unconsiously saved in server, could be read, not like .php, apache server refuse to give raw data, \
apache will run and give return value.

#### l8.ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc
meaningless, most php have a 
`$allowed_pages = ['home', 'about', 'contact', 'services'];` to avoid pathTraversal attack

#### l9.UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9

#### l10.EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv
php's passthu(), similar to exec(),\
use ; to divide commands\

#### l11.VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd
filter like preg_match(), not worth to spend tomuch\
grep, \
`grep PATTERN FILE` is the key\
`grep . /etc/natas_webpass/natas11`\
. means "any character" \

#### l12.EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng
1. xor's key's length are fixed, it can't be fit for all input to met input ^ key = encrypted.\
but key = encrypted ^ input, and get a repeated key, to know the length or "real key"\
but The repeating key is: kBSwkBSwkBSwkBSwkBSwkBSwkBZ{GvF"R) this is what i got when cal the key.\

2. we want cal the cookies to input, by input = b64Encode(xor（jsonEncode(desiredText), key))\
and for the key's length didnt match exactly we want\
( i think we could reduce bgcolor's length by 1 to get same answer， to not guess key's length to avoid second php script)

3. b64 and php's main usage is some text are not humanReadable but computer storable or dealable? so store as data, then use b64 to handle
more to see natas11-12's php script
4. XOR have switch, A^B = B^A, based
