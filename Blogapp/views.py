from Blogapp.models import users,posts

session={ }
#using  decorator

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid user")
    return wrapper


# for user in users:
#     if user["username"]==username and user["password"]==password:
#         print("access granted")
#         break
#     else:
#         print("denied")


def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user

# calling authenticate function
# print(authenticate(username="akhil",password="Password@123"))

class LoginView:
    def post(self,*args,**kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
             session["user"]=user[0]
        # print(session)


#  listing all
class PostListView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        print(kwargs)
        my_post=kwargs.get("data")
        userId=session["user"]["id"]
        my_post["userId"]=userId
        posts.append(my_post)
        print(posts[-1])


class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post

class AddLike:
    @signin_required
    def post(self,*args,**kwargs):
        postId=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postId]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])

log_in=LoginView()
log_in.post(username="richard",password="Password@123")
# # calling post
all_post=PostListView()
# print(all_post.get())
# # object creation
myposts=MyPostListView()
# print(myposts.get())
my_post={
    "postId":9,"title":"hello good morning","content":"mycontent","Liked_by":[]
}
all_post.post(data=my_post)

like=AddLike()
like.post(postid=1)