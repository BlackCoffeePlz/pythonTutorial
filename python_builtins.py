# Range: use in loops to iterate over a set of numbers
for i in range(0, 5): # Translates to a collection of <0, 1, 2, 3, 4, 5>
    print(i)


# Enumerate: assigns an index as key to a collection of values
collection = ['Apple', 'Orange', 'Pear']
for index, item in enumerate(collection):
    print(index, item)

# len: returns the count of all items in an iterable
some_string = 'Hello'
collection_count = len(collection)

print(len(some_string))
print(collection_count)

