# num=5
# i=1

# num=int(input("enter the number:"))
# i=1
# fact=1
# while(i<=num):
#     fact=fact*i
#     i+=1
# print("factorial",fact)
#
# # Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))