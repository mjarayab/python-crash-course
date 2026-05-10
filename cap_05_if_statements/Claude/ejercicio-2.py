# Ejercicio 2 — Básico-medio
# Usando range() y list comprehension, generá una lista de 20 números de lote
# empezando en el 5001. Luego imprimí solo los lotes impares.
# El % es el operador módulo — devuelve el residuo de la división. 
# Si lote % 2 != 0 significa que no es divisible entre 2, o sea es impar.
numeros_lote = [value for value in range(5001, 5021)]
print([lote for lote in numeros_lote if lote % 2 != 0])