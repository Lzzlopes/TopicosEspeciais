#  Validação de Entradas: Adicionar validação de entradas para garantir que todos os campos, como o ano e o preço, sejam valores válidos.
#Relatórios: Adicionar a funcionalidade de gerar relatórios em diferentes formatos, como PDF ou HTML, a partir dos
# dados exportados.
from numbers import Real
from pathlib import Path
import os, sqlite3, shutil, csv
from datetime import datetime
import pandas as pd
from sqlalchemy import Integer, String, Float

#caminhos
db = Path('data')
bckp = Path('backups')
exports = Path('exports')

#conexão tabela


def exibir_menu():
    print("=== Livraria ===")
    print("1. Adicionar novo livro")
    print("2. Exibir todos os livros")
    print("3. Atualizar preço de um livro")
    print("4. Remover um livro")
    print("5. Buscar livros por autor")
    print("6. Exportar dados para CSV")
    print("7. Importar dados de CSV")
    print("8. Fazer backup do banco de dados")
    print("9. Sair")


def criar_tabela():
    os.makedirs(db, exist_ok=True)
    conn = sqlite3.connect(db / 'livraria.db')
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS livraria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano_publicacao INTEGER NOT NULL,
                preco REAL NOT NULL
                )
                ''')
    conn.commit()
    return cursor, conn


def backup_tabela():
    os.makedirs(db, exist_ok=True)

    shutil.copyfile(db / 'livraria.db', bckp / f'backup_livraria_{datetime.now().strftime("%Y-%m-%d %H_%M_%S")}.db')


def limpar_backups():
    os.makedirs(bckp, exist_ok=True)
    flag = 0
    arquivos = [arquivo for arquivo in Path('backups').iterdir() if arquivo.is_file()]

    arquivos_ordenados = sorted(arquivos, key=lambda x: x.stat().st_mtime)

    if len(arquivos_ordenados) > 5:
        arquivos_apagar = len(arquivos_ordenados) - 5
        for arquivo in arquivos_ordenados[:arquivos_apagar]:
            os.remove(arquivo)


def menu():
    global db
    while True:
        limpar_backups()
        exibir_menu()
        cursor, conn = criar_tabela()


        opcao = int(input("Digite sua opção: "))
        if opcao == 1:
            #adicionar livro
            backup_tabela()

            titulo = input("Digite o titulo do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = int(input("Digite o ano de publicação: "))
            preco = float(input("Digite o preço do livro: "))
            cursor.execute(''' 
            INSERT INTO livraria(titulo, autor, ano_publicacao, preco) VALUES(? ,? ,? ,?)
            ''', (titulo, autor, ano_publicacao, preco))
            conn.commit()
            conn.close()

        elif opcao == 2:
            #exibir todos os livros
            cursor.execute('''
            select * from livraria''')
            livros = cursor.fetchall()

            if livros:
                print("lista de livros:")
                for livro in livros:
                    print(f"ID: {livro[0]}, titulo: {livro[1]}, Autor: {livro[2]}, ano: {livro[3]}, preco: {livro[4]}")

        elif opcao == 3:
            #atualizar preço de livro
            backup_tabela()

            idprocurado = int(input("Digite o titulo do livro: "))
            preco = float(input("Digite o novo preco do livro: R$"))

            cursor.execute('''
            update livraria
            set preco = ? where id = ?
            ''', (preco, idprocurado))
            conn.commit()
            conn.close()

        elif opcao == 4:
            #remover livro
            backup_tabela()

            livro_procurado = int(input("Digite o id do livro que deseja remover: "))

            cursor.execute('''
            delete from livraria
            where id = ?
            ''', (livro_procurado,))
            conn.commit()

        elif opcao == 5:
            #buscar livros por autor
            nome_autor = input("Digite o nome do autor: ")

            cursor.execute('''
            select * from livraria
            where autor = ?''', (nome_autor,))

            livros = cursor.fetchall()

            if livros:
                print("lista de livros:")
                for livro in livros:
                    print(f"ID: {livro[0]}, titulo: {livro[1]}, Autor: {livro[2]}, ano: {livro[3]}, preco: {livro[4]}")

        elif opcao == 6:
            #exportar dados csv
            os.makedirs(exports, exist_ok=True)
            df = pd.read_sql('select * from livraria', con=conn)
            df.to_csv(exports / 'livros_exportados.csv', index=False)

        elif opcao == 7:
            #importar dados csv
            try:
                nome_arquivo = input("Digite o nome do arquivo: ")
                df = pd.read_csv(exports / f'{nome_arquivo}.csv')
                df.to_sql('livraria', conn, if_exists='replace', index=False)
                print("dados importados com sucesso!")
            except FileNotFoundError:
                print(f"Erro: o arquivo {nome_arquivo}.csv não foi encontrado.")
            except pd.errors.EmptyDataError:
                print("Erro: o arquivo está vazio")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        elif opcao == 8:
            #criando backups
            backup_tabela()

        elif opcao == 9:
            break

    conn.close()


menu()
