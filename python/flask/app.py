from flask import Flask, request, jsonify

app = Flask(__name__)

players = []

@app.route("/")
def show_index():
    return "use other APIs to explore more"

@app.route("/players", methods=['GET', 'POST'])
def get_or_post_player():
    if request.method == 'POST':
        data = request.get_json()
        name = data['name']
        role = data['role']
        id = players[-1]['id'] + 1 if players else 1
        players.append({'id':id,'name':name,'role':role})
    return jsonify(players)

@app.route('/players/<int:id>', methods=['PUT'])
def modify_player_data(id):
    if request.method == 'PUT':
        data = request.get_json()
        res = [i for i in range(len(players)) if players[i]['id']==id]
        idx = res[0] if res else -1
        if idx == -1:
            return "Incorrect ID"
        else:
            players[idx]['name'] = data.get('name', players[idx]['name'])
            players[idx]['role'] = data.get('role', players[idx]['role'])
        return jsonify(players[idx])

if __name__=='__main__':
    app.run(debug=True)