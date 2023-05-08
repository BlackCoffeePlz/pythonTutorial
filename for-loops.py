# For-loops perform a set of actions per iteration of a collection in sequence.
# A for-loop is constructed with the for keyword, followed by a variable to represent
# each item found, and finally the collection to loop over.

some_collection = ['Apple', 'Orange', 'Pear']

for item in some_collection:
    item = item.upper()
    print(item)

# The sequence of code does not necessarily have to perform
# an action on the collection. For-loops can be used to repeat
# actions.

x = 5
for i in range(5):
    x += 2
    print(f'X Value: {x}')


