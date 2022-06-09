lst=[10,11,12,12,12,12,13,14,15,16,17]

evenlist=[]
for num in lst:
    if num%2==0:
        evenlist.append(num)
print(evenlist)
evenlist.sort(reverse=True)
print(evenlist)

print(lst.count(14))
#
# lst1=[10,11,12,13,14,15]
# lst2=[11,14,15,16,17]
# dup_lst=list()
#
# for num in lst1:
#     if num in lst2:
#         dup_lst.append(num)
#
#
# print(dup_lst)

