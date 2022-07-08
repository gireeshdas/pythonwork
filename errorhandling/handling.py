# num1=int(input("enter the num1"))
# num2=int(input("enter the num2"))
#
# lst=[]
# try:
#
#     print(num1/num2)
# except Exception as e:
#     num2=int(input("entre the num2"))
#     print(num1/num2)
#
# # try:
# #     a,*b =lst
# # except Exception as e:
# #     print(e)
#
# finally:
#     print("line1")
#     print("line2")


num=input("enter the phnumber")
if len(num)!=10:
    raise Exception("incorrect number")
else:
    print("correct number")