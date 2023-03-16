# lst=[2,3,4,6]
# lst.sort()
# element=8
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==element:
#             print("pairs",lst[i],lst[j])
#
#             break
# # count=1
# low=0
# upp=len(lst)-1
#
# while(low<upp):
#     cur_sum=lst[low]+lst[upp]
#     if element==cur_sum:
#         print(f"pairs {lst[upp]},{lst[low]}")
#         break
#     elif cur_sum<element:
#         upp+=1
#     elif cur_sum>element:
#         low-=1


lst = [1,2,3,4]
sum = 5
res = []
for i in range(0, len(lst) - 1):
    for j in range(i + 1, len(lst) ):
            if lst[i] + lst[j] == sum:
                temp = []
                temp.append(lst[i])
                temp.append(lst[j])
                res.append(tuple(temp))
print("The pairs is : " +str(res))