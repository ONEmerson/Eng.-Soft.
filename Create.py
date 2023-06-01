"""                                                   CREATE
----------------------------------------------------- CREATE -------------------------------------------"""

from datetime import datetime
import Connect
# teste

class Create:
    def __init__(self, nome_cliente, sala, assento, valor, tipo_entrada, data, hora, novaReservaMsgmLabel=None):
        self.nome_cliente = nome_cliente
        self.sala = sala
        self.assento = assento
        self.valor = valor
        self.tipo_entrada = tipo_entrada
        self.data = data
        self.hora = hora
        self.tipo = self.fazTipo()
        self.data = self.fazData()

        comando = f'INSERT INTO ingresso( nome_cliente,' \
                  f' sala,' \
                  f' assento,' \
                  f' valor,' \
                  f' tipo_entrada,' \
                  f' data,' \
                  f' hora)' \
                  f' VALUES("{self.nome.get()}",' \
                  f' {self.sala.get()},' \
                  f' "{self.assento.get()}",' \
                  f' {self.valor.get()},' \
                  f' "{self.tipo}",' \
                  f'"{self.dataIda}",' \
                  f' "{self.hora}")'

        Connect.cursor.execute(comando)
        Connect.conexao.commit()  ## <<<< quando se edita o banco de dados
        novaReservaMsgmLabel.configure(text=f'\n_______________________________' \
                                            f'\nReserva realizada com sucesso' \
                                            f'\n_______________________________' \
                                            f'\n{"Assento:"} {self.assento.get():>40}' \
                                            f'\n{"Valor:"}{"R$: " + self.valor.get():>40}' \
                                            f'\n{"Nome:"}{self.nome_cliente.get():>40}' \
                                            f'\n{"Sala:"}{self.sala.get():>40}' \
                                            f'\n{"Tipo:"}{self.tipo:>40}' \
                                            f'\n' \
                                            f'\n=========Adcionado=========' \
                                            f'\n Data:__________ {self.dataEscrita.get():<7}' \
                                            f'\nHora:_________ {hora:<7}' \
                                            f'\n===========================')

    def fazTipo(self):
        v = int(self.valor.get())
        if (v > 10):
            self.tipo = "Inteira"
        elif (v == 10):
            self.tipo = "Meia"
        elif (v < 10 and v > 0):
            self.tipo = "Promocional"
        else:
            self.tipo = "Cortesia"

    def fazData(self):
        dataCrua = datetime.now()
        dataIda = f'{dataCrua:%y/%m/%d}'
        dataEscrita = f'{dataCrua:%d/%m/%y}'
        hora = f'{dataCrua:%H:%M:%S}'
        print(f'{dataIda, hora}')


'''------------------------------------------------------- CREATE FIM-------------------------------------------------'''
