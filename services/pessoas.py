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
        cmd = """
        SELECT nome, id 
        FROM pessoa;
        """
        cursor.execute(cmd)
        retorno = cursor.fetchall()
        for nome, id in retorno:
            print(f"id: {id} nome: {nome}")

    except Exception as e:
        print("Erro ao acessar o banco")
        print(e)

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
        

        

        





