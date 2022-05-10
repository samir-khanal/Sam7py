# types of  function:
# 1. Inbuilt function
# 2. User defined function

# Inbuilt function example:
# 1. abs()
# 2. pow()
# 3. max()
# 4. min()
# 5. round()
# print(dir(__builtins__))

# User defined function example:
def my_function():
    # function body
    print("hello world")


# call function
my_function()

# Parameters example:

# def users(name, age):
#     print("hello", name)
#     print("you are", age, "years old.")
#
#
# users("samir", 20)

# def add(x,y):
#     print(x+y)
#
#
# add(40,50)
# add(70,80)

# Optional parameters example:
# def add(x,y=0):
#     print(x+y)
#
#
# add(40)

# * arguments example:
# **keyword argument example:
# def users(*names,**data):
#     print(names)
#     print(data)
#
#
# users("samir","mobin","abhisek",name="samir",age="20", address="new york")

# def test():
#     print("hello world")
#
#
# def get():
#     test()
#
#
# get()


# return types function
# def add(x, y):
#     return x + y
#
#
# print(add(40, 50))


x = 10


def test():
    print(x)


test()
print(x)

x = 20


def test():
    global x
    x = x + 30
    print(x)


test()
print(x)

# Inline function example
a=lambda x,y:x+y  #lambda is used for a single line statement.
print(a(20,30))


def a(x,y):
    return x+y



# Nested function:
# def users():
#     def name():
#         return "i am samir"
#
#     return name
#
#
# a=users()
# print(a())
# or print(users()())

# def connection():
#     """
#
#     :return:
#     """
