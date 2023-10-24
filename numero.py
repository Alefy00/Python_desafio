import random

# Define os limites mínimo e máximo para o número a ser adivinhado
limite_min = 1
limite_max = 100

# Gera um número aleatório dentro do intervalo especificado
numero_secreto = random.randint(limite_min, limite_max)

print("Adivinhe o número entre", limite_min, "e", limite_max)

tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Muito baixo. Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto. Tente novamente.")
    else:
        print("Parabéns! Você adivinhou o número corretamente em", tentativas, "tentativas.")
        break
