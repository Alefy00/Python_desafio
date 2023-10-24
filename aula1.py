calcular = """
[+] adição
[-] subtração
[*] multplicação
[/] divisão

=> """

while True:
    opcao = input(calcular)
    if  opcao == "+":

        primeiro_valor = int(input("Digite o primeiro numero: "))
        segundo_valor = int(input("Digite o segundo numero: "))
        
        total = primeiro_valor + segundo_valor
        print(total)
    elif opcao == "-":
        primeiro_valor = int(input("Digite o primeiro numero: "))
        segundo_valor = int(input("Digite o segundo numero: "))
        
        total = primeiro_valor - segundo_valor
        print(total)
    elif opcao == "*":
        primeiro_valor = int(input("Digite o primeiro numero: "))
        segundo_valor = int(input("Digite o segundo numero: "))
        
        total = primeiro_valor * segundo_valor
        print(total)
    elif opcao == "/":
        primeiro_valor = int(input("Digite o primeiro numero: "))
        segundo_valor = int(input("Digite o segundo numero: "))
        
        total = primeiro_valor // segundo_valor
        print(total)
        

    else:
        print("insira um valor valido")
    



    
