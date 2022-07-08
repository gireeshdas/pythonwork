import json

with open("blogs.json",encoding="utf-8")as f:
    data=json.load(f)
print(len(data))

# f=open("blogs.json")
# data=json.load(f)
# print(data)

# number of post by userId=1
userid=[post for post in data if post["userId"]==1]
print(len(userid))

# total number of likes for postId 6
num_likes_post=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(num_likes_post)

# number post liked by use2

like_count_user=len([post for post in data if 2 in post["liked_by"]])
print(like_count_user)