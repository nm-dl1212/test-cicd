from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return jsonify({"message": "hello-world"})

@app.route('/calc')
def calculation():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)

    if a is None or b is None:
        return jsonify({"error": "Parameters 'a' and 'b' are required."}), 400

    multiple_result = a * b
    return jsonify({"message": f"multiple is {multiple_result}"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)