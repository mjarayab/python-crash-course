# A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary. Think of five 
# programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings 
# as values. Print each word and its meaning as neatly formatted output. You might print 
# the word followed by a colon and then its meaning, or print the word 
# on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each 
# word-meaning pair in your output.

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
