import json
import random_read

try:
    with open("users.json",encoding="utf-8")as f:
        data=json.load(f)
        print(data)

        all_users=[user["id"]for user in data]

        my_followings=[user["followers"]for user in data if user["username"]=="akhil"][0]

        my_id=[user["id"]for user in data if user["username"]=="akhil" ].pop()

        to_follow=set(all_users)-set(my_followings)
        to_follow.remove(my_id)
        print(to_follow)
        suggestions=random_read.sample(to_follow,2)
        print(suggestions)


except Exception as e:
    print(e.__class__)

# convert list into set
lst=[1,2,3,4,5,6]
st={*lst}
print(st)

# convert set into list
st={1,2,3,4,5,6}
lst=[*st]
print(lst)