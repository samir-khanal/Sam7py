# types of data types: 1)number 2)string 3)boolean 4)list 5)set 6)tuple 7)dict 8)none
# number: integer,float,complex
x = 7
print(type(x))
print(dir(x))
# data types ma k k xa tyo dekhauxa (dir) le.
y = 30.5
print(type(y))
z = 20j
print(type(z))

# x = input("name: ")
# y = input("Address: ")
# z = input("phone: ")
# print(x, y, z)

# type-casting
# x = int(input("enter x: "))
# y = int(input("enter y: "))
# print(x + y)
# boolean is used as true or false.
print(100 > 20)

# data={1,2,3,1}
# print(data)
# data={} is a dictionary
data={
     "name":"ram",
     "address": {
     "location":"kathmandu"
 } }
print(data["address"]["location"])