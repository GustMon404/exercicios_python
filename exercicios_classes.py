#4
class Pessoa:
    def __init__(self, nome, idade, peso, altura ) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
            self.idade += 1
    
    def engordar(self):
        pass
    
    def emagrecer(self):
        pass
    
    def crescer(self):
        pass
    
    def __str__(self) -> str:
        return f'Nome: {self.nome} - idade: {self.idade} - peso: {self.peso}kg - altura: {self.altura}cm'
    
pessoa1 = Pessoa('Gustavo', 19,83, 173)

# pessoa1.envelhecer()
# print(pessoa1)
# pessoa1.envelhecer()
# print(pessoa1)


#10
class BombaCombustivel:
    def __init__(self, tipo, valor_litro, quantidade_combustivel) -> None:
        self._tipo = tipo
        self._valor_litro = valor_litro
        self._quantidade_combustivel = quantidade_combustivel
        
    def abastecer_valor(self, valor: float) -> str:
        litro_abastecido = round(valor / self._valor_litro,2)
        self._quantidade_combustivel -= litro_abastecido
        return litro_abastecido
        
    
    def abastecer_litro(self, litro: int) -> float:
        valor_litro_abastecido = litro * self._valor_litro
        self._quantidade_combustivel -= litro
        return valor_litro_abastecido
    
    def alterar_valor(self, preco: float):
        self._valor_litro = preco
    
    def alterar_combustivel(self, tipo: str):
        self._tipo = tipo
    
    def alterarQuantidadeCombustivel(self, qtd: int):
        self._quantidade_combustivel = qtd
        
    def __str__(self) -> str:
        return f'Tipo: {self._tipo} - Valor do litro: R${self._valor_litro} - Quantidade de combustível: {self._quantidade_combustivel}L'
        
bomba1 = BombaCombustivel('gasolina', 2.45, 100)
# print(bomba1)

# print(bomba1.abastecer_litro(10))
# print(bomba1)
# print(bomba1.abastecer_valor(15))
# print(bomba1)
# bomba1.alterar_combustivel('Etanol')
# bomba1.alterar_valor(4)
# bomba1.alterarQuantidadeCombustivel(45)
# print(bomba1)
