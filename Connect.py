import mysql.connector



class Connect:
    def __init__(self):
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='0001',  # <<<<< informações de log. in do Banco de Dados
            database='cine_bd',
        )
        cursor = conexao.cursor()
        print(f"Mensagem do cursor: f'{cursor}'")


print("Conexão com o Banco de Dados realizada com sucesso")
