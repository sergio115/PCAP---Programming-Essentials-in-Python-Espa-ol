# Datos de prueba

# Entrada de muestra: 10000

# Resultado esperado: El impuesto es: 1244.0 pesos

# Entrada de muestra: 100000

# Resultado esperado: El impuesto es: 19470.0 pesos

# Entrada de muestra: 1000

# Resultado esperado: El impuesto es: 0.0 pesos

# Entrada de muestra: -100

# Resultado esperado: El impuesto es: 0.0 pesos

ingreso = None

excencionFiscal = 556.02
impuestoPorcentajeMenor = 0.18

ingresoBaseMayor = 85528.00
impuestoBaseMayor = 14839.02
impuestoPorcentajeMayor = 0.32
excedenteMayor = None

ingreso = float(input("Ingrese el ingreso anual:"))

if ingreso < ingresoBaseMayor:
    impuesto = (impuestoPorcentajeMenor * ingreso) - excencionFiscal
elif ingreso >= ingresoBaseMayor:
    excedenteMayor = ingreso - ingresoBaseMayor
    impuesto = impuestoBaseMayor + (impuestoPorcentajeMayor * excedenteMayor)

if impuesto <= 0:
    impuesto = 0

impuesto = round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
