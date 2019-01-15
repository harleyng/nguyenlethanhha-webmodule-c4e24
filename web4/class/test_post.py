import mlab 
from models.user import User 
from models.post import Post 

mlab.connect()

# a_random_user = User.objects(username="hihihi").first()
# if a_random_user is None:
#     print("User not found")
# else:
#     new_post = Post(title="HANGRY",
#                     content="HIC",
#                     owner=a_random_user)
#     new_post.save()
#     print("Done saving...")

# Post => Owner
# for post in Post.objects():
#     print("'" + post.title + "'", "by", post.owner.username)


# Owner => Post 
user = User.objects(username="harley").first()
print("Posts owned by" + " " + user.username)
posts = Post.objects(owner=user) 
for post in posts:
    print(post.title)