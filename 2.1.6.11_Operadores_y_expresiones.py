# Datos de Prueba

# Entrada de muestra:
# 12
# 17
# 59

# Salida esperada: 13:16

# Entrada de muestra:
# 23
# 58
# 642

# Salida esperada: 10:40

# Entrada de muestra:
# 0
# 1
# 2939

# Salida esperada: 1:0

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
minutosDuracion = str((min + dura) % 60)
horaDuracion = str(((hora*60 + min + dura)//60) % 24)

print(horaDuracion + ":" + minutosDuracion)
