valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

#Calculo do preço final
valor_total_hamburguer= (valorHamburguer * quantidadeHamburguer)
valor_total_bebida = (valorBebida * quantidadeBebida)

preco_total = valor_total_hamburguer + valor_total_bebida

#Troco

troco = valorPago - preco_total

#final

print(f'O preço final do pedido é R$ {preco_total:.2f}. Seu troco é R$ {troco:.2f}.')