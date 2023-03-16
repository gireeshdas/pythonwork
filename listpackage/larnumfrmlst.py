# from functools import cmp_to_key
#
# # initializing the list
# numbers = [5,8,4,6,9,2,1,3,7]
#
# def get_key(first, second):
#    if str(first) + str(second) > str(second) + str(first):
#       return -1
#    return 1
#
# # getting the result
# result = sorted(numbers, key=cmp_to_key(get_key))
#
# # joining the result
# result = "".join(str(integer) for integer in result)
#
# # printing the result
# print(int(result))

from functools import reduce
numbers = [5,8,4,6,9,2,1,3,7]
str_lst=[str(n) for n in numbers]
str_lst=sorted(str_lst,reverse=True)
out=reduce(lambda n1,n2:(n1+n2) if (n1+n2)>(n2+n1) else (n2+n1),str_lst)
print(out)
