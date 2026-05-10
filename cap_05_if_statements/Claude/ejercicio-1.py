# Ejercicio 1 — Básico: Tenés estos valores de temperatura de un horno:
# pythontemperaturas = [482, 479, 485, 501, 478, 493, 488, 476, 495, 502]
# Imprimí cuáles temperaturas están fuera del rango de especificación 
# (mínimo 478, máximo 498), usando un bucle for y un if/else.
pythontemperaturas = [482, 479, 485, 501, 478, 493, 488, 476, 495, 502]
fuera_spec_temperaturas =[]
for temperatura in pythontemperaturas:
    if temperatura < 478 or temperatura > 498:
        fuera_spec_temperaturas.append(temperatura)
print(fuera_spec_temperaturas)