# for row in range(1,10):
#     str=" "
#     for space in range(1,(10-row)):
#         str+=" "
#     for col in range(1,(row+1)):
#         str+="* "
#     prin  t(str)

for row in range(1,5):
    str=""
    for col in range(1,6):
        str+="   "
        if (row==4) or (row+col==4) or (col-row==2):
            str+="*"
    print(str)
