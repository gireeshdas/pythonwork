lst=[1,2,3,4,5,6,7,8,9,0]
element=12
flag=0

for i in range (len(lst)):
    if element==lst[i]:
        flag=1
        break

print("number is found" if flag!=0 else "not found")


element=2

flag=0
for i in range (len(lst)):
    if element==lst[i]:
        flag=1
        break
print("number is found" if flag!=0 else "not found")










