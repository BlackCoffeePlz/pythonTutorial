# While loops execute a set of code indefinitely until the condition is satified.

x = 0

while x < 10:
    print(f"{x} is smaller than 10")
    x += 1


# BECAREFUL! make sure to write a way to break your set condition, else it will be trapped in a infinite loop.

while x < 20:
    print("I am stopping")
    break

# The break statement stops a loop's execution.