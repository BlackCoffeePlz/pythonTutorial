# Functions are a named block of code that executes only when it is called.
# Functions are constructed with the def keyword

def some_function():
    return "I am a function"

# To run a function, call its name
some_function()


# Notice how nothing is shown on the screen
# Functions can "return a value" to be referenced when called. To view the returned value,
# Print the function
print(some_function())
reference = some_function()
print(reference)


# Functions can take in arguments, which are values passed in to be used in the block of code.
def arguments_example(input_argument):
    return f"Passed in: {input_argument}"

# To call a function with arguments, add the data you want to pass-in into the function in the same position.
some_value = "I am a value"
new_value = arguments_example(some_value)
print(new_value)


# Functions can take in multiple arguments
def multiple_arguments(arg, arg_two, arg_three):
    return arg, arg_two, arg_three

# Arguments can be inserted based on keyword rather than position
print(multiple_arguments(arg_two="hi", arg="Hello", arg_three="hey"))
