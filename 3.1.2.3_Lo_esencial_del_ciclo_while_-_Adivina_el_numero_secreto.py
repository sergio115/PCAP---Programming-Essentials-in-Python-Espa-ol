numero = 0
esNumeroSecreto = False
numeroSecreto = 777

print(
    """
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
"""
)

while esNumeroSecreto == False:
    numero = int(input("Ingrese un número entero: "))

    if numero != numeroSecreto:
        print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    else:
        esNumeroSecreto = True

print("¡Bien hecho, muggle! Eres libre ahora")
