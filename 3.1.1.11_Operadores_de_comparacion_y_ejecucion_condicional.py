# Datos de prueba

# Entrada de muestra: espatifilo

# Resultado esperado: No, ¡quiero un gran Espatifilo!

# Entrada de ejemplo: pelargonio

# Resultado esperado: !Espatifilo! ¡No pelargonio!

# Entrada de muestra: Espatifilo

# Resultado esperado: Si, ¡El Espatifilo es la mejor planta de todos los tiempos!

planta = input("Ingresa el nombre de una planta: ")
espatifiloGrande = "Espatifilo"
espatifiloChico = "espatifilo"

if planta == espatifiloGrande:
    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif planta == espatifiloChico:
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("!Espatifilo! ¡No " + planta + "!")
