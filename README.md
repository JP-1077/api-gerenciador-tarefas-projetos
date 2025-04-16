# API de Gerenciador de Tarefas e Projetos 🔍

## Introdução 
Esta é uma API Restful desenvolvida com Python e framework Flask, com o objetivo de fornecer uma solução simples e eficiente para o gerenciamento de projetos, tarefas e usuários. Ideal para equipes que desejam organizar seu fluxo de trabalho de forma prática e centralizada.

---

## ✍🏼 System Design

### 1.Arquitetura da Aplicação

* **Padrão Arquitetural:** MVC (Model - View - Controller) com separação de responsabilidades.

* **Framework:** Flask

* **Banco de Dados:** SQLite

### 2. Diagrama de Entidade - Relacionamento (ERD)

![Diagrama do Banco de Dados](Diagrama%20Banco%20de%20Dados.png)

### 3. Fluxo de Requisições

![Diagrama do Banco de Dados](Fluxo%20de%20Requisições.png)

* **Explicação:**

1. O cliente envia uma requisição HTTP para o endpoint (ex: POST /tasks).

2. A rota correspondente chama um controller.

3. O controller aplica regras de negócio e chama os models.

4. Os models interagem com o banco via SQLAlchemy.

5. A resposta é retornada em JSON.

### 4. Tecnologias Utilizadas

* **Flask:** Framework principal da API.

* **Flask-RESTful:** Extensão para criação de APIs REST.

* **Flask-SQLAlchemy:** ORM para manipulação do banco de dados.

* **Flask-Migrate (se usar):** Controle de versionamento do banco.

---

## 🧰 Endpoints Principais

| Método | Rota           | Descrição                    |
|--------|----------------|------------------------------|
| GET    | /projects      | Lista todos os projetos      |
| POST   | /projects      | Cria um novo projeto         |
| GET    | /tasks         | Lista todas as tarefas       |
| POST   | /tasks         | Cria uma nova tarefa         |
| PUT    | /tasks/<id>    | Atualiza uma tarefa específica |
| DELETE | /tasks/<id>    | Remove uma tarefa específica |
| GET    | /users         | Lista todos os usuários      |
| POST   | /users         | Cria um novo usuário         |

