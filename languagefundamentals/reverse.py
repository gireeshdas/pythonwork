# num=123
# while(num!=0):
#     last_digit=num % 10
#     print(last_digit,end="")
#     num = num // 10


num=123
res=""

while (num!=0):
    last_digit= num % 10
    res=res+str(last_digit)
    num=num//10
print(res)


