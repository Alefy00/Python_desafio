# Solicita ao usuário o número de disciplinas
num_disciplinas = int(input("Quantas disciplinas você deseja calcular a média? "))

# Inicializa a variável que armazenará a soma das notas
soma_notas = 0

# Loop para solicitar notas para cada disciplina
for i in range(1, num_disciplinas + 1):
    nota = float(input(f"Digite a nota da disciplina {i}: "))
    
    # Verifica se a nota está dentro da faixa válida (0-10)
    if nota < 0 or nota > 10:
        print("Nota inválida. As notas devem estar na faixa de 0 a 10.")
        break  # Sai do loop em caso de nota inválida
    soma_notas += nota

# Calcula a média das notas
media = soma_notas / num_disciplinas

# Exibe a média e a situação do aluno
print(f"\nA média das notas é: {media:.2f}")
if media >= 6:
    print("Aluno APROVADO.")
else:
    print("Aluno REPROVADO.")
