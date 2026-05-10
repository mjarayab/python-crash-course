# Ejercicio 3 — Medio 
# Tenés tres clasificaciones posibles para un punto en una carta de control:
# pythonclasificaciones = ["en control", "advertencia", "fuera de control"]
# Pedile al usuario un valor numérico con input(). 
# Si está entre 0 y 1 sigma 
# imprimí "en control", entre 1 y 2 sigma "advertencia", más de 2 sigma "fuera 
# de control". Usá la clasificación de la lista para imprimir el mensaje.
clasificaciones = ["en control", "advertencia", "fuera de control"]
numero = float(input("Ingrese un valor sigma: "))
if numero < 1:
    print("El valor sigma no puede ser negativo")
elif numero <= 1:
    print(clasificaciones[0])
elif numero > 1 and numero <= 2:
    print(clasificaciones[1])
else:
    print(clasificaciones[2])