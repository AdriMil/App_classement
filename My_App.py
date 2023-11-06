from flask import Flask, render_template, jsonify
from DB_Actions import connexion

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/data')
def get_data_as_json():
    formatted_data=[]
    # Supposez que vous avez des données que vous voulez renvoyer sous forme de JSON
    data = connexion()
   
    data_from_db = list(data.find({}))

    for item in data_from_db:
        formatted_item = {
            'nom': item['nom'],
            'victoire': item['victoire'],
            'defaite': item['defaite'],
            'nul': item['nul'],
            'parties': item['parties']
        }
        formatted_data.append(formatted_item)

    print(formatted_data)

    return jsonify({
      'status': 'ok', 
      'data': formatted_data
    }),200

if __name__ == '__main__':
    app.run( port = 5010)
