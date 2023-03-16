pattern="ABACCDA"

char_count={}
rec_char=[]
for char in pattern:
    if char in char_count:
        rec_char.append(char)

    else:
        char_count[char]=1
print(rec_char[1],"second recursive ")
print(rec_char[0],"first recursive")
#
word_count={"a":2,"b":5,"c":2,"d":4,"e":2}
wc_list=word_count.items()
print(sorted(wc_list,key=lambda item:item[1],reverse=True))
#
# max and min==============
print(max(wc_list,key=lambda item:item[1]))
print(min(wc_list,key=lambda item:item[1]))
print(min(word_count.items(),key=lambda i:i[1]))
print(wc_list)