#!/hackThisSite/realisticMission

R1. simple injection attack

R2. gobuster or some other scanner\fuzzer...
    requires me to gain admin access, so must be an login.php or somthing similar...
    we got a login page, and tried SQL injection, commentalized "request password"
    

R3. yes, goBuster, but nothing interesting found 403 code haha..
    however, there is some self-claimed genius script kiddo leave some comment and could use as clue
    we found the vulnerable part that poem are store as file and only rewrite mode activated
    Bizzard part is why /../index.html instead of /index.html
    only gods know how this playground's file structures built
