def take_value():
    p = int(input("enter p:"))
    t = int(input("enter t:"))
    r = int(input("enter r:"))
    return [p, t, r]


def calculate():
    p, t, r = take_value()
    return p * t * r / 100
    ## or res=take_value()
    # p=res[0]
    # t=res[1]
    # r=res[2]
    # return =p*t*r/100


calculate()

#
# def display():
#     print("the interest is:", calculate())
#
#
# display()

# name = input("enter name:")
# time = int(input("enter time:"))
#
#
# def my_repeat(data, n_times):
#     increment = 1
#     while increment <= n_times:
#         print(data)
#         increment += 1
#
#
# my_repeat(name, time)


# num_1 = int(input("enter a number:"))
# num_2 = int(input("enter a number:"))
# num_3 = int(input("enter a number:"))
#
#
# def add_sub_mul_div(num_1, num2, num3):
#     add = num_1 + num2 + num3
#     sub = num_1 - num2 - num3
#     mul = num_1 * num2 * num3
#     div = num_1 / num2 / num3
#     return [add, sub, mul, div]
#     print(add, sub, mul, div)
#
# add_sub_mul_div(num_1, num_2, num_3)


# zip()

data = []
