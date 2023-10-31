from os import system
system('cls')
import requests, json

nome = input('Digite seu nome: ')
dolar = int(input('Digite o valor para conversão: U$ '))
response = requests.get(f'https://economia.awesomeapi.com.br/last/USD-BRL')
#requests = requests.json()

if response.status_code == 200:
    system('cls')

    data = response.json()
    if 'USDBRL' in data:
        cotacao = float(data['USDBRL']['bid'])
        calculo = dolar * cotacao

        print(f'Olá {nome}. Segue as informações do dólar {dolar} informado: \n')
        print(f'Valor: {calculo}')
    else:
        print(f'{dolar} não encontrado')
else:
    print(f'Não foi possível encontrar o valor do dólar {dolar}')