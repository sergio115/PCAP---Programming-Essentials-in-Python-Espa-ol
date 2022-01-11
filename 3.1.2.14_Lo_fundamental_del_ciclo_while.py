# Datos de prueba

# Entrada de muestra: 6

# Producto esperado: La altura de la pirámide es: 3

# Entrada de muestra: 20

# Salida esperada: La altura de la pirámide es: 5

# Entrada de muestra: 1000

# Resultado esperado: La altura de la pirámide es: 44

# Entrada de muestra: 2

# Salida esperada: La altura de la pirámide es: 1

bloques = int(input("Ingrese el número de bloques: "))
altura = 0

while bloques > 0:
    longitudNecesariaDelNivel = altura + 1

    if longitudNecesariaDelNivel <= bloques:
        bloques -= longitudNecesariaDelNivel
        altura += 1
    else:
        break

print("La altura de la pirámide:", altura)
print("Sobran:", bloques, "bloque(s).")
