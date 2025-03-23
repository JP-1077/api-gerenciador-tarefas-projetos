"""
===============================================================
Criação do Banco de Dados
---------------------------------------------------------------
Este script cria e inicializa o banco de dados SQLite para a API
Gerenciador de Tarefas e Projetos. Ele define as tabelas necessárias
para armazenar informações sobre projetos, tarefas e usuários.

Tabelas Criadas:
- TB_PROJETOS: Armazena os projetos
- TB_TAREFAS: Armazena as tarefas associadas aos projetos e usuários
- TB_USUARIOS: Armazena informações dos usuários

Dependências:
- sqlite3 (biblioteca nativa do Python)

Autor: João Pedro Mendes Fonseca
Data de Criação: 22/03/2025
===============================================================
"""

# Importa a biblioteca SQLite para manipulação do banco de dados.
import sqlite3

# Conecta ao banco de dados e cria um arquivo database.db.
banco = sqlite3.connect("database.db")

# Cria um cursor para executar comandos em SQL.
cursor = banco.cursor()

# ------------------------------ CRIAÇÃO TABELA PROJETOS -----------------------------

cursor.execute("""
    CREATE TABLE TB_PROJETOS (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        nome VARCHAR(255) NOT NULL,
        descricao TEXT,
        data_inicio DATE,
        data_fim DATE
    );
""")
# -----------------------------------------------------------------------------------

# ------------------------------ CRIAÇÃO TABELA TAREFAS -----------------------------
cursor.execute("""
    CREATE TABLE TB_TAREFAS (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        titulo VARCHAR(255) NOT NULL,
        descricao TEXT,
        status VARCHAR(50) DEFAULT 'Pendente',
        prioridade VARCHAR(50) DEFAULT 'Média',
        data_vencimento DATE,
        projeto_id INTEGER,
        responsavel_id INTEGER,
        FOREIGN KEY (projeto_id) REFERENCES TB_PROJETOS(id),
        FOREIGN KEY (responsavel_id) REFERENCES TB_USUARIOS(id)
    );
""")
# -----------------------------------------------------------------------------------

# ------------------------------ CRIAÇÃO TABELA USUÁRIOS -----------------------------
cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_USUARIOS (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        senha VARCHAR(255) NOT NULL
    );
""")
# ------------------------------------------------------------------------------------

# Realiza as mudanças
banco.commit()

# Fecha a conexão com o banco de dados
banco.close()

# Mensagem de Confirmação
print("✅ Banco de dados e tabelas criadas com sucesso!")