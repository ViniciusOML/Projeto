from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

database = dict()
database['USUARIO'] = {}
database['PACIENTE'] = {}

@app.route("/")
def index(): 
    return 'Hello World'


@app.route("/login", methods=['POST'])
def fazer_login():
    return 'Hello World usuario'


@app.route("/login/cadastro", methods=['POST'])
def fazer_cadastro_usuario():
    dados_usuario = request.form
    if 'email' in dados_usuario:
        if '@' not in dados_usuario['email']:
            return 'Email invalido', 404
    else:
        return 'Email não informado', 404
    return jsonify(dados_usuario)


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)