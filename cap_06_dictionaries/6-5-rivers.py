#  Make a dictionary containing three major rivers and the country each river 
# runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through 
# Egypt.

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'orinoco': 'colombia'
    }
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.") 