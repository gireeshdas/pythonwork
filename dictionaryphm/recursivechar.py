# pattern="ABAACCDA"
#
#
#
# # char_count={}
# # for char in pattern:
# #     if char in char_count:
# #         print(f"first_recursive is {char}")
# #         break
# #     else:
# #         char_count[char]=1
#
#
# # second recursive char
# char_count={}
# rec_char=[]
# for char in pattern:
#     if char in char_count:
#         rec_char.append(char)
#     else:
#         char_count[char]=1
# # print(rec_char[1],"sec rec char")
# print(rec_char)


word_count={"a":2,"b":5,"c":2,"d":4,"e":2}
wc_list=word_count.items()
# print(sorted(wc_list,key=lambda item:item[1],reverse=True))
#
# # max and min==============
# print(max(wc_list,key=lambda item:item[1]))
# print(min(wc_list,key=lambda item:item[1]))
print(min(word_count.items(),key=lambda i:i[1]))