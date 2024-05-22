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