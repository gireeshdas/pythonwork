from functools import reduce
# mapping

#filtering
# reduce

lst=[1,2,3,3]

squares=list(map(lambda n:n**2,lst))
cubs=list(map(lambda n:n**3,lst))

print(squares)
print(cubs)

# map <5 num-1 >5 num+1
# num_out =[num-1 if num<5 else num+1 for num in lst]
# print(num_out)

num_out=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(num_out)

# map
# filter
# reduce
lst=[10,2,30,4,5,6,7]
gt_ten=list(filter(lambda n:n>5,lst))
print(gt_ten)

# reduce

sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)