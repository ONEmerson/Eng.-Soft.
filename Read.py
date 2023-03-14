"""
                                                          READ
#-------------------------------------------------------- READ ------------------------------------------------------"""
import mysql.connector
import Connect
from Interface import Interface


class Read:
    def __init__(self):
        comando = f'SELECT * FROM ingresso;'
        Connect.cursor.execute(comando)
        resultado = Connect.cursor.fetchall()  # <<<< ler o banco de dados
        print(resultado)
        Interface.exibir(resultado)

    """print("Numero de linhas retornadas: ", cursor.rowcount)
        for resultados in resultado:
            print("cod:", resultados[0])
            print("nome:", resultados[1])
            print("sala:", resultados[2])
            print("assento:", resultados[3])
            print("valor:", resultados[4])
            print("tipo: ", resultados[5])
            print("data:", resultados[6])
            print("hora:", resultados[7])

    --------------------------------------------------- READ FIM -------------------------------------------"""