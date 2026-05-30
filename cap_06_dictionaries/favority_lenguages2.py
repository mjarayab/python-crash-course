favorite_languages = {
       'jen': ['python', 'rust'],
       'sarah': ['c'],
       'edward': ['rust', 'go'],
       'phil': ['python', 'haskell'],
       }

for name, lenguages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite lenguages are:")
    for lenguage in lenguages:
        print(f"\t{lenguage.title()}")
