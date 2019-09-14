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
    login = request.form
    for usuario in database['USUARIO']:
        if login['nusp'] == usuario['nusp'] and login['senha'] == usuario['senha']:
            return 'Usuario encontrado', 200
    return {'erro': 'Usuario não encontrado'}, 404


@app.route("/login/cadastro", methods=['POST'])
def fazer_cadastro_usuario():
    dados_usuario = request.form
    if 'email' in dados_usuario:
        if '@' not in dados_usuario['email']:
            return 'Email invalido', 404
    else:
        return 'Email não informado', 404
    return jsonify(dados_usuario)


@app.route("/paciente")
def listar_paciente():
    return jsonify(database['PACIENTE'])


@app.route("/paciente", methods=['POST'])
def fazer_cadastro_paciente():
    dados_paciente = request.values

    if 'nome' not in dados_paciente:
        return {'erro': 'Nome não informado'}, 400

    if len(dados_paciente['nome']) < 6:
        return {'erro': 'Informe o nome completo'}, 400

    if 'sexo' not in dados_paciente:
        return {'erro': 'Sexo não informado'}, 400

    if dados_paciente['sexo'].upper() not in ['M', 'F', 'O']:
        return {'erro': 'Sexo invalido'}, 400

    if 'data_nascimento' not in dados_paciente:
        return {'erro': 'Data de nascimento não informado'}, 400

    if 'cpf' not in dados_paciente:
        return {'erro': 'CPF não informado'}, 400

    if len(dados_paciente['cpf']) < 11:
        return {'erro': 'CPF invalido'}, 400

    # Verificando se o paciente já existe
    for paciente in database['PACIENTE']:
        if paciente['cpf'] == dados_paciente['cpf']:
            return {'erro': 'CPF já existente no cadastro'}, 400

    novo_paciente = {
        'nome': dados_paciente['nome'],
        'sexo': dados_paciente['sexo'].upper(),
        'data_nascimento': dados_paciente['data_nascimento'],
        'cpf': dados_paciente['cpf']
    }
    database['PACIENTE'].append(novo_paciente)

    return 'Paciente cadastrado com sucesso', 201


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)