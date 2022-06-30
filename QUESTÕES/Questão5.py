teclado = str(input("Insira uma frase: ")).lower()
frase = list(teclado)
x = int (len(frase) - 1)
print(f"Você inseriu a frase: {teclado}")
print("Ela ao contrário é: ", end='')
for letra in frase:
    print(frase[x], end='')
    x = x -1