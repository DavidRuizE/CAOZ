import requests 

def getProducts():
    url = 'http://35.238.42.183:8000/clientes'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Esto lanzará una excepción si la respuesta no es 200 OK
        clientes = response.json()  # Parsear el contenido JSON de la respuesta
        return clientes
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return None


API_BASE_URL = 'http://146.148.75.200:8000/api/'

def registerUser(username, password):
    url = f"{API_BASE_URL}register/"
    payload = {
        'username': username,
        'email': email,
        'password': password
    }
    response = requests.post(url, data=payload)
    return response.json()

def loginUser(username, password):
    url = f"{API_BASE_URL}login/"
    payload = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=payload)
    return response.json()

def getNotes(token):
    url = f"{API_BASE_URL}notes/10/"
    headers = {
        'Authorization': f'Token {token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()