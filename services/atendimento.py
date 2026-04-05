from db import connect

def criar_atendimento(pessoa_id, tipo_violencia, numero_prontuario):
    try:
        conn = connect.conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO atendimento (pessoa_id, tipo_violencia, numero_prontuario)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (pessoa_id, tipo_violencia, numero_prontuario))
        conn.commit()

        print("Atendimento criado!")

    except Exception as e:
        print("Erro:", e)

    finally:
        conn.close()

def criar_oficio(pessoa_id, descricao, orgao_origem):
    try:
        conn = connect.conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO oficio (pessoa_id, descricao, orgao_origem)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (pessoa_id, descricao, orgao_origem))
        conn.commit()

        print("Ofício criado!")

    except Exception as e:
        print("Erro:", e)

    finally:
        conn.close()


def registrar_atendimento_com_oficio ( #sempre utilize essa função, as outras são auxiliares dessa.
    pessoa_id,
    tipo_violencia,
    numero_prontuario,
    descricao,
    orgao_origem
):
    try:
        conn = connect.conectar()
        cursor = conn.cursor()

        conn.start_transaction()

        cursor.execute(
            "SELECT * FROM pessoa WHERE id = %s FOR UPDATE",
            (pessoa_id,)
        )

        sql_atendimento = """
        INSERT INTO atendimento (pessoa_id, tipo_violencia, numero_prontuario)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql_atendimento, (pessoa_id, tipo_violencia, numero_prontuario))

        sql_oficio = """
        INSERT INTO oficio (pessoa_id, descricao, orgao_origem)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql_oficio, (pessoa_id, descricao, orgao_origem))
        conn.commit()

        print("Atendimento + Ofício registrados com sucesso!")

    except Exception as e:
        conn.rollback()
        print("Erro, não foi possível salvar alteracões, tente novamente mais tarde. \nErro:", e)

    finally:
        conn.close()