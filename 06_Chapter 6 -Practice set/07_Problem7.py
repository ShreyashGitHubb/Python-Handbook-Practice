#  Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter the post: ")

post_lower = post.lower()

if "harry" in post_lower:
    print("The post is talking about Harry.")

else:
    print("The post is not talking about Harry.")
