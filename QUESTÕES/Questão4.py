SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53
TOTAL = (SP + RJ + MG + ES + OUTROS)
print(TOTAL)

print("--- FATURAMENTO MENSAL ===")
print("Estados disponíveis para consulta: SP, RJ, MG e ES")
print("Digite 1 para visualizar outros estados")
print("Digite 0 para encerrar programa")

while True:
    teclado = str(input('\nInsira a sigla do estado que você deseja consultar: ')).upper()
    if teclado in "SP":
        percentual = (SP * 100) / TOTAL
        print('O pecentual que o estado {} representa no faturamento mensal da empresa é de {:.2f}%' .format(teclado, percentual))
    elif teclado in "RJ":
        percentual = (RJ * 100) / TOTAL
        print('O pecentual que o estado {} representa no faturamento mensal da empresa é de {:.2f}%' .format(teclado, percentual))
    elif teclado in "MG":
        percentual = (MG * 100) / TOTAL
        print('O pecentual que o estado {} representa no faturamento mensal da empresa é de {:.2f}%' .format(teclado, percentual))
    elif teclado in "ES":
        percentual = (ES * 100) / TOTAL
        print('O pecentual que o estado {} representa no faturamento mensal da empresa é de {:.2f}%' .format(teclado, percentual))
    elif teclado in "1":
        percentual = (OUTROS * 100) / TOTAL
        print('O pecentual que outros estados representam no faturamento mensal da empresa é de {:.2f}%'.format(percentual))
    elif teclado in "0":
        print("Programa encerrado!")
        break
    else:
        print("Valor inserido não é válido! Tente novamente!")
