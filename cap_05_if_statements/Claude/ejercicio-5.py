# Ejercicio 5 — Difícil
# Simulá un inspector de calidad. Tenés esta lista de mediciones:
#   mediciones = [10.2, 9.8, 10.5, 11.3, 9.5, 10.1, 11.8, 9.7, 10.3, 12.1]
# El programa debe:
# -Calcular el promedio manualmente con sum() y len() — sin librerías
# -Clasificar cada medición como "OK" si está dentro de ±1 unidad del promedio, 
#   "ADVERTENCIA" si está entre ±1 y ±2 unidades, o "RECHAZO" si está fuera 
#   de ±2 unidades
# -Imprimir cada medición con su clasificación
# -Al final imprimir cuántas mediciones cayeron en cada categoría

mediciones = [10.2, 9.8, 10.5, 11.3, 9.5, 10.1, 11.8, 9.7, 10.3, 12.1]
promedio = (sum(mediciones)/len(mediciones))
print (f"El promedio es: {promedio}")

conteo_ok = 0
conteo_adv = 0
conteo_rech = 0

for medicion in mediciones:
    if promedio - 1 <= medicion <= promedio + 1:
        print(f"{medicion} --> OK")
        conteo_ok = conteo_ok +1
    elif promedio - 2 <= medicion < promedio -1 or promedio + 1 < medicion <= promedio + 2:
        print(f"{medicion} --> ADVERTENCIA")
        conteo_adv = conteo_adv + 1
    else:
        print(f"{medicion} --> RECHAZO")
        conteo_rech = conteo_rech + 1
print(f"\nOK -> {conteo_ok}")
print(f"\nADVERTENCIA -> {conteo_adv}")
print(f"\nRECHAZO -> {conteo_rech}")