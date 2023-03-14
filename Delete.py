""" DELETE
--------------------------------------------------------- DELETE -------------------------------------------------"""


class Delete:
    def __init__(self):
            match txt:
                case 'Código':  # Código
                    cod = int(Descricao.get())
                    comando = f'DELETE FROM ingresso WHERE cod = {cod}'
                    cursor.execute(comando)
                    conexao.commit()  # <<< editar o banco de dados
                    msgmConfirm.configure(text=f'Reservas de {txt}: ({cod})\n apagada com sucesso!')
                    return 0
                case "Nome":  # Nome
                    comando = f'DELETE FROM ingresso WHERE nome_cliente = "{Descricao.get()}" AND sala="{DescricaoParaSala.get()}" AND assento="{DescricaoParaAssento.get()}"'
                    cursor.execute(comando)
                    conexao.commit()  # <<< editar o banco de dados
                    msgmConfirm.configure(
                        text=f'Reservas de: ( Nome {Descricao.get()}, Sala {DescricaoParaSala.get()}, Assento {DescricaoParaAssento.get()})\n apagada com sucesso!')
                    return 0
                case "Assento":  # Assento
                    comando = f'DELETE FROM ingresso WHERE assento = "{Descricao.get()}" AND sala = "{DescricaoParaSala.get()}"'
                    cursor.execute(comando)
                    conexao.commit()  # <<< editar o banco de dados
                    msgmConfirm.configure(
                        text=f'Reservas de {txt} {Descricao.get()}: ( Sala {DescricaoParaSala.get()} )\n apagada com sucesso!')
                    return 0
                case "Sala":  # Sala
                    comando = f'DELETE FROM ingresso WHERE sala = "{Descricao.get()}" AND assento = "{DescricaoParaAssento.get()}"'
                    cursor.execute(comando)
                    conexao.commit()  # <<< editar o banco de dados
                    msgmConfirm.configure(
                        text=f'Reserva de {txt} {Descricao.get()}: ( Assento {DescricaoParaAssento.get()} ) apagada com sucesso!')
                case _:
                    msgmConfirm["text"] = f'Opção ({txt}) não é válida.\nPor favor confira a escolha e tente novamente.'
                    return 0

        ##--------------------------------------------------- DELETE FIM -------------------------------------------
