from flask import Blueprint, render_template, request
from database.cliente import CLIENTES


"""
Rotas para clientes:
- /clientes/ - Listagem de clientes e inserir o cliente no servidor
- /clientes/new - Criação de um novo cliente.
- /clientes/<id> - Obter os dados de um cliente específico
- /clientes/<id>/edit - Formulário para editar clientes
- /clientes/<id>/update - Atualizar dados de um cliente
- /clientes/delete - Deletar informações de um cliente
"""

client_route = Blueprint('cliente', __name__)

@client_route.route('/')
def lista_cliente():
  return render_template('lista_clientes.html', clientes=CLIENTES)

@client_route.route('/', methods = ['POST'])
def inserir_clientes():
  data = request.json

  novo_usuario = {
    'id': len(CLIENTES) + 1,
    "nome": data['nome'],
    "email": data['email']
  }
  CLIENTES.append(novo_usuario)

  return render_template('objeto_cliente.html', cliente = novo_usuario)

@client_route.route('/new')
def form_novo_cliente():
  return render_template('form_clientes.html')

@client_route.route('/<int:cliente_id>')
def cliente_especifico(cliente_id):
  return render_template('cliente_especifico.html')

@client_route.route('/<int:cliente_id>/edit')
def form_atualizar_cliente(cliente_id):
  cliente = None
  for c in CLIENTES:
    if c['id'] == cliente_id:
      cliente = c
  return render_template('form_clientes.html', cliente=cliente)
  
@client_route.route('/<int:cliente_id>/update', methods = ['PUT'])
def atualizar_cliente(cliente_id):
  #Obtendo dados do formulário:
  cliente_editado = None
  data = request.json

  #Obtendo usuário pelo ID
  for c in CLIENTES:
    if c['id'] == cliente_id:
      c['nome'] = data['nome']
      c['email'] = data['email']

      cliente_editado = c

      #Editando o usuário
      return render_template('objeto_cliente.html', cliente = cliente_editado)

@client_route.route('/<int:cliente_id>/delete', methods = ['DELETE'])
def deletar_cliente(cliente_id):
  global CLIENTES
  CLIENTES =[ c for c in CLIENTES if c['id'] != cliente_id]
  return{'deleted': 'ok'}