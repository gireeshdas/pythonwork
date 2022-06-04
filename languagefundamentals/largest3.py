num1=10
num2=460
num3=30

if(num1>num2) & (num1>num3):
    print(f"{num1} is largest")
elif(num2>num1) & (num2>num3):
    print(f"{num2} is largest")
elif(num3>num1) & (num3>num2):
    print(f"{num3} is largest")
elif(num1==num2) & (num1==num3):
    print("same")