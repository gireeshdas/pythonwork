# expenses=[10,20,30,40,50]
# # for amount in expenses:
# #     print(amount)
#
# for i in range(0,len(expenses)):
#     print(expenses[i])

# numbers=[12,13,14,15,16,17,18]

# for num in numbers:
#     if num%2==0:
#         print(num)
#
# for num in numbers:
#     if (num>15):
#         print(num+1)
#     elif(num<15):
#         print(num-1)
#     elif(num==15):
#         print(num)

# numbers=[14,18]
# count=0
#
# for num in numbers:
#     if num>=14 and num<=18:
#         count+=1
#
# print(count)

numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
# p_count=0
# n_count=0
# z_count=0
#
# for num in numbers:
#     if num>0:
#         p_count+=1
#
#     elif(num<0):
#         n_count+=1
#     elif(num==0):
#         z_count+=1
# print(f"+ve count{p_count},-ve count {n_count},zero count{z_count}")
sum=0
for num in numbers:
    sum+=num
print(sum)

