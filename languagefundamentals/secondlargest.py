num1=5
num2=6
num3=7
if(num1>num2) and (num1>num3):
    if(num2>num3):
        print(f"{num2} is second largest")
    else:
        print(f"{num3} is second largest")




elif(num2>=num1) & (num2>=num3):
    print(f"{num2} is second largest")
elif(num3>=num1) & (num3>=num2):
    print(f"{num3} is second largest")

