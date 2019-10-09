br = '\''

with open('code.js') as f:
    code = f.read()

#code = '\'\'blabla'
# print (code)
# print(code.find(br))
# SLoc = code.find(br) + 1
# ELoc = code[SLoc + 1:].find(br) + SLoc + 1
# print(code[ELoc + 1:])
pass
Strings = []

while True:
    if code.find(br) == -1:
        break
    SLoc = code.find(br) + 1
    ELoc = code[SLoc:].find(br) + SLoc + 1
    s = code[SLoc:ELoc]
    Strings.append(s)
    code = code[ELoc + 1:]

print(Strings)