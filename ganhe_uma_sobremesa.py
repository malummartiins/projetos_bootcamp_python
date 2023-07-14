import sys

valorPedido = float(sys.stdin.readline())

if valorPedido >= 50.0:
    mensagem = "Parabens, você ganhou uma sobremesa gratis!"
else:
    mensagem = "Que pena, você nao ganhou nenhum brinde especial."

print(mensagem)



"""Python
Todas as entradas e saída dos algoritmos são utilizados o STDIN e STDOUT de cada linguagem, abaixo tem algumas dicas de como utilizar cada STDIN e STDOUT de cada linguagem.
Em Python existe várias formas de implementar o STDIN e STDOUT recomendamos utilizar sys.stdin.readline para o STDIN e o print para o STDOUT.

Exemplo:
import sys
a = int(sys.stdin.readline()) // Lê a linha de entrada
print(a); // Imprime o dado
"""