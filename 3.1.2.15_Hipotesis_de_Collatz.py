numero = int(input("Ingrese un número: "))
estaResuelto = False
pasos = 0

if numero >= 1:
    while estaResuelto == False:
        if numero != 1:
            if (numero % 2) == 0:
                numero //= 2
            else:
                numero = (3 * numero) + 1

            pasos += 1
            print(numero)
        else:
            estaResuelto = True

print("pasos =", pasos)

# Datos de prueba

# Entrada de muestra: 15

# Salida esperada:
# 46
# 23
# 70
# 35
# 106
# 53
# 160
# 80
# 40
# 20
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# pasos = 17

# Entrada de muestra: 16

# Salida esperada:
# 8
# 4
# 2
# 1
# pasos = 4

# Entrada de muestra: 1023

# Salida esperada:
# 3070
# 1535
# 4606
# 2303
# 6910
# 3455
# 10366
# 5183
# 15550
# 7775
# 23326
# 11663
# 34990
# 17495
# 52486
# 26243
# 78730
# 39365
# 118096
# 59048
# 29524
# 14762
# 7381
# 22144
# 11072
# 5536
# 2768
# 1384
# 692
# 346
# 173
# 520
# 260
# 130
# 65
# 196
# 98
# 49
# 148
# 74
# 37
# 112
# 56
# 28
# 14
# 7
# 22
# 11
# 34
# 17
# 52
# 26
# 13
# 40
# 20
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# pasos = 62
