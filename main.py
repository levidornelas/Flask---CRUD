from flask import Flask, url_for, render_template
from routes.home import home_route
from routes.clientes import client_route

#Inicializando o flask:
app = Flask(__name__)

#Rota principal:
app.register_blueprint(home_route)

#Rota dos clientes:
app.register_blueprint(client_route, url_prefix='/clientes')



#Rodando o flask:
app.run(debug=True)