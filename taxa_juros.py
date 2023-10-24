#O valor principal (o valor do empréstimo ou investimento).

principal = float(input("Digite o valor que deseja realizar o emprestimo ou invertimento: "))

#A taxa de juros anual (em porcentagem).

taxa_juros_anual = float(input("Digite a taxa de juros anual: "))

taxa_juros_porcentagem = taxa_juros_anual / 100
#O período de tempo (em anos) pelo qual o dinheiro será emprestado ou investido.

tempo = float(input("Digite o tempo(anos) que deseja que o dinheito sera emprestado ou investido: "))

#Em seguida, o programa deve calcular o montante total após o período de tempo especificado e exibir o resultado.

montante = principal + (principal * taxa_juros_porcentagem * tempo)

print(f"O montante total após {str(tempo)} é: {montante:.2f}")