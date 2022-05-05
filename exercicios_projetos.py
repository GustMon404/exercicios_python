import os

#1
def abrir_arquivo() -> list[list]:
    with open('./arquivos/usuario.txt') as usuario_file:
        lista_usuario = usuario_file.read().split('\n')
        lista_usuario_armazenamento = [usuario.split() for usuario in lista_usuario]
        
        usuario_file.close()
        return lista_usuario_armazenamento
        
def byte_para_mega(valor_byte:str) -> float:
    valor_mega = int(valor_byte) / 1048576
    
    return round(valor_mega,2)

# def percentual_uso(uso: str, total: str) -> str:
#     return str(round((uso/total) *100, 2))

def adicionar_percentual(lista: list[list], total: float) -> list[list]:
    for list in lista:
        list.append(round((list[1]/total) * 100, 2))
    return lista

def ordenar_usuario_percentual(lista: list[list]) -> list[list]:
    return sorted(lista, key= lambda lista : lista[2], reverse=True)

def gerar_relatorio(lista: list, espaco_total:float, nome_arquivo: str):
    with open(f'./arquivos/{nome_arquivo}.txt','w') as novo_relatorio:
        novo_relatorio.write('ACME Inc.           Uso do espaço em disco pelos usuários \n')
        novo_relatorio.write('-' * 70 + '\n')
        novo_relatorio.write("{:<5} {:<15} {:<25} {:<15} \n".format('Nr.', 'Usuário', 'Espaço utilizado', r'% do uso'))
        for i in lista:
            novo_relatorio.write("{:<5} {:<15} {:<25} {:<15}\n".format(lista.index(i), i[0], str(i[1]) + ' MB',
                                                                       str(i[2]) + ' %'))
        novo_relatorio.write(f'\nEspaço total ocupado: {espaco_total} MB \n')
        novo_relatorio.write(f'Espaço médio ocupado: {round(espaco_total/len(lista))} MB')
        novo_relatorio.close()
        
        
def gerar_arquivo_inicial() -> None:
    base_path_name = 'C:\\Users'
    
    lista_pasta = os.listdir(base_path_name)
    
    with open('./arquivos/arquivo_inicial.txt', 'w') as arquivo:
        for pasta in lista_pasta:
            arquivo.write("{:<25} {:<15} \n".format(pasta, os.path.getsize(base_path_name + '\\' + pasta)))
        
        arquivo.close()
            
if __name__:
    usuarios_bytes = abrir_arquivo()
    espaco_total = 0
    for user in usuarios_bytes:
        user[1] = byte_para_mega(user[1])
        espaco_total += user[1]
        
    usuarios_bytes = adicionar_percentual(usuarios_bytes, espaco_total)
    gerar_relatorio(usuarios_bytes, espaco_total, 'relatorio_uso')
    
    usuarios_bytes = ordenar_usuario_percentual(usuarios_bytes)
    gerar_relatorio(usuarios_bytes, espaco_total, 'relatorio_uso_ordenado')
    
    n_primeiros = int(input('Quantidade de item a serem visualizados? '))
    gerar_relatorio(usuarios_bytes[:n_primeiros], espaco_total, 'relatorio_uso_ordenado_n_primeiros')
    
    gerar_arquivo_inicial()
    
    
    print('Finish')