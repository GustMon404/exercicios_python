#31
def coveniencia_tabajara() -> None:
    produtos = []
    valor_total = 0
    
    count = 1
    while True:
        produto_valor = float(input('Digite o Valor: '))
        if(produto_valor == 0):
            break
        
        produtos.append([f'Produtos {count}:', produto_valor])
        valor_total += produto_valor
        count += 1
        
    pago = int(input('Valor a pagar: '))
    troco = pago - valor_total
               
    print('Tabajara')
    for produto in produtos:
        print ("{:<15} R${:<10}".format(produto[0], produto[1]))
    print("{:<15} R${:<10}".format('Total', round(valor_total,2)))
    print("{:<15} R${:<10}".format('Valor Pago', pago))

    if(pago < valor_total):
        print('valor insuficiente')
    else:  
        print("{:<15} R${:<10}".format('Troco', round(troco,2)))


    if input('Deseja continuar? ') == 'sim':
        coveniencia_tabajara()

coveniencia_tabajara()

#46
def media_nota():
    resultado = []
    nome_atleta = input('Atleta: ')

    if nome_atleta == '':
        return

    ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
    for i in range(5):
        resultado.append(float(input(f'{ordem[i]} Salto: ')))

    resultado.sort()
    melhor_salto = resultado[len(resultado)-1]
    pior_salto = resultado[0]
        
    resultado.remove(melhor_salto)
    resultado.remove(pior_salto)
    
    media_restante = round(sum(resultado)/len(resultado),2)

    print(f'Atleta:{nome_atleta}')
    print(f'Melhor salto: {melhor_salto}')
    print(f'Pior salto: {pior_salto}')
    print(f'Média dos demais saltos: {media_restante}')
    print('Resultado final')
    print(f'{nome_atleta}: {media_restante}')

    media_nota()

media_nota()

#51
def soma_n_termos(n):
    n1, n2 = 1,1
    count = 0
    
    valores = []
    while count < n: 
        valores.append(n1/n2)
        n1+= 1
        n2+=2
        count +=1
    
    print(f'Soma: {round(sum(valores),2)}')
soma_n_termos(10)
