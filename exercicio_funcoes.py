import random

#9
def inverter_numero(num : int) -> int:
    num_ivertido = int(str(num)[::-1])
    return num_ivertido

print(inverter_numero(127))

#12
def embaralha_palavra(palavra: str) -> str:
    listpalavra = list(palavra)
    random.shuffle(listpalavra)
    return ''.join(listpalavra).upper()

print(embaralha_palavra('python'))