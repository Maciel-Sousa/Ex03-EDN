# Programa para classificar a idade da pessoa

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma Criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um Adolescente.")
elif idade >= 18 and idade <= 59:
    print("Você é um Adulto.")
elif idade >= 60:
    print("Você é um Idoso.")
else:
    print("Idade inválida.")

# Programa que calcula o IMC (Índice de Massa Corporal)

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)

print("Seu IMC é:", round(imc, 2))

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obeso")

    # Programa para converter temperatura entre Celsius, Fahrenheit e Kelvin

temperatura = float(input("Digite a temperatura: "))
origem = input("De qual unidade? (C/F/K): ").upper()
destino = input("Para qual unidade? (C/F/K): ").upper()

if origem == "C" and destino == "F":
    resultado = (temperatura * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = temperatura + 273.15
elif origem == "F" and destino == "C":
    resultado = (temperatura - 32) * 5/9
elif origem == "F" and destino == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    resultado = temperatura - 273.15
elif origem == "K" and destino == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
elif origem == destino:
    resultado = temperatura
else:
    resultado = None

if resultado is not None:
    print(f"Temperatura convertida: {round(resultado, 2)}°{destino}")
else:
    print("Unidade inválida.")

    # Programa para verificar se um ano é bissexto

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")