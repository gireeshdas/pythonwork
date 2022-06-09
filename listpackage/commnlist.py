lst1=[1,2,3,4,5,6,7,7,8,9]
lst2=[2,4,4,5,6,7,3,1,9]

lst1.sort()
lst2.sort()
# print(lst1)
# print(lst2)

dup_list=[]
for i in range(0,len(lst1)):
    for j in range((i+1),len(lst2)):
        if lst1[i]==lst2[j]:
            dup_list.append(lst1[i])
            # dup_list.append(lst2[i])
print(dup_list)

