print('***********************')
print('* Jogo de Advinhação *')
print('***********************')
numero_secreto = 50
chute = int(input('Digite um número: '))
print('Você digitou:',chute )
if chute == 50:
    print('Você acertou! ')
elif chute > numero_secreto:
    print('Você errou! O seu chute foi maior que o número secreto! ')
elif chute < numero_secreto:
    print('Você errou! O seu chute foi menor que o número secreto! ')
print ('Jogar de novo? ')
