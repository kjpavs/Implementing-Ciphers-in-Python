import random
import string

key = ''
emsg = ''
msg = input("enter the message:")
for i in range(len(msg)):
    if msg[i].isalpha():
        key += chr(random.randrange(26) + 65)
    else:
        key += random.choice(string.punctuation)
msg = msg.upper()
for j in range(len(msg)):
    if key[j].isalpha():
        emsg += chr(((ord(msg[j]) + ord(key[j])) % 26) + 65)
    else:
        emsg += chr((ord(msg[j]) + ord(key[j])) % 256)
print(emsg)
dmsg = ''
for n in range(len(key)):
    if key[n].isalpha():
        dmsg += chr(((ord(emsg[n]) - ord(key[n]) + 26) % 26) + 65)
    else:
        dmsg += chr((ord(emsg[n]) - ord(key[n]) + 256) % 256)
print(dmsg)
