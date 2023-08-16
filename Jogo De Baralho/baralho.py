import random

def cria():
    monte = []
    for x in range(1,14):

        if(x == 1):
            x = 'A'
        if(x == 11): 
            x = 'J'
        if(x == 12):
            x = 'Q'
        if(x == 13):
            x = 'K'
        monte.append((x,'♣'))
        monte.append((x,'♦'))
        monte.append((x,'♥'))
        monte.append((x,'♠'))
         
        

    return monte


def compra(monte: list):
    return monte.pop()


def distribui(monte: list, qtd: int):
    mao = []
    while qtd > 0:
        c = compra(monte)
        mao.append(c)
        qtd = qtd-1
    return mao

def embaralha(monte: list):
    random.shuffle(monte)

deck = cria()
#print(deck)
carta = compra(deck)
