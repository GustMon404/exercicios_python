import math

#13
def altura_ideal(h: float):
    print("Peso ideal caso seja Homem {0} kg".format(round(72.7*h -58, 2)))
    print("Peso ideal caso seja Mulher {0} kg".format(round(62.1*h - 44.7, 2)))
    
altura_ideal(1.5)

#14
def valor_excedente(peso: float):
    excesso = 0 if peso <= 50 else peso-50
    multa = excesso * 4
    
    print("Seu excesso foi de {}kg, você irá pagar R${}".format(excesso, multa))
    
valor_excedente(55)

#15
def valor_hora(valor: float):
    salario_bruto = valor
    ir = valor * (11/100)
    inss = valor * (8/100)
    sindicato = valor * (5/100)
    salario_liquido =salario_bruto - (ir + inss + sindicato)
    print('+ Salário Bruto : R${0} \n- IR (11%) : R${1} \n- INSS (8%) : R${2} \n- Sindicato ( 5%) : R${3} \n= Salário Liquido : R${4}'
          .format(salario_bruto, ir, inss, sindicato, salario_liquido))  
    
valor_hora(20)

#16
# def qtd_lata_metro_quadrado(metro: int):
#     metro_18L = 18*3
#     quociente = metro / metro_18L
#     qtd_latas = math.ceil(quociente / 54)
#     print(f"Quandidades de latas necessárias {qtd_latas}, equivalente a: R${qtd_latas * 80}")
    
# qtd_lata_metro_quadrado(50)

#17
def qtd_lata_metro_quadrado_2(metro: int):
    metro_18L = metro/(18*6)
    metro_3600ml = metro/(3.6*6)
    
    qtds_latas_18L = math.ceil(metro_18L)
    qtds_latas_3600ml = math.ceil(metro_3600ml)
    
    qtd_latas_com_margem = math.ceil((metro_3600ml*(10/100)) + metro_3600ml)
    qtd_lt_18, qtd_lt_3600 = (qtd_latas_com_margem//5), (qtd_latas_com_margem % 5)
    
    print(f"Quandidades de latas necessárias {qtds_latas_18L}, equivalente a: R${qtds_latas_18L * 80}")
    print(f"Quandidades de latas necessárias {qtds_latas_3600ml}, equivalente a: R${qtds_latas_3600ml * 25}")
    print(f"Você precisará de {qtd_lt_18} lata de 18L e {qtd_lt_3600} lata de 3.6L, equivalente há R${(qtd_lt_18*80) + (qtd_lt_3600 * 25)}")
    
    
qtd_lata_metro_quadrado_2(150);

#18
def tempo_download():
    tamanho_arq = int(input('Tamanho do arquivo em mega: '))
    velocidade = int(input('velociade da internet: '))
    velocidade_bytes = velocidade / 8
    tempo_minutos = (tamanho_arq / velocidade_bytes) / 60
    print(f'O download levará {round(tempo_minutos,2)} min')

tempo_download()
