import hashlib
import random

def generate_ntlm_hash(password):
    #生成 md5 hash
    unicode_password = password.encode('utf-16le')
    ntlm_hash = hashlib.md5()
    ntlm_hash.update(unicode_password)
    return ntlm_hash.digest()

# 生成5組6位密碼
passwords = [f"{random.randint(100000, 999999)}" for _ in range(5)]
hashes = [generate_ntlm_hash(password) for password in passwords]
# 輸出結果
for i,j in enumerate(hashes):
    print(f"Password: {passwords[i]}")
    print(f"NTLM hash: {j.hex()}")
    print(f"------------------------------------")

