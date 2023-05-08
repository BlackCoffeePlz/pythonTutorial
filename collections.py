# Lists are ordered, mutable (changeable) collection of data.
# Lists can be used to store multiple items in a single variable, and are often signaled
# with brackets [], with commas separating each item.
empty_list: list = []
populated_list = ['Hello', 3, False]

# Add to a list with the .append() method
empty_list.append("New Item")
empty_list.append("Another new Item")

# Remove from a list with the .remove method
populated_list.remove("New Item")

# Remove from a list by index with the .pop() method
populated_list.pop(0)


# Tuples are ordered, immuatable (unchangeable) collection of data.
# Tuple are constructed with parenthesis (), with a comma separating each item.
populated_tuple: tuple = ('Hello', "It's", 'Me')
empty_tuple = ()


# Sets are unordered, mutable collections of data. Unlike lists and tuples,
# sets DO NOT allow duplicate data. Sets are constructed with curly-braces {},
# but to construct an set, you must call the class set().
empty_set: set = set()
populated_set = {'Hello', "It's", 'Me'}
