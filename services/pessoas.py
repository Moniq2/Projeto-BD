from db import connect

#olhar nova versao cadastra pessoas
'''
def cadastrar_pessoa(nome, idade, endereco, territorio):
    try:
        conn = connect.conectar()
        cursor = conn.cursor()
        cmd = """INSERT INTO pessoa(nome, idade, endereco, territorio)
        VALUES (%s,%s,%s,%s);
        """
        cursor.execute(cmd, (nome, idade, endereco, territorio))
        conn.commit()

    except Exception as e:
        print("Erro ao acessar o banco")
        print(e)

    finally:
        cursor.close()
        conn.close()
'''
def cadastrar_pessoa(nome, idade, endereco, territorio):
    try:
        conn = connect.conectar()
        cursor = conn.cursor()
        cmd = """INSERT INTO pessoa(nome, idade, endereco, territorio)
        VALUES (%s,%s,%s,%s);
        """
        cursor.execute(cmd, (nome, idade, endereco, territorio))
        conn.commit()
        
        
        return cursor.lastrowid 

    except Exception as e:
        print("Erro ao acessar o banco")
        print(e)
        return None # Caso dê erro
    finally:
        cursor.close()
        conn.close()

def listar_pessoas():
    try:
        conn = connect.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, idade, endereco, territorio
            FROM pessoa
        """)

        usuarios = cursor.fetchall()

        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for u in usuarios:
            print(f"ID: {u[0]}")
            print(f"Nome: {u[1]}")
            print(f"Idade: {u[2]}")
            print(f"Endereço: {u[3]}")
            print(f"Território: {u[4]}")
            print("-" * 30)

    except Exception as e:
        print("Erro:", e)

    finally:
        cursor.close()
        conn.close()


def buscar_pessoa_por_id(pessoa_id):
    try:
        conn = connect.conectar()
        cursor = conn.cursor()

        sql = "SELECT * FROM pessoa WHERE id = %s"
        cursor.execute(sql, (pessoa_id,))

        resultado = cursor.fetchone()

        return resultado  #pode ser None ou uma tupla

    except Exception as e:
        print("Erro:", e)
        return None

    finally:
        conn.close()

def editar_cadastro(id, nome, idade, endereco, territorio): #Devem ser passados o ID do usuário cadastrado e todas as informações, editadas e não editadas                                                        
    try: 
        if buscar_pessoa_por_id(id) == None:
            print("Não foi encontrado nenhum indivíduo cadastrado com esse ID, não foi possível editar o cadastro.") 
            return                                                  
    
        conn = connect.conectar()
        cursor = conn.cursor()
        cmd = """
        UPDATE pessoa
        SET nome = %s, idade = %s, endereco = %s, territorio = %s
        WHERE id = %s;
        """
        cursor.execute(cmd, (nome, idade, endereco, territorio, id))
        conn.commit()
  
    except Exception as e:
        print("Erro ao acessar o banco")
        print(e)

    finally:
        cursor.close()
        conn.close()
        
def exibir_detalhes_pessoa(pessoa_id):
    try:
        # Reutilizamos a função de busca que já tem
        pessoa = buscar_pessoa_por_id(pessoa_id)
        
        if pessoa:
            print("\n" + "="*40)
            print(f"       DADOS DETALHADOS")
            print("="*40)
            print(f"ID:         {pessoa[0]}")
            print(f"Nome:       {pessoa[1]}")
            print(f"Idade:      {pessoa[2]}")
            print(f"Endereço:   {pessoa[3]}")
            print(f"Território: {pessoa[4]}")
            print("="*40)
        else:
            print(f"\n[AVISO] Nenhum registro encontrado com o ID: {pessoa_id}")
            
    except Exception as e:
        print("Erro ao exibir detalhes:", e)

        





