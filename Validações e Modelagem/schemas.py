"""
===============================================================
Definição dos Schemas para Validação de Dados
---------------------------------------------------------------
Este módulo define os schemas para validar os dados das requisições 
da API Gerenciador de Tarefas e Projetos.

Schemas:
- ProjetoSchema: Valida os dados dos projetos.
- TarefaSchema: Valida os dados das tarefas.
- UsuarioSchema: Valida os dados dos usuários.

Dependências:
- marshmallow (biblioteca para serialização e validação de dados)

Autor: João Pedro Mendes Fonseca
Data de Criação: 22/03/2025
===============================================================
"""

# Importação da biblioteca marshmallow para validação dos dados
from marshmallow import Schema, fields, validate

# ------------------------------ VALIDAÇÃO DE DADOS DA ROTA PROJETOS -----------------------------
class ProjetoSchema(Schema):
    """
    Schema para validar os dados dos projetos
    """
    # Campo gerado de forma automática pelo banco.
    id = fields.Integer(dump_only=True)

    # Nome vai ser um campo obrigátorio e só vai aceitar valores que possui de 1 até 255 caracteres.
    nome = fields.String(required=True, validate=validate.Length(min=1, max=255))

    # Descrição é opcional e aceita valores do tipo String.
    descricao = fields.String()

    # Data de inicio do projeto aceita valores do tipo Date.
    data_inicio = fields.Date()

    # Data de término aceita valores do tipo Date.
    data_fim = fields.Date()
# -------------------------------------------------------------------------------------------------

# ------------------------------ VALIDAÇÃO DE DADOS DA ROTA TAREFAS ------------------------------
class TarefaSchema(Schema):
    """
    Schema para validar os dados das tarefas.
    """

    # Campo gerado de forma automática pelo banco.
    id = fields.Integer(dump_only=True)

    # Titulo da tarefa é um campo obrigátorio e só vai aceitar valores que possui de 1 até 255 caracteres.
    titulo = fields.String(required=True, validate=validate.Length(min=1, max=255))

    # Descrição detalhada da tarefa é opcional e aceita valores do tipo String.
    descricao = fields.String()

    # Status aceita apenas os valores estabelecidos (Pendente, Em Andamento e Concluida).
    status = fields.String(validate=validate.OneOf(['Pendente', 'Em andamento', 'Concluída']))

    # Prioridade aceita os valores estabelecidos (Baixa, Média e Alta)
    prioridade = fields.String(validate=validate.OneOf(['Baixa', 'Média', 'Alta']))

    # # Data de vencimento da tarefa aceita valores do tipo Date.
    data_vencimento = fields.Date()

    # ID do projeto associado.
    projeto_id = fields.Integer()

    # ID do responsável pela tarefa.
    responsavel_id = fields.Integer()
# ------------------------------------------------------------------------------------------------

# ------------------------------ VALIDAÇÃO DE DADOS DA ROTA USUÁRIOS -----------------------------
class UsuarioSchema(Schema):
    """
    Schema para validar os dados do usuários.
    """

    # Campo gerado de forma automática pelo banco.
    id = fields.Integer(dump_only=True)

    # Nome do usuário é um campo obrigátorio e só vai aceitar valores que possui de 1 até 255 caracteres.    
    nome = fields.String(required=True, validate=validate.Length(min=1, max=255))

    # Email do usuário campo obrigatório, aceita apenas dados em formato de email.
    email = fields.Email(required=True)

    # Senha do usuário é um campo obrigatório e aceita valor de no minimo 6 caracteres.
    senha = fields.String(required=True, validate=validate.Length(min=6))
# ------------------------------------------------------------------------------------------------