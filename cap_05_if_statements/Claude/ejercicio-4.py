# Ejercicio 4 — Medio-difícil
# Tenés los tiempos de ciclo de dos máquinas:

# maquina_a = [45, 42, 48, 51, 43, 46, 50, 44]
# maquina_b = [38, 41, 37, 52, 39, 40, 55, 38]

# Combiná ambas en una lista, ordénalas, e imprimí:
# -El tiempo mínimo y máximo
# -Cuántos tiempos están por encima de 48 segundos
# -Los 3 tiempos más bajos de cada máquina por separado usando slicing

maquina_a = [45, 42, 48, 51, 43, 46, 50, 44]
maquina_b = [38, 41, 37, 52, 39, 40, 55, 38]
tiempos_ciclo = maquina_a + maquina_b
# Tiempos maximo y minimo.
print(f"El tiempo maximo es: {max(tiempos_ciclo)}")
print(f"El tiempo minimo es: {min(tiempos_ciclo)}")
# Tiempos mayores a 48.
tiempos_altos = []
for tiempo in tiempos_ciclo:
    if tiempo > 48:
        tiempos_altos.append(tiempo)
print(f"\nTiempos por encima de 48: {len(tiempos_altos)} - {tiempos_altos}")
# Los 3 mas bajos de cada maquina
maquina_a.sort()
maquina_b.sort()
print(f"Los 3 tiempos mas bajos de maquina a: {maquina_a[:2]}")
print(f"Los 3 tiempos mas bajos de maquina b: {maquina_b[:2]}")

