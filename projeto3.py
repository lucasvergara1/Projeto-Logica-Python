'''
Levando em cosideração a velocidade maxima permitida de 80km em uma determinada rua, crie um programa que recebe do usuario um valor que representa a velocidade e com base nessa velocidade diga se ela tomou uma multa leve, grave ou gravissima. 
Levando em consideração que  se a pessoa estiver abaixo da velocidade maxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade maxima, exiba "levou multa gravissima"

>Aplique os 5Qs

1.Quais são os dados de entrada necessários?
Velocidade do usuario na via
2. O que devo fazer com estes dados? 
Levando em cosideração a velocidade maxima permitida de 80km em uma determinada rua, crie um programa que recebe do usuario um valor que representa a velocidade e com base nessa velocidade diga se ela tomou uma multa leve, grave ou gravissima.
3. Quais são as restrições deste problema? 
Nao ha restrição
4. Qual é o resultado esperado? 
Mostrar mensagens que corresponde ao nivel da multa que a pessoa levou
5. Qual é a sequencia de passos a ser feitas para chegar ao resultado esperado

velocidade_usuario = input("Qual a velocidade do usuario na via?")
velocidade_max_via= 80
if velocidade_usuario <= velocidade_max_via 
 print("Nao levou multa")
elif velocidade_usuario > velocidade_max_via e velocidade_usuario < velocidade_max_via +10
 print("Levou multa")
elif velocidade_usuario > velocidade_max_via e velocidade_usuario > velocidade_max_via +10 e velocidade_usuario <= velocidade_max_via +20
 print ("Levou multa grave")
elif velocidade_usuario > velocidade_max_via e velocidade_usuario > velocidade_max_via +11 e velocidade_usuario >= velocidade_max_via +20
 print ("Levou multa gravissima")



'''

velocidade_usuario = int(input("Qual a velocidade do usuario na via?   - "))
velocidade_max_via= 80


if velocidade_usuario <= velocidade_max_via:
 print ("Nao levou multa")
elif velocidade_usuario > velocidade_max_via and velocidade_usuario <= velocidade_max_via +10:
  print ("Levou multa")
elif velocidade_usuario > velocidade_max_via and velocidade_usuario > velocidade_max_via +10 and velocidade_usuario <= velocidade_max_via +20:
  print ("Levou multa grave")
elif velocidade_usuario > velocidade_max_via and velocidade_usuario > velocidade_max_via +11 and velocidade_usuario >= velocidade_max_via +20:
  print ("Levou multa gravissima")