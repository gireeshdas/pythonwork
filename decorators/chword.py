master_word="abbeccddeffggf"

#
# def possible_word(master_word):
#     x={ }
#     for n in master_word:
#         x[n]=x.get(n,0)+1
#     return x
# def master_word_set(w,master_word):
#     for char in w:
#         value=1
#         m=possible_word(char)
#         for k in m:
#             if k not in master_word:
#                 value=0
#             else:
#                 if master_word.count(k)!=m[k]:
#                     value=0
#     if value==1:
#         print(char)

words=master_word.split(" ")

ch_word={}

for w in master_word:
    if w in ch_word:
        ch_word[w]+=1
    else:
        ch_word[w]=1
print(ch_word)