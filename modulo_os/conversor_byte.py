
if __name__ == '__main__':
    print(__name__)


def formata_tamanho(tam_arq):
    base = 1000  # ou 1024
    kilo = base
    mega = base**2
    giga = base**3
    tera = base**4
    peta = base**5

    if tam_arq < kilo:
        texto = 'B'

    elif tam_arq < mega:
        tam_arq /= kilo
        texto = 'K'

    elif tam_arq < giga:
        tam_arq /= mega
        texto = 'M'

    elif tam_arq < tera:
        tam_arq /= giga
        texto = 'G'

    elif tam_arq < peta:
        tam_arq /= tera
        texto = 'T'

    else:
        texto = 'Z'

    formatacao = round(tam_arq, 1)
    return f'{formatacao}'.replace('.', ',') + f'{texto}'


