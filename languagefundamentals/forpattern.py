
# pattern=1234
# #                                  #1234
# for i in range ( 1,4):             #1234
#     # for i in range(1,5):         #1234
#     print(pattern)                 #1234

#
# for row in range (1,5):
#     for col in range (1,row+1):
#         print(row,end="\t")
#     print()

# for row in range (1,5):
#     for col in range (1,row+1):
#         print(col,end=" ")
#     print()


# for row in range(1,5):
#     for col in range (5,row,-1):
#         print("#", end="\t")
#     print()


for row in range(1,5):
    for col in range (1,row,-1):
        print(col,end="\t")
    print()
