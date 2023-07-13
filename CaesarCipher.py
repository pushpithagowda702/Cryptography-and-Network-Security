print("Caesar Cipher")
s = input("Enter the text to be encrypted: ")
key = int(input("Enter key: "))
st = ""
for i in range(0, len(s)):
  pos = ord(s[i]) + key%26
  if(pos > 122 and s[i].islower()):
    pos = pos - 26
  elif(pos > 90 and s[i].isupper()):
    pos = pos - 26
  st += chr(pos)
print(st)

print("Encrypted text: ", st)
        
    
