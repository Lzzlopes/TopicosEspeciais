# Aplicativo de Lista de Tarefas

Desenvolvido com Django

## Descrição do Projeto

Este projeto é uma aplicação web desenvolvida com Django, projetada para gerenciar tarefas de forma eficiente. Ele oferece funcionalidades essenciais para a criação, edição, exclusão e atribuição de tarefas, além de permitir o acompanhamento do status das tarefas (pendente, em andamento e concluída).

## Funcionalidades

### Cadastro e Autenticação de Usuários

- **Registro de Novos Usuários**: Permite a criação de contas de novos usuários.
- **Login e Logout**: Gerencia sessões para garantir acesso seguro às tarefas pessoais de cada usuário.
- **Gerenciamento de Sessões**: Cada usuário pode acessar e gerenciar suas próprias tarefas.

### Gerenciamento de Tarefas

- **Criação de Tarefas**: Usuários podem adicionar novas tarefas com título, descrição e status.
- **Visualização de Tarefas**: Exibe uma lista de todas as tarefas atribuídas ao usuário.
- **Edição de Tarefas**: Permite a modificação das informações de uma tarefa existente.
- **Exclusão de Tarefas**: Usuários podem remover tarefas que não são mais necessárias.
- **Atribuição de Tarefas**: As tarefas podem ser atribuídas a outros usuários, promovendo a colaboração.

### Status das Tarefas

- **Filtragem por Status**: As tarefas podem ser filtradas por status (pendente, em andamento, concluída) para facilitar a organização e o acompanhamento.

### Dashboard

- **Acompanhamento do Grupo**: Painel para visualizar todas as tarefas do grupo, oferecendo uma visão geral das atividades em andamento.

## Desenvolvimento e Tecnologias

A aplicação é desenvolvida utilizando o framework Django para o backend, com SQLite como banco de dados. A autenticação de usuários garante que o acesso às tarefas seja seguro e individual. A interface do usuário é projetada com HTML e CSS, apresentando um design simples e responsivo.

## Dependências

As principais dependências do projeto estão listadas no arquivo `requirements.txt` e incluem:

- Django==4.2
- djangorestframework==3.14.0

## Como Executar

1. **Clone o Repositório**

    ```bash
    git clone https://github.com/SeuUsuario/to-do-list.git
    ```

2. **Execute as Migrações**

    Configure o banco de dados com o seguinte comando:

    ```bash
    python manage.py migrate
    ```

3. **Inicie o Servidor**

    Execute o servidor Django com:

    ```bash
    python manage.py runserver
    ```

4. **Acesse a Aplicação**

    Abra um navegador e vá para [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Contribuidores

Este projeto foi desenvolvido por:

- **Luiz Gabriel Vicentin Lopes**
- **RGM:** 8132637357
