#19
def tabular_resultados():
    sistemas = ['Windows_server', 'Unix', 'linux','Netware','MacOS','Outro']
    todos_votos = []
    while True:
        voto = int(input('Vote: '))
        if voto == 0:
            break
        elif voto > 6 or voto < 0:
            print('Valor errado')
            continue
        else:
            todos_votos.append(voto)

    qtd_total = len(todos_votos)
    print(qtd_total)
        
    print("{:<30} {:<10} {:<10}".format('Sistemas Operacionais', 'Votos','%'))
    print("{:<30} {:<10} {:<10}".format('-' * 28, '-' * 10,'-' * 10))
    for i in range(len(sistemas)):
        qtd_votos = todos_votos.count(i+1)
        print("{:<30} {:<10} {:<10}".format(sistemas[i], qtd_votos, round((qtd_votos/qtd_total) *100,2)))
    print("{:<30} {:<10}".format('-' * 28, '-' * 10))
    print("{:<30} {:<10}".format('Total', qtd_total))
    

tabular_resultados()

#21
def km_carros():
    carros = ['Gol','Corsa','Voyage','Vectra','Fusca']
    km_litros = [10, 15, 9, 9, 10]
    
    melhor_custo = 0
    for i in range(len(carros)):
        melhor_custo = km_litros[i] if (km_litros[i]>melhor_custo) else melhor_custo
        lit_1000 = 1000/km_litros[i]
        print("{:<15} {:<10} {:<10} litros - R${}".format(carros[i], km_litros[i], round(lit_1000,1), round(lit_1000*2.25, 2)))
    
    print("O menor consumo é do: {}".format(carros[km_litros.index(melhor_custo)]))
    
#km_carros()