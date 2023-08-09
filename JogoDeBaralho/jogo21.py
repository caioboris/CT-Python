import baralho

def imprime(mao):
    info = ""
    for c in mao:
        info = info + str(c[0])+ " " + c[1]
    print(info)

def pontos(mao):
    valor = 0 
    for c in mao:
        if c[0] > 10:
            valor = valor +10
        else:
            valor = valor + c[0]
    return valor

def quer_carta(mao:list):
    imprime(mao)
    print('Pontos: ', pontos(mao))
    escolha = input('Quer carta (s/n)?')
    if(escolha == 's'):
        return True
    else:
        return False

deck = baralho.cria()

baralho.embaralha(deck)

mao_jog = baralho.distribui(deck,2)
mao_cpu = baralho.distribui(deck,2)

while quer_carta(mao_jog) == True:
    c = baralho.compra(deck)
    mao_jog.append(c)

while pontos(mao_cpu) > 16:
    c = baralho.compra(deck)
    mao_cpu.append(c)

print('JOGADOR: ')
imprime(mao_jog)
print('Pontos: ', pontos(mao_jog))

print('CPU: ')
imprime(mao_cpu)
print('Pontos: ', pontos(mao_cpu))