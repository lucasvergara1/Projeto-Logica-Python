'''
#Crie um programa que ao receber um numero imprime o fatorial daquele numero
#Metodo 5Qs para montar algo: Analise criticamente o problema e descubra: 
# (Tente explicar para você mesmo o problema em voz alta e peça mais informações/investigue mas até você compreender completamente o problema.)
1.Quais são os dados de entrada necessários?
2. O que devo fazer com estes dados? 
3. Quais são as restrições deste problema? 
4. Qual é o resultado esperado? 
5. Qual é a sequencia de passos a ser feitas para chegar ao resultado esperado
'''

valor_numero_input = int(input("Digite um número"))
if valor_numero_input >0:
  fatorial = 1
for item in range (1,valor_numero_input +1) :
    fatorial = fatorial * item
print (fatorial)

