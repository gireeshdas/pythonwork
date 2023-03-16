# home work
lst = [1,2,3,4,5,6,7,8]
sum = 10
res = []
for i in range(0, len(lst) - 2):
    for j in range(i + 1, len(lst) - 1):
        for k in range(j + 1, len(lst)):
            if lst[i] + lst[j] + lst[k] == sum:
                temp = []
                temp.append(lst[i])
                temp.append(lst[j])
                temp.append(lst[k])
                res.append(tuple(temp))
print("The pairs is : " + str(res))