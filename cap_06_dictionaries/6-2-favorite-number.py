# Use a dictionary to store people’s favorite numbers. Think of five names, and 
# use them as keys in your dictionary. Think of a favorite number for each 
# person, and store each as a value in your dictionary. Print each person’s 
# name and their favorite number. For even more fun, poll a few friends and 
# get some actual data for your program.

favorite_numbers = {
    "mauricio" : 25,
    "ana" : 15,
    "matias" : 46,
    "raul"  : 20,
    "luis" : 00
}

# Imprimiendo numeros favoritos.
print(f"El numero favorito de Mauricio es: {favorite_numbers['mauricio']}")
print(f"El numero favorito de Ana es: {favorite_numbers['ana']}")
print(f"El numero favorito de Matias es: {favorite_numbers['matias']}")
print(f"El numero favorito de Raul es: {favorite_numbers['raul']}")
print(f"El numero favorito de Luis es: {favorite_numbers['luis']}")