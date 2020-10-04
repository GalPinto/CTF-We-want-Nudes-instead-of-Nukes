x1 = "FIRE_NUKES_MELA!"
iv = b'\x39\x1e\x95\xa1\x58\x47\xcf\xd9\x5e\xce\xe8\xf7\xfe\x7e\xfd\x66'
c = b'\x84\x73\xdc\xb8\x6b\xc1\x2c\x6b\x60\x87\x61\x9c\x00\xb6\x65\x7e'
# c = Ek(iv xor x1)    ci = Ek(c(i-1) xor xi)
y1 = "SEND_NUDES_MELA!"
iv2 = []
# c will be the same if   iv xor x1 = iv2 xor y1
#                         iv2 = (iv xor x1) xor y1
#                         flag{iv2,c}

for i in range(len(iv)):
    #print("",ord(x1[i]),end="")
    #iv1.append(iv[i])
    iv2.append(iv[i]^ord(x1[i])^ord(y1[i]))
print("iv2:",iv2) # convert to hexlified string
# iv2: 2c1289a05847cfd65ecee8f7fe7efd66
# flag{2c1289a05847cfd65ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}