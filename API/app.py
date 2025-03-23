"""
========================================================================
API GERENCIADOR DE TAREFAS E PROJETOS
------------------------------------------------------------------------
Este arquivo contém a implementação da API para gerenciamento de projetos,
tarefas e usuários utilizando o framework Flask.

Funcionalidades:
    - CRUD para Projetos, Tarefas e Usuários.
    - Validação de dados.
    - Manipulação de Banco de Dados
    - Tratamento de Erros.
    - Acompanhamento de ações com logging

Autor: João Pedro Mendes Fonseca
Data de Criação: 22/03/2025
========================================================================
"""

from flask import Flask, jsonify, request
import sqlite3
from schemas import ProjetoSchema, TarefaSchema, UsuarioSchema
from marshmallow import ValidationError
import logging

# Criação e Configuração do logging para registrar os erros que ocorrem em um arquivo de log denominado como "api.log"
logging.basicConfig(filename='api.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Inicializa a aplicação Flask
app = Flask(__name__)

# Função para realizar a conexão com banco de dados.
def get_db_connection():
    """
    Estabelece uma conexão com o banco de dados SQLite.
    Retorna um objeto de conexão.
    Permitindo acessar as colunas por nome.
    """
    conn = sqlite3.connect('database.db')
    # Permitindo acessar as colunas por nome.
    conn.row_factory = sqlite3.Row
    return conn

# ------------------------------ ROTAS PARA PROJETOS ------------------------------

# Função para listar todos os projetos que temos armazenados no banco.
@app.route('/projetos', methods=['GET'])
def listar_projetos():
    """
    Recupera todos os projetos do banco de dados.
    Retorna uma lista contendo os dados dos projetos.
    """
    # Cursor para realizar a conexão.
    conn = get_db_connection()
    # Comando SQL para capturar todos os projetos na base.
    projetos = conn.execute('SELECT * FROM TB_PROJETOS').fetchall()
    # Fechar conexão.
    conn.close()
    # Retorna a lista com todos os projetos
    return jsonify([dict(projeto) for projeto in projetos])

# Função para realizar a criação de um projeto novo na base.
@app.route('/projetos', methods=['POST'])
def criar_projeto():
    """
    Cria um novo projeto a partir dos dados enviados na requisição.
    Realiza uma validação dos dados antes de inseri-los no banco.
    """
    # Instancio o validador ProjetoSchema e valido a requisição.
    schema = ProjetoSchema()
    try:
        dados = schema.load(request.get_json())
    except ValidationError as err:
        logging.error(f'Erro de validação: {err.messages}')
        return jsonify(err.messages), 400
    except sqlite3.Error as err:
        logging.error(f'Erro de Banco de Dados: {err}')
        return jsonify({'mensagem': 'Erro interno do servidor'}), 500
    
    # Insere o projeto no banco de dados.
    conn = get_db_connection()
    conn.execute('INSERT INTO TB_PROJETOS (nome, descricao, data_inicio, data_fim) VALUES (?, ?, ?, ?)', (dados['nome'], dados['descricao'], dados['data_inicio'], dados['data_fim'])) 
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Projeto criado com sucesso!'}), 201

# Função para atualizar um projeto que já está armazenado.
@app.route('/projetos/<int:id>', methods=['PUT'])
def atualizar_projeto(id):
    """
    Atualiza os detalhes de um projeto existente identicado pelo ID.
    """
    # Instancio o validador ProjetoSchema e valido a requisição.
    schema = ProjetoSchema()
    try:
        dados = schema.load(request.get_json())
    except ValidationError as err:
        logging.error(f'Erro de validação: {err.messages}')
        return jsonify(err.messages), 400
    except sqlite3.Error as err:
        logging.error(f'Erro de Banco de Dados: {err}')
        return jsonify({'mensagem': 'Erro interno do servidor'}), 500
    
    # Atualiza os dados no banco
    conn = get_db_connection()
    conn.execute('UPDATE TB_PROJETOS SET nome = ?, descricao = ?, data_inicio = ?, data_fim = ? WHERE id = ?', (dados['nome'], dados['descricao'], dados['data_inicio'], dados['data_fim'], id))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Projeto atualizado com sucesso!'})

# Função para deletar um projeto do banco de dados
@app.route('/projetos/<int:id>', methods=['DELETE'])
def excluir_projeto(id):
    """
    Exclui um projeto do banco de dados com base no ID fornecido.
    """
    # Cursor para realizar a conexão.
    conn = get_db_connection()
    # Comando SQL para deletar o projeto que se encaixa com o ID fornecido.
    conn.execute('DELETE FROM TB_PROJETOS WHERE id = ?', (id,))
    # Realiza a ação.
    conn.commit()
    # Fecha a conexão.
    conn.close()
    # Retorna a confirmação se o projeto foi excluído com sucesso.
    return jsonify({'mensagem': 'Projeto excluído com sucesso!'})
# --------------------------------------------------------------------------------

# ------------------------------ ROTAS PARA TAREFAS ------------------------------

# Função para listar todas tarefas que temos armazenados no banco.
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    """
    Retorna todas as tarefas cadastradas no banco de dados
    """
    # Cursor para realizar a conexão.
    conn = get_db_connection()
    # Comando SQL para capturar todas as tarefas na base.
    tarefas = conn.execute('SELECT * FROM TB_TAREFAS').fetchall()
    # Fechar a conexão
    conn.close()
    # Retorna uma lista com todas as tarefas
    return jsonify([dict(tarefa) for tarefa in tarefas])

# Função para realizar a criação de uma nova tarefa na base.
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    """
    Cria uma nova tarefa a partir dos dados enviados na requisição.
    Realiza uma validação dos dados antes de inseri-las na tabela.
    """
    # Instancia o validador TarefaSchema e valida a requisição.
    schema = TarefaSchema()
    try:
        dados = schema.load(request.get_json())
    except ValidationError as err:
        logging.error(f'Erro de validação: {err.messages}')
        return jsonify(err.messages), 400
    except sqlite3.Error as err:
        logging.error(f'Erro de Banco de Dados: {err}')
        return jsonify({'mensagem': 'Erro interno do servidor'}), 500
    
    # Insere os dados no banco
    conn = get_db_connection()
    conn.execute('INSERT INTO TB_TAREFAS (titulo, descricao, status, prioridade, data_vencimento, projeto_id, responsavel_id) VALUES (?, ?, ?, ?, ?, ?, ?)', (dados['titulo'], dados['descricao'], dados['status'], dados['prioridade'], dados['data_vencimento'], dados['projeto_id'], dados['responsavel_id']))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Tarefa criada com sucesso!'}), 201

# Função para atualizar uma tarefa que já está armazenada.
@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    """
    Atualiza os detalhes de uma tarefa já existente identicado pelo ID.
    """
    # Instancia o validador TarefaSchema e valida a requisição.
    schema = TarefaSchema()
    try:
        dados = schema.load(request.get_json())
    except ValidationError as err:
        logging.error(f'Erro de validação: {err.messages}')
        return jsonify(err.messages), 400
    except sqlite3.Error as err:
        logging.error(f'Erro de Banco de Dados: {err}')
        return jsonify({'mensagem': 'Erro interno do servidor'}), 500
    
    # Atualiza os dados no banco
    conn = get_db_connection()
    conn.execute('UPDATE TB_TAREFAS SET titulo = ?, descricao = ?, status = ?, prioridade = ?, data_vencimento = ?, projeto_id = ?, responsavel_id = ? WHERE id = ?', (dados['titulo'], dados['descricao'], dados['status'], dados['prioridade'], dados['data_vencimento'], dados['projeto_id'], dados['responsavel_id'], id))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Tarefa atualizada com sucesso!'})

# Função para deletar uma tarefa
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    """
    Exclui uma tarefa que está no banco de dados com base no ID fornecido.
    """
    # Cursor para realizar a conexão.
    conn = get_db_connection()
    # Comando SQL para deletar a tarefa que se encaixa com o ID fornecido.
    conn.execute('DELETE FROM TB_TAREFAS WHERE id = ?', (id,))
    # Realiza a ação.
    conn.commit()
    # Fecha a conexão
    conn.close()
    # Retorna a confirmação se a tarefa foi excluída com sucesso.
    return jsonify({'mensagem': 'Tarefa excluída com sucesso!'})
# --------------------------------------------------------------------------------

# ------------------------------ ROTAS PARA USUÁRIOS -----------------------------

# Função para listar todas tarefas que temos armazenados no banco.
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """
    Retorna todas os usuários já cadastradas no banco de dados
    """
    # Cursor para realizar a conexão.
    conn = get_db_connection()
    # Comando SQL para capturar todos os usuários armazenados.
    usuarios = conn.execute('SELECT * FROM TB_USUARIOS').fetchall()
    # Fecha a conexão com o banco.
    conn.close()
    # Retorna uma lista com todos os usuários cadastrados;
    return jsonify([dict(usuario) for usuario in usuarios])

# Função para Criar um novo usuário.
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    """
    Cria um novo usuário a partir dos dados enviados na requisição.
    Realiza uma validação dos dados antes de inseri-los na tabela.
    """
    # Instancia o validador UsuarioSchema e valida a requisição.
    schema = UsuarioSchema()
    try:
        dados = schema.load(request.get_json())
    except ValidationError as err:
        logging.error(f'Erro de validação: {err.messages}')
        return jsonify(err.messages), 400
    except sqlite3.Error as err:
        logging.error(f'Erro de Banco de Dados: {err}')
        return jsonify({'mensagem': 'Erro interno do servidor'}), 500
    
    # Realiza a criação do usuário no banco.
    dados = request.get_json()
    # Cursor para realizar a conexão.
    conn = get_db_connection()
    # Comando SQL para inserir um novo usuário na tabela.
    conn.execute('INSERT INTO TB_USUARIOS (nome, email, senha) VALUES (?, ?, ?)', (dados['nome'], dados['email'], dados['senha']))
    # Realiza a ação.
    conn.commit()
    # Fecha a conexão
    conn.close()
    # Retorna uma mensagem de confirmação falando que o usuário foi cadastrado.
    return jsonify({'mensagem': 'Usuário criado com sucesso!'}), 201

# Função para atualizar um usuário já cadastrado
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    """
    Atualiza os detalhes de um usuário já existente identicado pelo ID.
    """
    # Instancia o validador UsuarioSchema e valida a requisição.
    schema = UsuarioSchema()
    try:
        dados = schema.load(request.get_json())
    except ValidationError as err:
        logging.error(f'Erro de validação: {err.messages}')
        return jsonify(err.messages), 400
    except sqlite3.Error as err:
        logging.error(f'Erro de Banco de Dados: {err}')
        return jsonify({'mensagem': 'Erro interno do servidor'}), 500
    
    # Atualiza os dados do usuário no banco
    dados = request.get_json()
    conn = get_db_connection()
    conn.execute('UPDATE TB_USUARIOS SET nome = ?, email = ?, senha = ? WHERE id = ?', (dados['nome'], dados['email'], dados['senha'], id))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Usuário atualizado com sucesso!'})

# Função para deletar um usuário já armazenado na base
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    """
    Exclui um usuário que está no banco de dados com base no ID fornecido.
    """
    # Cursor para realizar a conexão.
    conn = get_db_connection()
    # Comando SQL para deletar um usuário na base com base em um ID.
    conn.execute('DELETE FROM TB_USUARIOS WHERE id = ?', (id,))
    # Realiza a ação
    conn.commit()
    # Fecha a conexão com o banco
    conn.close()
    # Retorna uma mensagem de confirmação afirmando que a ação foi realizada
    return jsonify({'mensagem': 'Usuário excluído com sucesso!'})
# --------------------------------------------------------------------------------

# ------------------------------ ROTAS DE BOAS - VINDAS --------------------------
"""
Rotas de Boas Vindas
    Desta forma, quando acessado ela retorna um JSON com a mensagem estabelecida
"""
@app.route('/', methods=['GET'])
def boas_vindas():
    return jsonify({'mensagem': 'Bem-vindo à API Gerenciador de Tarefas e Projetos!'})
# --------------------------------------------------------------------------------

"""
Inicia o servidor Flask, permitindo:
    * Atualizações automáticas ao modificar o código

    * Exibição de erros detalhados no navegador.
"""
if __name__ == '__main__':
    app.run(debug=True)