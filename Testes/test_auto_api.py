"""
===============================================================
Testes Automatizados para a API Gerenciador de Tarefas e Projetos
---------------------------------------------------------------
Este script contém testes automatizados utilizando pytest e requests
para verificar o correto funcionamento das rotas da API.

Testes realizados:
- Listagem, criação, atualização e exclusão de Projetos
- Listagem, criação, atualização e exclusão de Tarefas
- Listagem, criação, atualização e exclusão de Usuários

Dependências:
- pytest (executar testes automatizados)
- requests (realizar requisições HTTP)

Autor: João Pedro Mendes Fonseca
Data de Criação: 22/03/2025
===============================================================
"""

import pytest
import requests

# URL da API
BASE_URL = 'http://127.0.0.1:5000'

# ------------------------------ TESTES ROTA DE PROJETOS ------------------------------

# Testa a listagem de todos os projetos cadastrados na API.
def test_listar_projetos():
    response = requests.get(f'{BASE_URL}/projetos')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Testa a criação de um novo projeto.
def test_criar_projeto():
    projeto = {
        'nome': 'Projeto de Teste',
        'descricao': 'Descrição do projeto de teste',
        'data_inicio': '2023-11-01',
        'data_fim': '2023-12-31'
    }
    response = requests.post(f'{BASE_URL}/projetos', json=projeto)
    assert response.status_code == 201
    assert response.json()['mensagem'] == 'Projeto criado com sucesso!'

# Testa a atualização dos dados de um projeto existente.
def test_atualizar_projeto():
    projeto_atualizado = {
        'nome': 'Projeto Atualizado',
        'descricao': 'Descrição atualizada do projeto',
        'data_inicio': '2023-11-15',
        'data_fim': '2024-01-15'
    }
    response = requests.put(f'{BASE_URL}/projetos/1', json=projeto_atualizado)
    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Projeto atualizado com sucesso!'

# Testa a exclusão de um projeto existente.
def test_excluir_projeto():
    response = requests.delete(f'{BASE_URL}/projetos/1')
    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Projeto excluído com sucesso!'
# --------------------------------------------------------------------------------------

# ------------------------------ TESTES ROTA DE TAREFAS ------------------------------

# Testa listagem de todas as tarefas cadastradas na API.
def test_listar_tarefas():
    response = requests.get(f'{BASE_URL}/tarefas')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Testa a criação de uma nova tarefa
def test_criar_tarefa():
    tarefa = {
        'titulo': 'Tarefa de Teste',
        'descricao': 'Descrição da tarefa de teste',
        'status': 'Em andamento',
        'prioridade': 'Alta',
        'data_vencimento': '2023-11-10',
        'projeto_id': 1,
        'responsavel_id': 1
    }
    response = requests.post(f'{BASE_URL}/tarefas', json=tarefa)
    assert response.status_code == 201
    assert response.json()['mensagem'] == 'Tarefa criada com sucesso!'

# Testa a atualização de uma tarefa já existente.
def test_atualizar_tarefa():
    tarefa_atualizada = {
        'titulo': 'Tarefa Atualizada',
        'descricao': 'Descrição atualizada da tarefa',
        'status': 'Concluída',
        'prioridade': 'Baixa',
        'data_vencimento': '2023-11-15',
        'projeto_id': 1,
        'responsavel_id': 1
    }
    response = requests.put(f'{BASE_URL}/tarefas/1', json=tarefa_atualizada)
    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Tarefa atualizada com sucesso!'

# Testa a exclusão de uma tarefa 
def test_excluir_tarefa():
    response = requests.delete(f'{BASE_URL}/tarefas/1')
    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Tarefa excluída com sucesso!'
# --------------------------------------------------------------------------------------

# ------------------------------ TESTES ROTA DE USUÁRIOS ------------------------------

# Testar a listagem de usuários já cadastrados.  
def test_listar_usuarios():
    response = requests.get(f'{BASE_URL}/usuarios')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Testar a criação de usuários.
def test_criar_usuario():
    usuario = {
        'nome': 'João da Silva',
        'email': '[endereço de e-mail removido]',
        'senha': 'senha123'
    }
    response = requests.post(f'{BASE_URL}/usuarios', json=usuario)
    assert response.status_code == 201
    assert response.json()['mensagem'] == 'Usuário criado com sucesso!'

# Testar a atualização de um usuário. 
def test_atualizar_usuario():
    usuario_atualizado = {
        'nome': 'João Silva',
        'email': '[endereço de e-mail removido]',
        'senha': 'novaSenha'
    }
    response = requests.put(f'{BASE_URL}/usuarios/1', json=usuario_atualizado)
    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Usuário atualizado com sucesso!'

# Testar a exclusão de um usuário.
def test_excluir_usuario():
    response = requests.delete(f'{BASE_URL}/usuarios/1')
    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Usuário excluído com sucesso!'
# --------------------------------------------------------------------------------------