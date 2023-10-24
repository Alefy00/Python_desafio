# Solicita ao usuário que escolha a unidade de temperatura de entrada

unidade_origem = input("Escolha a unidade de temperatura de entrada (Celsius, Fahrenheit, Kelvin): ").lower()

# Solicita ao usuário que insira o valor da temperatura

valor = float(input("Digite o valor da temperatura: "))

# Solicita ao usuário que escolha a unidade de temperatura para a conversão

unidade_destino = input("Escolha a unidade de temperatura para a conversão (Celsius, Fahrenheit, Kelvin): ").lower()

# Função para converter a temperatura
def converter_temperatura(valor, origem, destino):
    if origem == destino:
        return valor
    if origem == "celsius":
        if destino == "fahrenheit":
            return (valor * 9/5) + 32
        elif destino == "kelvin":
            return valor + 273.15
    elif origem == "fahrenheit":
        if destino == "celsius":
            return (valor - 32) * 5/9
        elif destino == "kelvin":
            return (valor - 32) * 5/9 + 273.15
    elif origem == "kelvin":
        if destino == "celsius":
            return valor - 273.15
        elif destino == "fahrenheit":
            return (valor - 273.15) * 9/5 + 32

# Realiza a conversão
resultado = converter_temperatura(valor, unidade_origem, unidade_destino)

# Exibe o resultado
print(f"Resultado: {resultado} {unidade_destino.capitalize()}")
