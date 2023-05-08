# If/Else statements provide us a unique way of controlling our script. Initiated by the if keyword
# a code will only execute if the condition is True

x = 10
y = 5

if x == y:
    print("True")


# Else clause runs a set of code if the condition is not true
if x == y:
    print("X is equal to Y")
else:
    print("X is not equal to Y")


# You can also create multiple conditions with the elif keyword

if x == y:
    print("X is equal to Y")
elif x > y:
    print("X is greater than Y")
elif x < y:
    print("X is less than Y")
else:
    print("X is not equal to Y")