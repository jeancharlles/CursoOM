perguntas = {
    'Pergunta1': {
        'perguntas': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '8'},
        'respostas_certas': 'b',
    },
    'Pergunta2': {
        'perguntas': 'Quanto é 3*2?',
        'respostas': {'a': '1', 'b': '2', 'c': '6'},
        'respostas_certas': 'c',
    },
}
total_acertos = 0
total_perguntas = 0
for pk, pv in perguntas.items():
    total_perguntas += 1
    print(f'\n{pk}: {pv["perguntas"]}')
    for rk, rv in pv["respostas"].items():
        print(f'{rk}: {rv}')

    escolha = input('Escolha uma opção: ')

    if escolha == pv['respostas_certas']:
        print('Você acertou!')
        total_acertos += 1
    else:
        print('Você errou!!')


print(f'Você acertou {total_acertos} respostas de um total de {total_perguntas} perguntas.')
print(f'Sua porcentagem de acerto foi de {total_acertos/total_perguntas * 100}%')
