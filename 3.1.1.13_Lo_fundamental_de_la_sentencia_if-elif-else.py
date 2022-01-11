# Datos de prueba

# Entrada de muestra: 2000

# Resultado esperado: Año bisiesto

# Entrada de muestra: 2015

# Resultado esperado: Año común

# Entrada de muestra: 1999

# Resultado esperado: Año común

# Entrada de muestra: 1996

# Resultado esperado: Año bisiesto

# Entrada de muestra: 1580

# Resultado esperado: No dentro del período del calendario gregoriano

año = int(input("Introduzca un año:"))

divisibleEntre_4 = año % 4
divisibleEntre_100 = año % 100
divisibleEntre_400 = año % 400

if año >= 1582:
    if divisibleEntre_4 != 0:
        print("Año común")
    elif divisibleEntre_100 != 0:
        print("Año bisiesto")
    elif divisibleEntre_400 != 0:
        print("Año común")
    else:
        print("Año bisiesto")
else:
    print("No dentro del período del calendario gregoriano")
