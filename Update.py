"""                                                 UPDATE
--------------------------------------------------- UPDATE -------------------------------------------"""
import Create
import Connect
import Interface


class Update:
    def __init__(self):
        match Interface.txt:
            case "Código":  # Código
                Create.fazTipo()
                Create.fazData()
                comando = f'UPDATE ingresso SET' \
                          f' cod = "{codigo.get()}",' \
                          f' nome_cliente = "{nome.get()}",' \
                          f' sala = "{sala.get()}",' \
                          f' valor = "{valor.get()}",' \
                          f'tipo_entrada = "{tipo}",' \
                          f' assento = "{assento.get()}",' \
                          f' data = "{Create.dataIda}",' \
                          f' hora = "{Create.hora}"' \
                          f' WHERE cod = "{int(Descricao.get())}"'
                set.Connect.cursor.execute(comando)
                set.Connect.conexao.commit()  ##  <<<< editar o banco de dados

                novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                                    f'\n\nAssento: {assento.get()}' \
                                                    f'\nValor: R${valor.get()}' \
                                                    f'\nNome: {nome.get()}' \
                                                    f'\nSala: {sala.get()}' \
                                                    f'\nTipo: {tipo}' \
                                                    f'\n\n=======Adcionado=======' \
                                                    f'\nData:{Create.dataEscrita}' \
                                                    f'\nHora:{Create.hora}' \
                                                    f'\n=======================')
                return 0

            case "Nome":  # Nome

                Create.fazTipo()
                Create.fazData()

                comando = f'UPDATE ingresso SET' \
                          f' cod = "{codigo.get()}",' \
                          f' nome_cliente = "{nome.get()}",' \
                          f' sala = "{sala.get()}",' \
                          f' valor = "{valor.get()}",' \
                          f'tipo_entrada = "{tipo}",' \
                          f' assento = "{assento.get()}",' \
                          f' data = "{Create.dataIda}",' \
                          f' hora = "{Create.hora}"' \
                          f' WHERE nome_cliente = "{Descricao.get()}" AND assento = "{DescricaoParaSala.get()}" AND sala = "{DescricaoParaAssento.get()}"'
                print(comando)
                cursor.execute(comando)
                conexao.commit()  ##  <<<< editar o banco de dados

                novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                                    f'\n\nAssento: {assento.get()}' \
                                                    f'\nValor: R${valor.get()}' \
                                                    f'\nNome: {nome.get()}' \
                                                    f'\nSala: {sala.get()}' \
                                                    f'\nTipo: {tipo}' \
                                                    f'\n\n=======Adcionado=======' \
                                                    f'\nData:{Create.dataEscrita}' \
                                                    f'\nHora:{Create.hora}' \
                                                    f'\n=======================')
                return 0

            case "Sala":  # Sala

                Create.fazTipo()
                Create.fazData()

                comando = f'UPDATE ingresso SET' \
                          f' cod = "{codigo.get()}",' \
                          f' nome_cliente = "{nome.get()}",' \
                          f' sala = "{sala.get()}",' \
                          f' valor = "{valor.get()}",' \
                          f' tipo_entrada = "{tipo}",' \
                          f' assento = "{assento.get()}",' \
                          f' data = "{Create.dataIda}",' \
                          f' hora = "{Create.hora}"' \
                          f' WHERE sala = "{Descricao.get()}" AND assento = "{DescricaoParaAssento.get()}"'
                print(comando)
                cursor.execute(comando)
                conexao.commit()  ##  <<<< editar o banco de dados

                novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                                    f'\n\nAssento: {assento.get()}' \
                                                    f'\nValor: R${valor.get()}' \
                                                    f'\nNome: {nome.get()}' \
                                                    f'\nSala: {sala.get()}' \
                                                    f'\nTipo: {tipo}' \
                                                    f'\n\n=======Adcionado=======' \
                                                    f'\nData:{Create.dataEscrita}' \
                                                    f'\nHora:{Create.hora}' \
                                                    f'\n=======================')
                return 0

            case "Assento":  # Assento

                Create.fazTipo()
                Create.fazData()

                comando = f'UPDATE ingresso SET' \
                          f' cod = "{codigo.get()}",' \
                          f' nome_cliente = "{nome.get()}",' \
                          f' sala = "{sala.get()}",' \
                          f' valor = "{valor.get()}",' \
                          f'tipo_entrada = "{tipo}",' \
                          f' assento = "{assento.get()}",' \
                          f' data = "{Create.dataIda}",' \
                          f' hora = "{Create.hora}"' \
                          f' WHERE assento = "{Descricao.get()}" AND sala = "{DescricaoParaSala.get()}"'
                cursor.execute(comando)
                conexao.commit()  ##  <<<< editar o banco de dados

                novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                                    f'\n\nAssento: {assento.get()}' \
                                                    f'\nValor: R${valor.get()}' \
                                                    f'\nNome: {nome.get()}' \
                                                    f'\nSala: {sala.get()}' \
                                                    f'\nTipo: {tipo}' \
                                                    f'\n\n=======Adcionado=======' \
                                                    f'\nData:{Create.dataEscrita}' \
                                                    f'\nHora:{Create.hora}' \
                                                    f'\n=======================')
                return 0

            case _:
                novaReservaMsgmLabel.configure(
                    text=f'Opção {txt}: --> {Descricao.get()} <--\nnão é válida.\nPor favor confira a escolha \ne' \
                    f'\ntente novamente.')
                return 0

'''--------------------------------------------------- UPDATE FIM -------------------------------------------'''