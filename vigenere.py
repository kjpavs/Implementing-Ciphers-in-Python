import random
import string

key = input('enter the key:')
emsg = ''
msg = input("enter the message:")
for i in range(0, len(msg) - len(key), len(key)):
    key += key
if len(key) != len(msg):
    if len(key) > len(msg):
        key = key[:len(msg)]
    else:
        key += key[:len(msg) - len(key)]
key = key.upper()
msg = msg.upper()
for j in range(len(msg)):
    if msg[j].isalpha():
        emsg += chr(((ord(msg[j]) + ord(key[j])) % 26) + 65)
    else:
        emsg += chr((ord(msg[j]) + ord(key[j])) % 256)
print(emsg)
dmsg = ''
for n in range(len(key)):
    if emsg[n].isalpha():
        dmsg += chr(((ord(emsg[n]) - ord(key[n]) + 26) % 26) + 65)
    else:
        dmsg += chr((ord(emsg[n]) - ord(key[n]) + 256) % 256)
print(dmsg)
print(key)
