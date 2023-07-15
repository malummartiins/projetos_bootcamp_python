numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input().strip().lower() == 's'

    if ehVegano:
        tipoVegano = "Vegano"
    else:
        tipoVegano = "Nao-vegano"

    print(f"Pedido {i}: {prato} ({tipoVegano}) - {calorias} calorias")