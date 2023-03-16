text="hai hello hai hello hai hai hai hai hello"

# words=text.split(" ")
#
#
# word_count={}
# for w in words:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)
#
#
words=text.split(" ")
w_count={}
for w in words:
    if w in w_count:
        w_count[w]+=1
    else:
        w_count[w]=1
print(w_count)
