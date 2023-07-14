import sys

def calcular_valor_total_com_desconto(pedidos, cupom):
    valor_total = sum(pedido[1] for pedido in pedidos)
    if cupom == '10%':
        valor_total *= 0.9
    elif cupom == '20%':
        valor_total *= 0.8
    return valor_total

def main():
    n = int(input())

    pedidos = []

    for i in range(n):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        pedidos.append((nome, valor))

    cupom = input().strip()

    valor_total_com_desconto = calcular_valor_total_com_desconto(pedidos, cupom)

    print(f"Valor total: {valor_total_com_desconto:.2f}")

if __name__ == "__main__":
    main()

"""A entrada é composta por:

Uma linha com um número inteiro n representando a quantidade de pedidos que o usuário deseja inserir;
n linhas, cada uma contendo uma string com o nome do pedido e um valor em ponto flutuante separados por espaço. O nome do pedido não contém espaços em branco;
Uma linha contendo o cupom de desconto escolhido (10% ou 20%).
Saída
O programa deve exibir uma única linha contendo o valor total de todos os pedidos com o desconto aplicado, no seguinte formato:

Valor total: XX.YY, onde "XX.YY" é a soma de todos os pedidos com desconto em formato de duas casas decimais após a vírgula."""