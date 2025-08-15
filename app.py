from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # For now, return mock AI response
    result = {
        "prediction": "low_stress",
        "confidence": 0.91
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5001)
