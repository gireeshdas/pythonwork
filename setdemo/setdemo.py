# lst=[10,10,1,2,3,4,5,6,16,16,16]
#
# st=set(lst)
# print(st)
#
# print(dir(set))

#
# st1={1,2,3,4,5}
# st2={10,11,12,2,3}
#
# union_set=st1.union(st2)
# print(union_set)
#
# intersection_set=st1.intersection(st2)
# print(intersection_set)
#
# difference_set=st1.difference(st2)
# print(difference_set)


students=["ram","ravi","hari","nikil","jain","jhon","tom"]
passed_students=["ravi","hari","tom"]

# difference_set=students.difference(passed_students)
# print(difference_set)

failed_students=set(students).difference(set(passed_students))
print(failed_students)


lst1=[1,2,3,4,5,6,7,1,2,3,66,77,88]
lst2=[2,3,4,5,6,12,13,14,66,77,88]
difference_lst=set(lst1).difference((set(lst2)))
print(difference_lst)