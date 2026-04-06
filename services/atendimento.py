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

def registrar_atendimento_com_oficio (
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

        cmd = """
        SELECT * FROM pessoa WHERE id = %s FOR UPDATE
        """

        cursor.execute(cmd, (pessoa_id,))
        cursor.fetchone()

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
        print("Erro, não foi possível salvar alterações.\nErro:", e)

    finally:
        conn.close()

def listar_atendimentos(pessoa_id):
    try:
        conn = connect.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, tipo_violencia, numero_prontuario
            FROM atendimento
            WHERE pessoa_id = %s
        """, (pessoa_id,))

        atendimentos = cursor.fetchall()

        print("=== ATENDIMENTOS ===")
        if not atendimentos:
            print("Nenhum atendimento encontrado.")
        else:
            for a in atendimentos:
                print(f"ID: {a[0]}")
                print(f"Tipo de violência: {a[1]}")
                print(f"Prontuário: {a[2]}")
                print("-" * 30)

        cursor.execute("""
            SELECT id, descricao, orgao_origem
            FROM oficio
            WHERE pessoa_id = %s
        """, (pessoa_id,))

        oficios = cursor.fetchall()

        print("\n=== OFÍCIOS ===")
        if not oficios:
            print("Nenhum ofício encontrado.")
        else:
            for o in oficios:
                print(f"ID: {o[0]}")
                print(f"Descrição: {o[1]}")
                print(f"Órgão de origem: {o[2]}")
                print("-" * 30)

    except Exception as e:
        print("Erro:", e)

    finally:
        cursor.close()
        conn.close()