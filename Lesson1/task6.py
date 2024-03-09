s = "change me"
ss=''
for i in range(0,len(s)):
    if s[i]=="e":
        ss=ss+"E"
    else:
        ss=ss+s[i]
print(ss)
