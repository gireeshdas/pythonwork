# def lcm(a, b):
#     if a > b:
#         greater = a
#     else:
#         greater = b
#     while(True):
#         if((greater % a == 0) and (greater % b == 0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
#
#
# if __name__ == '__main__':
#     print("LCM = ", lcm(4, 6))


# Python Program to find the L.C.M. of two input number

def findlcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The LCM is", findlcm(num1, num2))