def add(*args):
    return sum(args)

#
# def max_fun(*args):
#     return max(args)
#
#
#
# def min_fun(*args):
#     return min(args)
#
# print(add(100,120))
# print(max_fun(200,1200))
# print(min_fun(-2,2))



# def add_nums(**kwargs):
#     sum()
#     print(kwargs)
#
#
# add_nums(n1=10,n2=20,n3=30)

def add_nums(**kwargs):
    print(sum([v for v in kwargs.values()]))

add_nums(n1=10,n2=20,n3=30)

# dict={"n1":10,"n2":20,"n3"=40}
# # def add_nums(**kwargs):
