from flask import Flask, jsonify

app = Flask(__name__)

trainingen = [
    {"id": 1, "naam": "Python", "prijs": 49, "maanden": 3},
    {"id": 2, "naam": "Linux", "prijs": 39, "maanden": 2},
    {"id": 3, "naam": "Cloud", "prijs": 59, "maanden": 4}
]


@app.route("/")
def home():
    return "Welkom bij mijn eerste Flask API!"


@app.route("/api/status")
def status():
    return jsonify({
        "status": "online",
        "message": "Mijn eerste API endpoint werkt!"
    })


@app.route("/api/trainingen")
def toon_trainingen():
    return jsonify(trainingen)


@app.route("/api/trainingen/<int:training_id>")
def toon_training(training_id):
    for training in trainingen:
        if training["id"] == training_id:
            return jsonify(training)

    return jsonify({
        "error": "Training niet gevonden"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)