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
    'string': 'A sequence of characters or text.'
}
print(f"variable:\n\t{glossary['variable']}\n")
print(f"list:\n\t{glossary['list']}\n")
print(f"dictionary:\n\t{glossary['dictionary']}\n")
print(f"loop:\n\t{glossary['loop']}\n")
print(f"string:\n\t{glossary['string']}\n")