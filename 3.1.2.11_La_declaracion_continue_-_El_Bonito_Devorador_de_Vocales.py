#  Datos de prueba

# Entrada de muestra: Gregory

# Salida esperada:
# GRGRY

# Entrada de muestra: abstemious

# Salida esperada:
# BSTMS

# Entrada de muestra: IOUEA

# Salida esperada:
#

palabraSinVocal = ""
userWord = ""

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
        palabraSinVocal += letra

print(palabraSinVocal)
