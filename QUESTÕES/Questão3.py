import json
arquivo = [
	'''{
		"dia": 1,
		"valor": 22174.1664
	}''',
	'''{
		"dia": 2,
		"valor": 24537.6698
	}''',
	'''{
		"dia": 3,
		"valor": 26139.6134
	}''',
	'''{
		"dia": 4,
		"valor": 0.0
	}''',
	'''{
		"dia": 5,
		"valor": 0.0
	}''',
	'''{
		"dia": 6,
		"valor": 26742.6612
	}''',
	'''{
		"dia": 7,
		"valor": 0.0
	}''',
	'''{
		"dia": 8,
		"valor": 42889.2258
	}''',
	'''{
		"dia": 9,
		"valor": 46251.174
	}''',
	'''{
		"dia": 10,
		"valor": 11191.4722
	}''',
	'''{
		"dia": 11,
		"valor": 0.0
	}''',
	'''{
		"dia": 12,
		"valor": 0.0
	}''',
	'''{
		"dia": 13,
		"valor": 3847.4823
	}''',
	'''{
		"dia": 14,
		"valor": 373.7838
	}''',
	'''{
		"dia": 15,
		"valor": 2659.7563
	}''',
	'''{
		"dia": 16,
		"valor": 48924.2448
	}''',
	'''{
		"dia": 17,
		"valor": 18419.2614
	}''',
	'''{
		"dia": 18,
		"valor": 0.0
	}''',
	'''{
		"dia": 19,
		"valor": 0.0
	}''',
	'''{
		"dia": 20,
		"valor": 35240.1826
	}''',
	'''{
		"dia": 21,
		"valor": 43829.1667
	}''',
	'''{
		"dia": 22,
		"valor": 18235.6852
	}''',
	'''{
		"dia": 23,
		"valor": 4355.0662
	}''',
	'''{
		"dia": 24,
		"valor": 13327.1025
	}''',
	'''{
		"dia": 25,
		"valor": 0.0
	}''',
	'''{
		"dia": 26,
		"valor": 0.0
	}''',
	'''{
		"dia": 27,
		"valor": 25681.8318
	}''',
	'''{
		"dia": 28,
		"valor": 1718.1221
	}''',
	'''{
		"dia": 29,
		"valor": 13220.495
	}''',
	'''{
		"dia": 30,
		"valor": 8414.61
	}'''
]
day = len(arquivo)
lista = []
for objeto in range(0, day):
    x = arquivo[objeto]
    y = json.loads(x)
    lista.append(y)

print(lista)

quantidade = len(lista)

soma = 0
for d in range(0, quantidade):
    if lista[d]['valor'] != 0.0:
        soma = soma + lista[d]['valor']

menor = 0
maior = 0
diaMenor = 0
diaMaior = 0
media = soma / quantidade
cont = 0

for z in range(0, quantidade):
    if z == 0:
        menor = lista[0]['valor']
        maior = lista[0]['valor']
    if lista[z]['valor'] < menor and lista[z]['valor'] != 0.0:
        menor = lista[z]['valor']
        diaMenor = lista[z]['dia']
    if lista[z]['valor'] > maior:
        maior = lista[z]['valor']
        diaMaior = lista[z]['dia']
    if lista[z]['valor'] > media:
        cont = cont + 1

print(f'O menor faturamento do mês foi de R${menor} no dia {diaMenor}')
print(f'O maior faturamento do mês foi de R${maior} no dia {diaMaior}')
print(f'O faturamento diário foi maior que a média mensal em {cont} dias')