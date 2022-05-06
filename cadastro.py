from ast import Str
from crypt import methods
import re
from flask import Flask,jsonify,abort, render_template
from flask import make_response, request, url_for
from flaskext.mysql import MySQL


app = Flask(__name__)
#app.url_map.strict_slashes = False


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass02345'
app.config['MYSQL_DATABASE_DB'] = 'ac2_fmk'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


@app.route('/cadastrar', methods=["GET","POST"])
def cadastrar():
    _nome = request.form['nom']
    _categoria = request.form['categoria']
    _preco = request.form['preco']
    if _name and _email and _endereco:
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "INSERT INTO tbl_alunos(nome, categoria, preco) VALUES (%s, %s, %s)"
        value = (_nome, _categoria, _preco)
        cursor.execute(sql, value)
        conn.commit()

    
 
    return render_template('index.html')

@app.route('/listar', methods=['GET'])
def listar():
    data = []
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = 'SELECT nome, categoria, preco FROM tbl_produto'
    cursor.execute(sql)
    for usuario in cursor.fetchall():
        data.append(usuario)
    return render_template('listar.html', data=data)



if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)