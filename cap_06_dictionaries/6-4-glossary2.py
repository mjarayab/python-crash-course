# Now that you know how to loop through a dictionary, clean up the code from 
# Exercise 6-3 (page 99) by replacing your series of print() calls with a loop 
# that runs through the dictionary’s keys and values. When you’re sure that your 
# loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should 
# automatically be included in the output.

glossary = {
    'variable': 'Stores a value that can change during the program.',
    'list': 'A collection of items stored in a specific order.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'Repeats a block of code multiple times.',
    'string': 'A sequence of characters or text.',
    'function': 'A block of reusable code that performs a specific task.',
    'tuple': 'An immutable sequence of items that cannot be changed after creation.',
    'boolean': 'A data type with only two values: True or False.',
    'index': 'The position of an element in a list, starting at 0.',
    'method': 'A function that belongs to an object or data type.',
}
for word, meaning in glossary.items():
    print (f"{word.title()}:")
    print (f"\t{meaning}\n")
