from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

database = dict()
database['USUARIO'] = []
database['PACIENTE'] = []

@app.route("/")
def index(): 
    return 'Bem Vindo ao !Iridium'


@app.route("/login", methods=['POST'])
def fazer_login():
    return 'Hello World usuario'


@app.route("/signin", methods=['POST'])
def fazer_cadastro_usuario():
    dados_usuario = request.values
    
    if 'email' in dados_usuario:
        if '@' not in dados_usuario['email']:
            return 'Email invalido', 404
    else:
        return 'e-mail não informado', 404       
    
    if 'nome' in dados_usuario:
        if ' ' in dados_usuario['nome']:
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
   
    return 'Cadastro realizado com sucesso' 

if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)