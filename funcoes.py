
'''Faça uma função para converter uma temperatura em graus Fahrenheit para Celsius. A temperatura em Fahrenheit é o dado de entrada e a temperatura em Celsius é o dado de saída. Utilize a fórmula C = (F - 32) * 5/9, onde F é a temperatura em Fahrenheit e C é a temperatura em Celsius.'''
def fahrenheit_para_celsius(temp_fahrenheit):
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    return temp_celsius

fahrenheit = float(input('Digite a temperatura em Fahrenheit:  '))
celsius = fahrenheit_para_celsius(fahrenheit)
print(f"{fahrenheit} graus Fahrenheit é igual a {celsius:.2f} graus Celsius.")

"""Faça uma função que calcule a hipotenusa. Os catetos são os dados de entrada e a hipotenusa é o dado de saída."""

import math


def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa


a = float(input("Digite o valor do cateto A: "))
b = float(input("Digite o valor do cateto B: "))
hipotenusa = calcular_hipotenusa(a, b)
print(f"A hipotenusa com catetos {a} e {b} é igual a {hipotenusa:.2f}.")

"""Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça uma função que receba as duas notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação)."""

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


def aprovacao(media):
    if media >= 6.0:
        print(f"Parabens voce foi aprovado!!! Sua media final foi {media}")
    else:
        print("Voce foi reprovado")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)

aprovacao(media)

print(f"Sua média semestral é {media} ")

"""Faça um programa que leia a altura e o sexo (codificado da seguinte forma: 1-feminino 2-masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
• para homens: (72.7 * h) – 58
• para mulheres: (62.1 * h) – 44.7
Observação: Altura = h (na fórmula acima).
"""

def pesoideal(altura, sexo):
    if sexo == 1:
        peso = (62.1 * altura) - 44.7
    elif sexo == 2:
        peso = (72.7 * altura) - 58
    else:
        print("Código de sexo inválido. Use 1 para feminino e 2 para masculino.")
        return None
    return peso

altura = float(input('Digite sua altura:'))
sexo =  int(input("Digite o código do sexo (1 - feminino, 2 - masculino): "))

pesoideal = pesoideal(altura, sexo)

if pesoideal is not None:
    print('Seu peso ideal é', pesoideal, 'kg')

"""Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça uma função que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
• Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
• Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
• Se o número de lados for igual a 5, escrever PENTÁGONO.

"""

def calcular_poligono(num_lados, medida_lado):
    if num_lados == 3:
        perimetro = num_lados * medida_lado
        print(f"TRIÂNGULO - Perímetro: {perimetro} cm")
    elif num_lados == 4:
        area = medida_lado * medida_lado
        print(f"QUADRADO - Área: {area} cm²")
    elif num_lados == 5:
        print("PENTÁGONO")
    else:
        print("Número de lados inválido. Informe apenas 3, 4 ou 5.")

num_lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado do polígono (em cm): "))

if num_lados in [3, 4, 5]:
    calcular_poligono(num_lados, medida_lado)
else:
    print("Número de lados inválido. Informe apenas 3, 4 ou 5.")

"""6."""

def soma_intervalo(n1, n2):

    soma = 0

    if n1 <= n2:

        for num in range(n1, n2 + 1):
            soma += num
    else:
        for num in range(n2, n1 + 1):
            soma += num

    return soma


n1 = int(input("Digite o valor de n1: "))
n2 = int(input("Digite o valor de n2: "))

resultado = soma_intervalo(n1, n2)
print(f"A soma dos números inteiros no intervalo [{n1}, {n2}] é: {resultado}")

"""7."""

def imprimir_mes_correspondente(numero):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }

    if numero in meses:
        print(meses[numero])
    else:
        print("Número inválido. Digite um número de 1 a 12 correspondente a um mês.")


numero_mes = int(input("Digite um número de 1 a 12 correspondente a um mês: "))


imprimir_mes_correspondente(numero_mes)

"""8."""

def imprimir_tres_primeiros_dias_semana(numero):
    dias_semana = {
        1: "DOM",
        2: "SEG",
        3: "TER",
        4: "QUA",
        5: "QUI",
        6: "SEX",
        7: "SAB"
    }

    if numero in dias_semana:
        print(dias_semana[numero])
    else:
        print("Número inválido. Digite um número de 1 a 7 correspondente a um dia da semana.")

numero_dia = int(input("Digite um número de 1 a 7 correspondente a um dia da semana: "))


imprimir_tres_primeiros_dias_semana(numero_dia)

"""9."""

def verificar_divisibilidade(x, y):
    if x % y == 0:
        return 1
    else:
        return 0

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))


resultado = verificar_divisibilidade(x, y)
print(f"Resultado: {resultado}")

"""10."""

def calcular_maior_valor(a, b):
    if a > b:
        return a
    else:
        return b

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

maior_valor = calcular_maior_valor(valor1, valor2)
print(f"O maior valor entre {valor1} e {valor2} é: {maior_valor}")

"""11."""

def polegadas_para_cm(pol):
    return pol * 2.54

valor_pol = float(input("Digite o valor em polegadas: "))

valor_cm = polegadas_para_cm(valor_pol)
print(f"{valor_pol} polegadas equivalem a {valor_cm} centímetros.")