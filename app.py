print("App is starting...")

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h2>Number Analyzer API</h2>

    <p><b>How to use this API:</b></p>

    <p>Send a POST request to:</p>
    <pre>http://127.0.0.1:5000/analyze</pre>

    <p><b>Example Input (JSON):</b></p>
    <pre>
{
  "numbers": [3, -1, 0, 7, -5, 8, -2]
}
    </pre>

    <p><b>Example Output:</b></p>
    <pre>
[3, -8]
    </pre>
    """

@app.route('/analyze', methods=['POST'])
def analyze_numbers():
    data = request.get_json()

    if not data or 'numbers' not in data:
        return jsonify([])

    numbers = data['numbers']

    if not numbers:
        return jsonify([])

    count = 0
    total = 0

    for num in numbers:
        if num > 0:
            count += 1
        elif num < 0:
            total += num

    return jsonify([count, total])

if __name__ == '__main__':
    app.run(debug=True)