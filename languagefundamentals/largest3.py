# num1=10
# num2=4
# num3=3
#
# if(num1>num2) & (num1>num3):
#     print(f"{num1} is largest")
# elif(num2>num1) & (num2>num3):
#     print(f"{num2} is largest")
# elif(num3>num1) & (num3>num2):
#     print(f"{num3} is largest")
# elif(num1==num2) & (num1==num3):
#     print("same")
#

# Python program to find the largest number among the three input numbers

num1 = 10
num2 = 14
num3 = 12
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)