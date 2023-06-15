from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    if request.method == 'POST':
        search_query = request.form.get('search')
        entities = ['people', 'planets', 'starships']

        for entity in entities:
            result = requests.get(f'https://swapi.dev/api/{entity}/?search={search_query}').json()
            for item in result['results']:
                if entity == 'people':
                    data.append(f"Персонаж: {item['name']}, Пол: {item['gender']}, Вес: {item['mass']}")
                elif entity == 'planets':
                    data.append(f"Планета: {item['name']}, Диаметр: {item['diameter']}, Население: {item['population']}")
                elif entity == 'starships':
                    data.append(f"Корабль: {item['name']}, Длина: {item['length']}, Экипаж: {item['crew']}")

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
