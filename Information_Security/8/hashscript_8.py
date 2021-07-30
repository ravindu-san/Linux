import sys
import hashlib
import os

if len(sys.argv) < 2:
    print("no input is provided as commandline argument!!!")
    exit()


input = sys.argv[1]

salt = os.urandom(16)

hashsha512 = hashlib.sha512()
hashsha512.update(input.encode('utf-8'))
hashsha512.update(salt)

hashsha512_hex = hashsha512.hexdigest()

print(hashsha512_hex)