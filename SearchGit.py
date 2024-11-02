#!/usr/bin/env python3
import requests, sys

def busca_informacoes_github(nomes, token):
    url = f'https://api.github.com/search/users?q={nomes}'


    headers = {
        'Authorization': f'token {token}'
    }

    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            dados = response.json()
            if dados['total_count'] > 0:
                for user in dados['items']:
                    print(f"Perfil: {user['login']}")
                    print(f"Url: {user['html_url']}")
                    print(f"Tipo: {user['type']}")
                    print('-' * 40)
        else:
            print(f'Não foi possível encontrar esse usuário!', response.status_code)
    except Exception as error:
        print('Ocorreu um error', error)

if __name__ == '__main__':
    print('''

 _______                            __       _______  __  __    __            __
|   _   |.-----..---.-..----..----.|  |--.  |   _   ||__||  |_ |  |--..--.--.|  |--.
|   1___||  -__||  _  ||   _||  __||     |  |.  |___||  ||   _||     ||  |  ||  _  |
|____   ||_____||___._||__|  |____||__|__|  |.  |   ||__||____||__|__||_____||_____|
|:  1   |                                   |:  1   |
|::.. . |                                   |::.. . |
`-------'                                   `-------'




''')
    


    if len(sys.argv) != 2:
        print('main <Nome>')
        sys.exit()
    


    url = sys.argv[1]
    token = 'Coloque_seu_token!'
    busca_informacoes_github(url, token)
