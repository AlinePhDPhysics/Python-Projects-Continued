print('***********************')
print('* Jogo de Advinhação *')
print('***********************')
numero_secreto = 50
total_de_tentativas = 3
for rodada in range(1, total_de_tentativas + 1):         
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite o seu número: '))
    print('Você digitou:',chute )
    if chute == 50:
        print('Você acertou! ')
        break
    elif chute > numero_secreto:
        print('Você errou! O seu chute foi maior que o número secreto! ')
    elif chute < numero_secreto:
         print('Você errou! O seu chute foi menor que o número secreto! ')
print ('Jogar de novo? ')