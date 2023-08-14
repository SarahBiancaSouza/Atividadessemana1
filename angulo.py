import math

angulo_graus = float(input("Digite o ângulo em graus: "))
angulo_radianos = math.radians(angulo_graus)  # Convertendo para radianos

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Seno do ângulo: {seno}")
print(f"Cosseno do ângulo: {cosseno}")
print(f"Tangente do ângulo: {tangente}")
