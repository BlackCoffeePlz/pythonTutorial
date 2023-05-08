# Dictionaries are collections of contain key-value pairs.
# Keys act as named references to a value.
# Dictionaries are constructed with curley braces {}, and a colon : separating the key: value

# Empty Dictionary
my_dict = {}

# Populated Dictionary
person = {
    "Name": "Jerome",
    "Age": 46,
    "Occupation": "Owner of Jammin' Jeromes"
}

# Keys and values can be of any data type, however it is recommended to keep keys as strings or integers
# if possible.

# Selecting a pair
print(person['Name'])

# Adding pair to a dictionary
person['New Item'] = 'Value'

# Removing from a dictionary
person.pop('New Item')

# Getting list of Keys from a dictionary
person.keys()

# Getting list of values from a dictionary
person.values()

# Iterating over a dictionary
for key, value in person.items():
    ... # Your code here

