from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Machine Learning Application is Running!",
        "status": "Success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)