#### L0-L1. connect then cat, connect via ssh bandit0@bandit.labs.xxx.xxx -p xxxx
#### l1-l2. to open file that names like "-", try cat ./- to make system understand we are not trying to add arg
#### l2-l3. the space, usually recognized as seperate, but a simple tab key will make system know how to autofill. like cat ./--spaces\ in\ this\ filename-- 
#### l3-l4. same, tab is the way
#### L4-L5. file -f <list> to examine files that listed on <list>
```
file -cfile -c (compile magic)： 我们说过，file 靠“魔数”认文件。
如果你自己发明了一种全新的文件格式（比如 .kagamine 后缀），你想让系统认识它，你得自己写一条魔数规则。
写完之后，用 file -c 你的规则文件 来测试你的代码写得对不对。它输出的 cont offset type... 就是规则表格的表头
```
`file ./* work, in linux, man page, file [options] [...], those in brackets[], are optional, by default`
#### L5-l6. find itself are Recursive, so find -size 1033c should do it

#### L6-l7 find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
```没错，find能直接-user -group来filtering， 2>/dev/null， 把stderr这个通道2的信息拉到null中
比直接find -size 33c | grep bandit7 然后眼睛看来的快， grep没有过滤这种功能。
```
#### l7-l8. dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

```grep could be use as filter,
-A n (After)： 显示匹配行及之后的 $n$ 行。-B n (Before)： 显示匹配行及之前的 $n$ 行。-C n (Context)： 显示匹配行前后各 $n$ 行。
cat data.txt | grep -B 1 "millionth"
```
#### l8-l9. 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```uniq ONLY compare Adjacent lines, sort first. sort -o\sort > t1.txt, no permissions.
sort data.txt | uniq -u
```
#### l9-l10. ========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```try xxd -b data.txt | grep -A n -E "={3,}"
xxd's output are very limited by 16 bytes per line, 
xxd + grep -A needs calculations of the strength of password for we dunno how many line xxd cut after "serveral '='".

strings data.txt,
strings could use to filtering all non-humanreadable chars
```
#### L10-L11. dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
`base64 trick`

#### L11-L12. 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```rot13, 
tr 'A-Za-z' 'N-ZA-Mn-za-m'
tr itself doesnot have any parser, simply Track1, track2
乱码+==在结尾，几乎可以确认是base64的前面，base64是把3个字节变成4个字符，如果原始数据的长度不是 3 的倍数，编码器就会在末尾补上 1 个或 2 个 =。
```
#### l12-l13. FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```gzip\bzip2, mathematical way to convert files, change in-place unless using options
tar, tape Archive, bucklet the files, when EXTRACT(not decompress), 
will trying to restore all the metaFile(permissions, belongs) by create
so tar -xf xxx.tar -C /validDir to switch to granted directory
```
#### L13-l14. ssh -i /path/to/keyfile user@host
```ssh -i sshkey.private -o ServerAliveInterval=45 bandit14@localhost -p 2220
yes, there are some way to login\get file, just wait
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```
#### l14-l15 
```nc localhost 30000 < bandit14
cat bandit14 | nc localhost 30000
在/etc/bandit_pass/ 里面
（没错，这个设计是搞人的，故意的）
nc 内部的代码逻辑只有一句话：“把键盘敲给我的东西（标准输入 stdin），发送到网络端口上去；把网络端口返回的东西，打印在屏幕上。”
所以
nc host port < FILE
echo "xxx" > nc host port
干的都是把stdin发给端口，如何返回的打印
什么> 重定向，| 管线，是shell的逻辑，
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```
#### l15-l16
```kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
ncat是最新的，建议用这个，什么nc,netcat都是老东西了，不太行,然后man7.org比较好，比Linux.die.net好
echo "strings" > ncat --ssl localhost 30001
或者有些老东西不支持ncat，但是用了http的就多少会有openssl
openssl s_client用于建立一个安全连接，
openssl s_client -connect host:port
然后再交互
```
#### l16-l17
```ncat -z localhost portRange
-z表示0I/O，连上直接退
所以不能-z --ssl，因为--ssl需要完整的tcp握手
或者nmap -p localhost portRange
然后拿到的几个
for port in Ranges; do echo "密码" | openssl s_client -connect host:$port -quiet; done
加上-quiet可以忽略KEYUPDATE之类的回执或者参数信息

