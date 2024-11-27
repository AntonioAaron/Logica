 
from flask import Flask, request, jsonify
import uuid
import logica

app = Flask(__name__)

# Configuración de conexión a la base de datos
def get_db_connection():
    database_url = "postgresql://postgres:IgtzJLbHpqJPoimAEYCVTqkDtQFFPqEz@autorack.proxy.rlwy.net:39767/railway"
    connection = psycopg2.connect(database_url)
    return connection

# Generar un identificador único para la URL
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


@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()  # Obtén los datos JSON de la solicitud
    original_url = data.get('original_url')  # URL original a acortar

    if not original_url:
        return jsonify({"message": "Falta la URL original"}), 400
    
    else:
        url_short = shorten_url(original_url)

    return jsonify({"url_short": url_short})


# Ejecuta la aplicación
if __name__ == "__main__":
    # Run the Flask application on localhost at port 3000
    app.run(host="127.0.0.1", port=3000, debug=True)