import requests

api_key = 'c99099d0'


def busca_por_id(id):
    url = f'http://www.omdbapi.com/?apikey={api_key}&i={id}'
    response = requests.get(url)
    return response.json()


def busca_por_nome(nome):
    url = f'http://www.omdbapi.com/?apikey={api_key}&s={nome}'
    response = requests.get(url)
    resposta_dict = response.json()
    return resposta_dict


def busca_qtd_total(dicionario_com_resultado):
    return dicionario_com_resultado['totalResults']


'''
Agora, faça uma função busca_qtd_total que retorna quantos
itens (pode ser filme, jogo, série ou o que for) batem com
uma determinada busca.
'''
def qtd_de_filmes(nome_filme):
    url = f'http://www.omdbapi.com/?apikey={api_key}&s={nome_filme}&type=movie'
    response = requests.get(url)
    filmes = response.json()
    return filmes['totalResults']



'''
Faça uma função busca_qtd_filmes que retorna quantos
filmes batem com uma determinada busca.
'''
def qtd_de_jogos(nome_jogo):
    url = f'http://www.omdbapi.com/?apikey={api_key}&s={nome_jogo}&type=game'
    response = requests.get(url)
    jogos = response.json()
    return jogos['totalResults']


'''
Faça uma função ano_do_filme_por_id que recebe a id de
um filme e retorna o seu ano de lançamento.
'''
def nome_do_filme_por_id(id):
    url = f'http://www.omdbapi.com/?i={id}&apikey={api_key}'
    response = requests.get(url)
    filme = response.json()
    return filme['Title']


'''
Peguemos vários dados de um filme de uma vez.
A ideia é receber uma id e retornar 
um dicionário com diversos dados do filme.
O dicionário deve ter as seguintes chaves:
 * ano
 * nome
 * diretor
 * genero
E os dados devem ser preenchidos baseado nos dados do site.
'''
def dicionario_do_filme_por_id(id):
    dicionario = {}
    filme = busca_por_id(id)
    dicionario['nome'] = filme['Title']
    dicionario['ano'] = filme['Year']
    dicionario['genero'] = filme['Genre']
    dicionario['diretor'] = filme['Director']
    return dicionario


'''
Voltando para a busca...
Faça uma função busca_filmes que, dada uma busca, retorna
os dez primeiros items (filmes, series, jogos ou o que for)
que batem com a busca.

A sua resposta deve ser uma lista, cada filme representado por 
um dicionário. cada dicionario deve conter os campos
'nome' (valor Title da resposta) e 'ano' (valor Year da resposta).
'''
def busca_resultados(nome):
    resultados = []
    url = f'http://www.omdbapi.com/?apikey={api_key}&s={nome}&'
    response = requests.get(url)
    filmesSeriesJogos =  response.json()
    for i in range(len(filmesSeriesJogos['Search'])):
       resultados.append({'nome': filmesSeriesJogos['Search'][i]['Title'],
                          'ano':filmesSeriesJogos['Search'][i]['Year']})
    return resultados


'''
Faça uma função busca_filmes_grande que, dada uma busca, retorna
os VINTE primeiros filmes que batem com a busca.
'''
def busca_filmes_grande(nome):
    primeiros20Filmes = []
    url = f'http://www.omdbapi.com/?apikey={api_key}&s={nome}&type=movie'
    url2 = f'http://www.omdbapi.com/?apikey={api_key}&s={nome}&type=movie&page=2'
    response = requests.get(url)
    responsePage2 = requests.get(url2)
    page1 = response.json()
    page2 = responsePage2.json()
    for i in range(len(page1['Search'])):
        primeiros20Filmes.append(page1['Search'][i]['Title'])
    for i in range(len(page2['Search'])):
        primeiros20Filmes.append(page2['Search'][i]['Title'])
    return primeiros20Filmes
