#  Datos de prueba

# Entrada de muestra: Gregory

# Salida esperada:
# G
# R
# G
# R
# Y

# Entrada de muestra: abstemious

# Salida esperada:
# B
# S
# T
# M
# S

# Entrada de muestra: IOUEA

# Salida esperada:
#

userWord = None

userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra)
