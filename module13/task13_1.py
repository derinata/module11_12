from flask import Flask, jsonify

app = Flask(__name__)

AIRPORTS = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Location": "London"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Location": "New York"},
    "LFPG": {"Name": "Charles de Gaulle Airport", "Location": "Paris"},
    "OMDB": {"Name": "Dubai International Airport", "Location": "Dubai"},
}

@app.route("/", methods=["GET"])
def root():
    return jsonify({"status": "ok", "hint": "Use /airport/<ICAO> e.g. /airport/EFHK"})

@app.route("/airport/<string:icao>", methods=["GET"])
def get_airport(icao: str):
    icao = icao.upper()  # make case-insensitive
    data = AIRPORTS.get(icao)
    if not data:
        return jsonify({"ICAO": icao, "error": "Airport not found"}), 404
    return jsonify({"ICAO": icao, "Name": data["Name"], "Location": data["Location"]})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
