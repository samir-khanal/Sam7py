# x=10
# y=20
# z=30
# # example of nested if else statements
# if x>y:
#     if x>z:
#         print("x is greater than y and z")
#     else:
#         print("z is larger than x and y")
#
# else:
#     if y>z:
#         print("x is greater than y and z" )
#     else:
#         print("z is greater than y")


username = input("enter your username:")
password = input("enter password:")
if username == "admin":
    if password == "12345":
        print("you are logged in")
    else:
        print("wrong password")
else:
    if password == "12345":
        if username == "admin":
            print("login successful")
        else:
            print("wrong username")
    else:
        print("username and password wrong")
