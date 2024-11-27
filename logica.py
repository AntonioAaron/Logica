import uuid

# Diccionario para almacenar URLs
url_map = {}

# Dominio base del acortador
BASE_URL = "http://goshort.ly/"

def generate_short_link():
    """
    Genera un identificador único para la URL corta.
    """
    return uuid.uuid4().hex[:6]

def shorten_url(original_url):
    """
    Acorta una URL y la almacena en el diccionario.
    """
    # Verificar si la URL ya existe en el diccionario
    for short_id, url in url_map.items():
        if url == original_url:
            return BASE_URL + short_id

    # Generar un nuevo identificador corto
    short_id = generate_short_link()
    while short_id in url_map:  # Asegurar unicidad
        short_id = generate_short_link()

    # Almacenar la URL en el diccionario
    url_map[short_id] = original_url
    return BASE_URL + short_id
