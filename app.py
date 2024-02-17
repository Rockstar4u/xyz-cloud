from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Automate all the things!",
        "timestamp": 1529729125  # Hardcoded timestamp for demonstration
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
