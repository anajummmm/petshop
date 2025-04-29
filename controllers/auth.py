from flask import Flask, jsonify
from config.jwt_config import generate_token

app = Flask(__name__)

@app.route('/login')
def login():
    token = generate_token()
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(debug=True)
