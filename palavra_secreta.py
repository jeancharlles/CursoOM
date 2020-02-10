secreto = 'perfume'
digitadas = list()
chances = 3

while True:
    if chances == 0:
        print('Voce Perdeu!')
        break

    letra = input('Digite uma letra:')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUL,  a letra {letra} existe na palavra secreta')
    else:
        print(f'Aff, a letra {letra} não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:  # Aqui está o pulo do gato

        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    # print(secreto_temporario)

    if secreto_temporario == secreto:
        print(f'Parabéns a palavra secreta era {secreto_temporario}.\n Você conseguiu!')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você tem {chances} chances\n')
