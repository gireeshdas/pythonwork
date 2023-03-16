master_word="aabbccddeggcattt"
check_word="egg"

flag=0
my_dict={}
for char in master_word:
    if char in my_dict:
        my_dict[char]+=1
    else:
        my_dict[char]=1

for char in check_word:
    if char in my_dict:
        char_count=my_dict.get(char)
        if char_count>0:
            my_dict[char]-=1
        elif my_dict[char]==0:
            flag=1
            break
    else:
        flag = 1
        break
if (flag==0):
    print(True)
else:
    print(False)




