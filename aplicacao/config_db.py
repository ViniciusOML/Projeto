from flask_mysqldb import MySQL


def configuraConexao(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'matherick'
    app.config['MYSQL_DB'] = 'ope'

    return MySQL(app)
