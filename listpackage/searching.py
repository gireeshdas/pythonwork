lst=[1,2,3,13,15,16,65,78,89]


element=15
# flag=0
# for num in arr:
#     if element==num:
#         flag=1
#         break
# print("element_fount" if flag!=0 else "not_fount")

for i in range(0,len(lst)):
    if element==lst[i]:
        flag=1
        break
print("element_fount" if flag!=0 else "not_fount")








