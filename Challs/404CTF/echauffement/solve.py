import binascii

string = "685f6683a487f0d1b6c1bcc55cddbebd56c954c9d4a950cfd0a5ce4bc8bd44bdaad9000000000000"

value = binascii.unhexlify(string)

print(value)
test = ""

for i in range (0, len(value)):
    print(value[i], end=' ')
    #print the code ascii of the value and put it in test variable
    test1 =  (value[i] + i)//2
    print(test1, end=' ')
    test += chr(test1)


print(test)