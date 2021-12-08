import csv

with open('stonks_bot.csv', 'r') as stonks:
    tabela = csv.reader(stonks)
    for vinho in tabela:    
        print(vinho)