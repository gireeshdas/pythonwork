lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]

]
# print(lst)
# # print all numbers > 16
# # for sub_list in lst:
# #     for num in sub_list:
# #         if num>16:
# #             print(num)
# flatten_list=[]
# for sub_list in lst:
#     for num in sub_list:
#         flatten_list.append(num)
#
# print(max(flatten_list))
# # print(sum(flatten_list))

fltn_list=[num for slist in lst for num in slist]
print(fltn_list)

num_gt_sixt=[ num for num in fltn_list if num>16]
print(num_gt_sixt)

num_odd_numb=[num  for num in fltn_list if num%2!=0]
print(num_odd_numb)

even_number_sum=sum([num for num in fltn_list if num%2==0])
# print(sum(even_number_sum))
print(even_number_sum)

mapping_of_numb=[num+1 if num>25 else num-1 for num in fltn_list]
print(mapping_of_numb)
