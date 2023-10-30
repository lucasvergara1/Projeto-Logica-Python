'''
Escreva um programa que , ao iniciar gera um valor aleatorio de 1 a 10 e permite que o usuario chute um numero ate que o valor aleatorio gerado no inicio do programa seja chutado corretamente

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no inicio do programa.
Lembre de usar os 5Qs do projeto 1.

'''
'''
1.Quais são os dados de entrada necessários?
Gera um valor aleatorio de 1 a 10 após um chute do usuario
2. O que devo fazer com estes dados? 
Devo conseguir comparar o numero chutado pelo usuario e comparar com o numero criado no inicio do programa e dizer se foi acima, abaixo ou igual. 
3. Quais são as restrições deste problema? 
Numero deve ser entre 1 a 10
4. Qual é o resultado esperado? 
Devo conseguir comparar o numero chutado pelo usuario e comparar com o numero criado no inicio do programa e dizer se foi acima, abaixo ou igual. 
5. Qual é a sequencia de passos a ser feitas para chegar ao resultado esperado
input valor aleatorio de 1 a 10
input chute
if valor aleatorio > chute acima 
if valor aleatorio < chute abaixo
else
Print ("Parabéns você acertou o número") 
'''

import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
 valor_chute = int(input("Chute um valor de 1 a 10  "))
 if valor_chute > valor_aleatorio:
  print("Valor do chute acima do valor gerado")
 elif valor_chute < valor_aleatorio:
  print("Valor do chute abaixo do valor gerado")
 elif valor_chute == valor_aleatorio:
  print ("Parabéns você acertou")