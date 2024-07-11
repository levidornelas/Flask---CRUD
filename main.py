from flask import Flask, url_for, render_template

#Inicializando o flask:
app = Flask(__name__)

#Rota principal:
@app.route('/')
def home():
  titulo = 'Gestão de Produtos'
  produtos = [{'nome': 'Sabão', 'disponivel': True},
              {'nome': 'Carteira', 'disponivel': False},
              {'nome': 'Colar', 'disponvel': False}
            ]
  
  return render_template('index.html', titulo = titulo, produtos = produtos)

#Rota secundária 'sobre':
@app.route('/sobre')
def sobre():
  return """
        <b> Esse é o meu site parceiros </b> <br>
        <a href ="https://www.instagram.com/lev_dorn/"> Meu instagram </a>
          """

#Rodando o flask:
app.run(debug=True)