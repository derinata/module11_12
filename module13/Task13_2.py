from flask import Flask, jsonify

app = Flask(__name__)

airport_data = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Location": "London"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Location": "New York"},
    "LFPG": {"Name": "Charles de Gaulle Airport", "Location": "Paris"},
}

@app.route('/airport/<icao>', methods=['GET'])
def get_airport_info(icao):
    icao = icao.upper()
    airport = airport_data.get(icao)

    if airport:
        return jsonify({
            "ICAO": icao,
            "Name": airport["Name"],
            "Location": airport["Location"]
        })
    else:
        return jsonify({
            "error": f"No data found for ICAO code {icao}"
        }), 404

if __name__ == '__main__':
    app.run(debug=True)
