import random
key = ''
msg = input("enter message:")
for i in range(len(msg)):
    key += chr(random.randrange(256))
emsg = ''
for j in range(len(msg)):
    emsg += chr(ord(msg[j]) ^ ord(key[j]))
print(emsg)
dmsg = ''
for n in range(len(emsg)):
    dmsg += chr(ord(emsg[n]) ^ ord(key[n]))
print(dmsg)
