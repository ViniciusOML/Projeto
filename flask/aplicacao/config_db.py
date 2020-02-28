from flask_mysqldb import MySQL


def configuraConexao(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'deivid'
    app.config['MYSQL_PASSWORD'] = 'deivid'
    app.config['MYSQL_DB'] = 'ope'
    app.config['MYSQL CURSORCLASS'] = 'DictCursor'

    return MySQL(app)
