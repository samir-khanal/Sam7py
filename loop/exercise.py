# users= [["user1", "user123"], ["user2", "user234"],["admin","admin123"]]
# username = input("enter a username:")
# y = (input("enter a password:"))
# total_users = len(list)
# increment = 0
# login_success = False
# while increment < total_users:
#     uname = users[increment][0]
#     upass = users[increment][1]
#     if username == uname and y == upass:
#         login_success: True
#     increment += 1
# if login_success:
#     print(f"welcome{username}")
# else:
#     print("user and password not found")

# x = 10
# while x > 0:
#     print(x)
#     x -= 1

# stop iteration: break,continue
x = 0
while x < 10:
    x += 1
    if x == 1 or x == 4 or x == 9:
        continue
    print(x, end=" ")
