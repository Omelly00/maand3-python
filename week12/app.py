from flask import Flask, render_template, jsonify

app = Flask(__name__)

trainingen = [
    {"id": 1, "naam": "Python", "prijs": 49, "maanden": 3},
    {"id": 2, "naam": "Linux", "prijs": 39, "maanden": 2},
    {"id": 3, "naam": "Cloud", "prijs": 59, "maanden": 4},
    {"id": 4, "naam": "Data Analyse", "prijs": 69, "maanden": 3}
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/trainingen")
def geef_trainingen():
    return jsonify(trainingen)


@app.route("/api/totaal")
def geef_totaal():
    totaal = 0

    for training in trainingen:
        subtotaal = training["prijs"] * training["maanden"]
        totaal = totaal + subtotaal

    return jsonify({
        "totaal": totaal
    })


if __name__ == "__main__":
    app.run(debug=True)
