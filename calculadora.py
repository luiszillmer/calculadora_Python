def calculadora():
    print("Bem-vindo à Calculadora Matemática!")
    print("Por favor, escolha a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    operacao = int(input())
    
    if operacao < 1 or operacao > 4:
        print("Operação inválida. Por favor, escolha uma operação válida.")
    else:
        valor1 = float(input("Insira o primeiro valor: "))
        valor2 = float(input("Insira o segundo valor: "))
        
        if operacao == 1:
            resultado = valor1 + valor2
        elif operacao == 2:
            resultado = valor1 - valor2
        elif operacao == 3:
            resultado = valor1 * valor2
        elif operacao == 4 and valor2 != 0:
            resultado = valor1 / valor2
        else:
            print("Erro: divisão por zero.")
            return

if operacao != 4 or valor2 != 0:
    print("O resultado da operação é: ", resultado)
    
    calculadora()
