import json
from difflib import get_close_matches

# Leitura do arquivo em formato json
data = json.load(open('data.json', 'r'))


def encontra_key(p):
    # p == palavra
    if p.lower() in data:  # Procura por palavras minusculas
        return data[p.lower()]
    elif p.capitalize() in data:  # Procura por palavras com iniciais maiusculas
        return data[p.capitalize()]
    elif p.upper() in data:  # Procura por palavras maiusculas
        return data[p.upper()]
    else:  # Procura por palavras similares
        try:
            # sim == Similar
            sim = get_close_matches(p, data.keys())[0]

        except:
            return [f'Não encontrei a palavra digitada.']  # Se não existe alguma similar, retorna uma lista com erro
        else:
            resp = input(f'Voce queria digitar {sim} ? Y or N: ').upper().strip()[0]  # Mostra a palavra similar na tela
            if resp == 'Y':
                return data[sim]
            elif resp == 'N':
                return [f'Não encontrei a palavra {p}']
            else:
                return [f'Não entendi o que você digitou']


# Programa principal
palavra = input('Pesquise o significado de uma palavra em inglês: ').strip()
if len(palavra) > 0:  # Evita de buscar uma palavra caso o usuario tenha apertado enter
    for m in encontra_key(palavra):
        print(m)
else:
    print('Voçê não digitou nada amigo.')
