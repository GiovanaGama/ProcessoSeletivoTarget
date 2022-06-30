teclado = int(input("Insira um número: "))
v1 = 0
v2 = 1
resposta = ""
print("0  1  ", end='')
while teclado >= v2:
    v3 = v1 + v2
    print(f"{v3}  ", end='')
    if v2 == teclado and v3 > teclado:
        resposta = "\nO número que você inseriu ESTÁ na sequência de Fibonacci."
    else:
        resposta = "\nO número que você inseriu NÃO ESTÁ na sequência de Fibonacci."
    v1 = v2
    v2 = v3

print(resposta)