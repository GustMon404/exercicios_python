#5
def media_aluno(nota1: int, nota2: int) -> str:
    nota = (nota1 + nota2) / 2
    if nota == 10:
        return 'Aprovado com Distinção'
    elif nota >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'
    
print(media_aluno(5,5))

#25
def perguntas() -> None:
    positivo = 0
    positivo += 1 if input('Telefonou para a vítima?') == 'sim' else 0
    positivo += 1 if input('Esteve no local do crime?') == 'sim' else 0
    positivo += 1 if input('Mora perto da vítima?') == 'sim' else 0
    positivo += 1 if input('Devia para a vítima?') == 'sim' else 0
    positivo += 1 if input('Já trabalhou com a vítima?') == 'sim' else 0
    
    acusado = 'Cidadão de bem'
    
    if (positivo == 5):
        acusado = 'Assasino'
    elif(positivo == 3 or positivo == 4):
        acusado = 'Cúmplice'
    elif(positivo == 2):
        acusado = 'Suspeito'
    
    print(f'Você é um {acusado}')
    
perguntas()
    
    
#28    
def tabajara() -> None:
    carnes = {'File Duplo':{'precoAte5kg': 4.90, 'precoMais5kg': 5.80},
              'Alcatra':{'precoAte5kg': 5.90, 'precoMais5kg': 6.80},
              'Picanha':{'precoAte5kg': 6.90, 'precoMais5kg': 7.80}
              }
    
    item =input('Qual carne gostaria de levar ? ').title()
    qtd = int(input('Quanto kg ? '))
    forma_pagamento = input('Qual a forma de pagamento ? ').title()
    
    preco = carnes[item]['precoAte5kg' if (qtd <= 5) else 'precoMais5kg']
    pedido = preco * qtd
    
    total = pedido-(pedido*0.05) if(forma_pagamento == 'Cartao') else pedido
    
    print ("{:<15} {:<8} {:<5} {:<10} {:<10}".format('carne','Preço','Qtd','Desconto', 'total'))
    print ("{:<15} {:<8} {:<5} {:<10} {:<10}".format(item, preco,qtd,forma_pagamento, total))
    
tabajara()