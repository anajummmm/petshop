import jwt
from flask import request, jsonify

SECRET_KEY = 'taylor swift'

def token_required(f):
    def decorated():
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'token nao fornecido!'}), 401
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({'message': 'token invalido!'}), 401
        return f()
    return decorated

def generate_token():
    return jwt.encode({}, SECRET_KEY, algorithm="HS256")

from flask import Flask

app = Flask(__name__)

@app.route('/minha_rota', methods=['GET'])
@token_required
def minha_rota():
    return jsonify({'message': 'Acesso autorizado!'})

if __name__ == '__main__':
    app.run(debug=True)

