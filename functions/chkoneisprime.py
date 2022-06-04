def is_prime(num):
    flag=0
    for i in range (2,num):
        if(num%i==0):
            flag=1
            break
    return flag==0

def prime_range(low,upp):
    for num in range(low,(upp+1)):
        if is_prime(num):
            prin boolt(num)
prime_range(12,21)
