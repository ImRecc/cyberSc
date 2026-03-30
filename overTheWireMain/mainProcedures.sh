L0-L1. connect then cat, connect via ssh bandit0@bandit.labs.xxx.xxx -p xxxx
l1-l2. to open file that names like "-", try cat ./- to make system understand we are not trying to add arg
l2-l3. the space, usually recognized as seperate, but a simple tab key will make system know how to autofill. like cat ./--spaces\ in\ this\ filename-- 
l3-l4. same, tab is the way
L4-L5. file -f <list> to examine files that listed on <list>
file -cfile -c (compile magic)： 我们说过，file 靠“魔数”认文件。
如果你自己发明了一种全新的文件格式（比如 .kagamine 后缀），你想让系统认识它，你得自己写一条魔数规则。
写完之后，用 file -c 你的规则文件 来测试你的代码写得对不对。它输出的 cont offset type... 就是规则表格的表头

file ./* work, in linux, man page, file [options] [...], those in brackets[], are optional, by default
L5-l6. find itself are Recursive, so find -size 1033c should do it

L6-l7 find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
没错，find能直接-user -group来filtering， 2>/dev/null， 把stderr这个通道2的信息拉到null中
比直接find -size 33c | grep bandit7 然后眼睛看来的快， grep没有过滤这种功能。
l7-l8. dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

grep could be use as filter,
-A n (After)： 显示匹配行及之后的 $n$ 行。-B n (Before)： 显示匹配行及之前的 $n$ 行。-C n (Context)： 显示匹配行前后各 $n$ 行。
cat data.txt | grep -B 1 "millionth"

l8-l9. 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
uniq ONLY compare Adjacent lines, sort first. sort -o\sort > t1.txt, no permissions.
sort data.txt | uniq -u

l9-l10. ========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
try xxd -b data.txt | grep -A n -E "={3,}"
xxd's output are very limited by 16 bytes per line, 
xxd + grep -A needs calculations of the strength of password for we dunno how many line xxd cut after "serveral '='".

strings data.txt,
strings could use to filtering all non-humanreadable chars

L10-L11. dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
base64 trick

L11-L12. 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
rot13, 
tr 'A-Za-z' 'N-ZA-Mn-za-m'
tr itself doesnot have any parser, simply Track1, track2
乱码+==在结尾，几乎可以确认是base64的前面，base64是把3个字节变成4个字符，如果原始数据的长度不是 3 的倍数，编码器就会在末尾补上 1 个或 2 个 =。

l12-l13. FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
