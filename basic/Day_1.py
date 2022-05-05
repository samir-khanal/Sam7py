# Comment is used like this in python.
# variables: 1) it must start with a-z/A-Z or _(underscore).2)it should not contain special characters like(@,$,#)
# standard convention for variable name : 1)first/Name 2)first-name 3)FirstName
# Name="ram" and name="ram" are diff variables.

first_name = "ram"
last_name = "sharma"
print(first_name + last_name)
print(first_name + " " + last_name)
# in string (+) sign combines the words(strings). Concatination = combining strings

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."
# So To fix this problem, use the escape character \" as shown above example.
