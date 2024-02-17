from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Automate all the things!",
        "timestamp": 1529729125
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
