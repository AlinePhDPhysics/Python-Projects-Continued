print('***********************')
print('* Jogo de Advinhação *')
print('***********************')
numero_secreto = 50
total_de_tentativas = 3
rodada = 1
while total_de_tentativas > 0:
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute_str = int(input('Digite o seu número: '))
    print('Você digitou:',chute_str )
    if chute_str == 50:
        print('Você acertou! ')
        break
    elif chute_str > numero_secreto:
        print('Você errou! O seu chute foi maior que o número secreto! ')
    elif chute_str < numero_secreto:
        print('Você errou! O seu chute foi menor que o número secreto! ')
    rodada = rodada + 1
print ('Jogar de novo? ')