from flask import Flask, jsonify, request, render_template, redirect
import config_db

app = Flask(__name__)

mysql = config_db.configuraConexao(app)

database = dict()
database['USUARIO'] = []
database['PACIENTE'] = []


@app.route("/")
def index():
    print(mysql)
    return 'teste'


@app.route("/login")
def tela_login():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def fazer_login():
    login = request.form

    if 'nusp' in login:
        if len(login['nusp']) < 5:
            return 'Nº USP inválido'
    else:
        return 'informe Nº USP', 404

    if 'senha' in login:
        if len(login['senha']) < 6:
            return 'A senha deve ter no minimo 6 digitos', 404
    else:
        return 'cadastre a senha', 404

    for usuario in database['USUARIO']:
        if login['nusp'] == usuario['nusp'] and login['senha'] == usuario['senha']:
            return 'Usuario encontrado', 200
    return {'erro': 'Usuario não encontrado'}, 404


@app.route("/signin")
def tela_signin():
    return render_template('signin.html')


@app.route("/signin", methods=['POST'])
def fazer_cadastro_usuario():
    dados_usuario = request.values

    if 'email' in dados_usuario:
        if '@' not in dados_usuario['email']:
            return 'Email invalido', 404
    else:
        return 'e-mail não informado', 404

    if 'nome' in dados_usuario:
        if dados_usuario['nome'] == '':
            return 'Nome inválido', 404
    else:
        return 'Nome não informado', 404

    if 'senha' in dados_usuario:
        if len(dados_usuario['senha']) < 6:
            return 'A senha deve ter no minimo 6 digitos', 404
    else:
        return 'cadastre a senha', 404

    if 'nusp' in dados_usuario:
        if len(dados_usuario['nusp']) < 5:
            return 'Nº USP inválido'
    else:
        return 'informe Nº USP', 404
    database['USUARIO'].append(dados_usuario)

    return redirect('login')


@app.route("/pacientes")
def listar_paciente():
    cur = mysql.connection.cursor()
    pacientes = cur.execute("SELECT * FROM pacientes")
    cur.close()
    return jsonify(pacientes)


@app.route("/paciente/novo")
def paciente_novo():
    return render_template('paciente.html')


@app.route("/paciente/novo", methods=['POST'])
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
