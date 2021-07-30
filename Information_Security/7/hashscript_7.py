import sys
import hashlib
import os

if len(sys.argv) < 2:
    print("no input is provided as commandline argument!!!")
    exit()


input = sys.argv[1]

salt = os.urandom(16)

ittr = 200000

hashpbkdf2 = hashlib.pbkdf2_hmac('sha512', input.encode('utf-8'), salt, ittr)

hashpbkdf2_hex = hashpbkdf2.hex()

print(hashpbkdf2_hex)