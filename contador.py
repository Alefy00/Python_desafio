#Solicite ao usuário que insira uma frase ou texto.

texto = input("Digite um texto: ")

#Conte o número de palavras no texto. Considere que as palavras são separadas por espaços em branco.

contador = texto.split()

numero_palabras = len(contador)

#Exiba o resultado, ou seja, o número de palavras na frase ou texto.

print(numero_palabras)