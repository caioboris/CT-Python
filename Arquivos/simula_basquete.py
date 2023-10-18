import random

times = [
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "LA Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards"
]

def gera_placar():
    ptsA = random.randint(80,130)
    ptsB = random.randint(80,130)
    while ptsA == ptsB:
        ptsB = random.randint(80,130)
    return (ptsA, ptsB)


i = 0
tamanho_array = len(times)
while i < tamanho_array:
    # print(times[i])
    j = i + 1
    while j < tamanho_array:
        pl = gera_placar()
        print(times[i], " X ", times[j])
        pl = gera_placar()
        print(times[j], pl[0] , " X ", pl[1] , times[i])
        j += 1
    i += 1