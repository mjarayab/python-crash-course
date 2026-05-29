favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name, lenguage in favorite_languages.items():
    print (f"{name.title()}´s favorite lenguage is {lenguage}")
print("\n")
for name in favorite_languages.keys():
    print (name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print (f"Hi, {name.title()}")
    if name in friends:
        leng = favorite_languages[name].title()
        print(f"{name.title()}´s favorite lenguage is {leng}")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for values in sorted(set(favorite_languages.values())):
    print (values.title())