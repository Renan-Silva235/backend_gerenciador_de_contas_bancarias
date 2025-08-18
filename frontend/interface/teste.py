num = 10

palpite = int(input('digite um número: '))
              


while palpite != num:
    print('você errou o palpite')

    if palpite > num:
        falta = palpite - num
        print(f'Seu palpite está {falta} acima do palpite correto')
    
    elif palpite < num:
        falta = num - palpite
        print(f'Seu palpite está {falta} abaixo do palpite correto')


    palpite = int(input('Digite um número: '))

else:

    print('Você acertou o palpite')
    