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
psw 4 L6. HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
L7.morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
L6-l7 find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
没错，find能直接-user -group来filtering， 2>/dev/null， 把stderr这个通道2的信息拉到null中
比直接find -size 33c | grep bandit7 然后眼睛看来的快， grep没有过滤这种功能。
l7-l8. dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

我有一个问题，首先是grep似乎不能或者说没有过滤这种功能？之前level6-7那个就这样？只是我比较好奇如果没有find这种工具能用，要如何过滤呢？是不是可以比如x工具，x->echo > 't.txt', 然后在find ./t.txt -group xxx这样子？

然后是level7-8, 额，他给的那些命令提示man, grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd，我要怎么文雅的表示出“没一个能用”呢？或者说，我直接想了想直接cat data.txt | grep millionth，然后欸，我预想会把millionth前后的都拉出来，结果直接拉出了millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc 这个出人意料又有点合理的结果。

只是我在想，有没有更能控制的方法呢？比如这次是运气好正好是millionth后面的，如果下一次是millionth前面的呢？那不就抓瞎了？
