""" -------------------------------------------------- inicialização -------------------------------------
 Terminal >> 1_ pip install mysql-connector-python <<<<<< para usar o MySQLl
 Terminal >> 1_ pip install requests <<<< para fazer interface"""
from Connect import Connect
from Create import Create
from Read import Read
from Update import Update
from Delete import Delete

"""--------------------------------------------------- funções -------------------------------------------"""


def duas_func_apagar(mensagens_para_deletar=None, confirme_delecoes=None):  # <<<<< CHAMA 2 FUNÇÕES
    mensagens_para_deletar()
    confirme_delecoes()


def duas_func_edit(mensagens_para_deletar=None, confirme_edicao=None):  # <<<<< CHAMA 2 FUNÇÕES MSGM2DEL E CONFIRM EDIT
    mensagens_para_deletar()
    confirme_edicao()


Connect()

Connect.cursor.close()
Connect.conexao.close()
print("Conexão encerrada com sucesso!!")
'''------------------------------------------------------ Encerrado ------------------------------------------------'''
