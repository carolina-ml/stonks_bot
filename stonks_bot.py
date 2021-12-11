import csv

lista_de_acoes = []

with open('stonks_bot.csv', 'r') as stonks:
    tabela = csv.DictReader(stonks)
    for linha in tabela:
        if linha['INVESTIMENTOS']=='RICO':    
            lista_de_acoes.append(linha['renda variável'])
print(lista_de_acoes)            