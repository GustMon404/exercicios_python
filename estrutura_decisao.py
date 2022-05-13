# 1
def maior_que():
    num_1 = input("Digite um numero: ")
    num_2 = input("Digite um numero: ")
    maior = num_1 if num_1 > num_2 else num_2
    print(maior)


# maior_que()

# 2
def valor_eh():
    num = int(input("Digite um numero: "))
    afirmacao = 'Positivo' if num > 0 else 'Negativo'
    print(afirmacao)


# valor_eh()

# 3
def feminino_ou_masculino(letra: str):
    if letra == 'F':
        print('Feminino')
    elif letra == 'M':
        print('Masculino')
    else:
        print('Invalido')


# feminino_ou_masculino('F')

# 4
def vogal_ou_consoante(letra: str):
    vogais = 'aeiou'
    if letra in vogais:
        print('É uma vogal')
    else:
        print("É uma consoante")


# vogal_ou_consoante('u')

# 5
def media_aluno(nota1: int, nota2: int) -> str:
    nota = (nota1 + nota2) / 2
    if nota == 10:
        return 'Aprovado com Distinção'
    elif nota >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'


# print(media_aluno(5,5))

# 6
def maior_de_tres(num1: int, num2: int, num3: int):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)


# maior_de_tres(3,11,5)

# 7
def maior_menor_de_tres(num1: int, num2: int, num3: int):
    maior = num1
    if maior < num2:
        maior = num2
    elif maior < num3:
        maior = num3

    menor = num1
    if num2 < menor:
        menor = num2
    elif num3 < menor:
        menor = num3

    print(f'Maior {maior}, Menor:{menor}')


# maior_menor_de_tres(5,11,9)

# 8
def menor_preco():
    produtos = {
        'Produto 1': int(input(f'Valor do produto 1: ')),
        'Produto 2': int(input(f'Valor do produto 2: ')),
        'Produto 3': int(input(f'Valor do produto 3: '))
    }

    menor_para_maior = sorted(produtos.items(), key=lambda produto: produto[1])

    menor_produto = list(dict(menor_para_maior).keys())[0]

    print(f'Menor prdouto {menor_produto}')


# menor_preco()

# 9
def ordem_crescente(n1, n2, n3):
    lista_crescente = [n1, n2, n3]
    print(sorted(lista_crescente))


# ordem_crescente(10, 12, 9)

# 10
def turno_estudo():
    letra_turno = input('Digite M[matutino] ou V[Vespertino] ou N[Noturno]: ').upper()

    todos_turnos = {
        'M': 'Bom Dia!',
        'V': 'Boa Tarde!',
        'N': 'Boa Noite'
    }
    turno_encontrado = todos_turnos.get(letra_turno)
    turno = 'Valor Inválido' if turno_encontrado is None else turno_encontrado

    print(turno)


# turno_estudo()

# 11
def aumento_salarial():
    valor = int(input('Digite seu salario: '))
    salario_reaj = {}

    if valor <= 280:
        salario_reaj = {'salario': valor, 'porcentagem': 20, 'reajuste': valor * (20 / 100) + valor}
    elif 280 < valor <= 700:
        salario_reaj = {'salario': valor, 'porcentagem': 15, 'reajuste': valor * (15 / 100) + valor}
    elif 700 < valor <= 1500:
        salario_reaj = {'salario': valor, 'porcentagem': 10, 'reajuste': valor * (10 / 100) + valor}
    else:
        salario_reaj = {'salario': valor, 'porcentagem': 5, 'reajuste': valor * (20 / 100) + valor}

    print(salario_reaj)


# aumento_salarial()

# 12
def folha_pagamento():
    valor_hora = int(input('Valor da hora: '))
    qtd_horas = int(input('quantidade hora trabalhada: '))
    salario_bruto = valor_hora * qtd_horas
    percentual_ir = 0

    if salario_bruto >= 2500:
        percentual_ir = 20
    elif salario_bruto >= 1500:
        percentual_ir = 10
    elif salario_bruto >= 900:
        percentual_ir = 5

    ir = salario_bruto * (percentual_ir / 100)
    inss = salario_bruto * (10 / 100)
    fgts = salario_bruto * (11 / 100)

    print(f"Salario Bruto({valor_hora} * {qtd_horas}): {salario_bruto} \n"
          f"(-) IR ({percentual_ir}%): R${ir} \n"
          f"(-) INSS (10%): R${inss} \n"
          f"FGTS (11%): {fgts} \n"
          f"Total de descontos: {ir + inss} \n"
          f"Salario Liquido: {salario_bruto - (ir + inss)}"
          )


# folha_pagamento()

# 13
def dia_semana():
    semana_list = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
    num_semana = int(input('Digite um numero: '))
    semana = semana_list[num_semana - 1] if 0 < num_semana <= 7 else 'Valor Inválido'
    # semana = {i: mes for i, mes in enumerate(semana_list, 1)}
    # print(semana.get(num_semana))
    print(semana)


# dia_semana()

# 14
def media_conceito(n1, n2):
    disciplina = [
        {'nota': 9, 'conceito': 'A'},
        {'nota': 7.5, 'conceito': 'B'},
        {'nota': 6.0, 'conceito': 'C'},
        {'nota': 4.0, 'conceito': 'D'},
        {'nota': 0, 'conceito': 'E'}
    ]

    media = (n1 + n2) / 2

    nota_conceito = next(filter(lambda c: c.get('nota') <= media, disciplina))
    nota_conceito['resultado'] = 'Aprovado' if nota_conceito['nota'] >= 6 else 'Reprovado'

    print(f"Nota 1: {n1}, Nota 2: {n2}, Nota media: {media}, Conceito: {nota_conceito['conceito']},"
          f"Resultado: {nota_conceito['resultado']}")


media_conceito(9, 8.5)


# 25
def perguntas() -> None:
    positivo = 0
    positivo += 1 if input('Telefonou para a vítima?') == 'sim' else 0
    positivo += 1 if input('Esteve no local do crime?') == 'sim' else 0
    positivo += 1 if input('Mora perto da vítima?') == 'sim' else 0
    positivo += 1 if input('Devia para a vítima?') == 'sim' else 0
    positivo += 1 if input('Já trabalhou com a vítima?') == 'sim' else 0

    acusado = 'Cidadão de bem'

    if positivo == 5:
        acusado = 'Assasino'
    elif positivo == 3 or positivo == 4:
        acusado = 'Cúmplice'
    elif positivo == 2:
        acusado = 'Suspeito'

    print(f'Você é um {acusado}')


# perguntas()


# 28
def tabajara() -> None:
    carnes = {'File Duplo': {'precoAte5kg': 4.90, 'precoMais5kg': 5.80},
              'Alcatra': {'precoAte5kg': 5.90, 'precoMais5kg': 6.80},
              'Picanha': {'precoAte5kg': 6.90, 'precoMais5kg': 7.80}
              }

    item = input('Qual carne gostaria de levar ? ').title()
    qtd = int(input('Quanto kg ? '))
    forma_pagamento = input('Qual a forma de pagamento ? ').title()

    preco = carnes[item]['precoAte5kg' if (qtd <= 5) else 'precoMais5kg']
    pedido = preco * qtd

    total = pedido - (pedido * 0.05) if (forma_pagamento == 'Cartao') else pedido

    print("{:<15} {:<8} {:<5} {:<10} {:<10}".format('carne', 'Preço', 'Qtd', 'Desconto', 'total'))
    print("{:<15} {:<8} {:<5} {:<10} {:<10}".format(item, preco, qtd, forma_pagamento, total))

# tabajara()
