from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [
    {
        "id":1,
        "titulo": "Rumo a Goiania",
        "artista": "Leonardo"
    },
    {
        "id":2,
        "titulo": "É o amor",
        "artista": "Zezé di Camargo e Luciano"
    }
]

@app.route('/playlist', methods=['GET'])
def get_musicas():
    return jsonify({"playlist":playlist, "total": len(playlist)})


if __name__  == '__main__':
    app.run(debug=True)