或者nmap其实会比对字典来避免无限被echo的
nmap -sV -p port host
当然0个人需要真的扫那么多端口
$ports=(nmap -p Ranges localhost | grep open | cut -d '/' -f 1 | tr '\n' ',')
:: -d 代表delimiter，分隔符，分出两块， -f代表field， xxxx/tcp open，-f 1 第一块就是xxx
来拿到一行端口，再
for ports in $ports; do nmap -p $port -sV localhost; done
或
nmap -p $ports -sV --version-intensity localhost
或者快一点T0躲避防火墙检测，最慢,T5最快，容易丢包
nmap -T4 -p $ports -sV --version-intensity 1 localhost
因为nmap接受1,2,3,这种形式，并且能忽略掉最后一个逗号
当然nmap很慢，所以
$ports=(nmap -p Ranges localhost | grep open | cut -d '/' -f 1)就行，for循环支持换行，不需要搞个空格tr '\n' ' '
for port in $ports; do echo "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | ncat --ssl localhost $port; done
利用ncat直接ssl链接
EReVavePLFHtFlFsjn3hyzMlvSuSAcRD
```
#### l17-l18:
```diff --suppress-common-lines file1 file2
x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```
#### l18-l19
```ssh user@host "command_to_run"
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
带命令的时候是非交互式的终端，会跳过.bashrc\.profile这些，
只有结果然后关闭链接
ssh -t bandit18@bandit.labs.overthewire.org -p 2220 "/bin/sh"
这个可以强制分配一个shell，不加载.bashrc这些
```
#### l19-l20
```about chmod
[r][w][x], triple binary number
100->4
010->2
001->1
拥有者 (Owner)、同组用户 (Group)、其他人 (Others) 每个文件都有这仨
然后有个s
-rwsr-x---   1 bandit20 bandit19 14888 Apr  3 15:17 bandit20-do
代表suid，用其他用户的名号运行文件
常用手法就是找找suid配置不好的文件然后用了看权限不符合的东西
还有符号模式
u = user (主人)
g = group (同组人)
o = others (其他人)
a = all (所有人)
操作符：
+  增加权限
-  剥夺权限
=  精确设置权限（没写的就代表没有）
chmod -R go=
把除了user外的权限清零
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```
#### l20-l21
```EeoULMCra2q0dSkYj561DX7s1CpBuOBt
port commu are client-client
ncat -l -p to post a listener, 
then ./suconnect to rise dialog
then, both listener or caller can commu

add & to put task in background
use jobs to check like [1]+ Running nc -l -p 11451 &
then fg %1 to put it back
ctrlZ to pause, and bg %1 to put it background
```
#### l21-l22
```crond
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
下面代表每一分钟、每一小时、每一天、每一月、每一周
如果想要0330
那就30 3 * * *
bandit22 代表强制以bandit22的权限运行
cron是会被这种东西攻破的
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```
#### l22-l23
```0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
正常下：md5sum filename
输出 [32bit hash] filename
如果多个文件
md5sum *.txt > check.md5
然后就可
md5sum -c check.md5
看看文件们和提供的哈希值是否一致
- 单破折号代表标准输入
用管道符传入数据时，md5sum为了保证[哈希值] [文件名] 这个死格式不被破坏
在结尾加了个‘ -’表示是从键盘\管道来的数据
有时候echo会自己加一个换行
echo 'xxx'变成echo 'xxx\n'
所以需要echo -n来保持
```
#### l23-l24
```gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
check hx.sh for more
```
#### l24-l25
```see b25hx.md
for more about bash
iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```
#### l25-l26
```
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
1. 
after ssh login, the first prog running are list in
/etc/passwd
#/etc/shadow to save all the password(hashed), check it if you have the permission
in this case, running
#!/bin/bash
export TERMINAL="linux"
# a shell varaible
exec more ~/showtext.txt
# more 的属性就是长的文本会打断，不会像strings或者cat一样一股脑吐出来
# 所以简单的缩小窗口就能直接“暂停”more，来下一步
# more 一般运行在safemode, export MORESECURE=1,所以直接!command不太行
# 但是more有个v
#Start up an editor at current line. The editor is taken from
           the environment variable VISUAL if defined, or EDITOR if
           VISUAL is not defined, or defaults to vi(1) if neither VISUAL
           nor EDITOR is defined.
so luckly, we have vi(VIM),it could run command, like
:r! command to echoning result in the vim inside
or :!command to run on shell
but when it needs a shell, it also ask /etc/passwd
so, do
:set shell=/bin/bash
and yes, /etc/passwd are more like a default settings

```
