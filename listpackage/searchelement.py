arr=[11,12,13,14,15]
# flag=0
# element=10
# low=0
# arr.sort()
# upp=len(arr)-1
# while(low<=upp):
#     mid=(low+upp)//2
#     if element==arr[mid]:
#         flag=1
#         break
#     elif element>arr[mid]:
#         low=mid+1
#     elif element<arr[mid]:
#         upp=mid-1
# print("found" if flag>0 else "not found")
element=10

flag=0

for i in range (len(arr)):
    if element==arr[i]:
        flag=1
        break
print("number found" if flag!=0 else "not found")