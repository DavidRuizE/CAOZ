import requests

# URL base de la API
base_url = 'http://127.0.0.1:8000'  # Cambia esto si tu servidor Flask se está ejecutando en una dirección o puerto diferente

def obtener_clientes():
    """
    Función para obtener la lista de todos los clientes.
    """
    try:
        response = requests.get(f'{base_url}/clientes')
        response.raise_for_status()  # Lanza una excepción en caso de error en la respuesta
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la lista de clientes: {e}")
        return None

def obtener_cliente_por_id(id_cliente):
    """
    Función para obtener información de un cliente específico por su ID.
    """
    try:
        response = requests.get(f'{base_url}/clientes/{id_cliente}')
        response.raise_for_status()  # Lanza una excepción en caso de error en la respuesta
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la información del cliente {id_cliente}: {e}")
        return None

def obtener_producto_de_cliente(id_cliente, id_producto):
    """
    Función para obtener información de un producto específico de un cliente específico.
    """
    try:
        response = requests.get(f'{base_url}/clientes/{id_cliente}/productos/{id_producto}')
        response.raise_for_status()  # Lanza una excepción en caso de error en la respuesta
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la información del producto {id_producto} del cliente {id_cliente}: {e}")
        return None

if __name__ == "__main__":
    # Obtener la lista de todos los clientes
    print("Lista de clientes:")
    clientes = obtener_clientes()
    if clientes:
        for cliente in clientes:
            print(f"Cliente {cliente['id']}: {cliente['nombre_cliente']}")
    
    # Obtener información de un cliente específico (por ejemplo, cliente con id 1)
    print("\nInformación del cliente 1:")
    cliente_1 = obtener_cliente_por_id(1)
    if cliente_1:
        print(cliente_1)
    
    # Obtener información de un producto específico de un cliente específico (por ejemplo, producto con id 101 del cliente 1)
    print("\nInformación del producto 101 del cliente 1:")
    producto_101 = obtener_producto_de_cliente(1, 101)
    if producto_101:
        print(producto_101)
