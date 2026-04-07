from services.pessoas import (cadastrar_pessoa,editar_cadastro,buscar_pessoa_por_id,listar_pessoas,exibir_detalhes_pessoa)
from services import atendimento

def exibir_menu():
    print("\n" + "="*60)
    print("      SISTEMA CREAS - GESTÃO DE ASSISTÊNCIA SOCIAL")
    print("="*60)
    print("1. Cadastrar Novo Usuário")
    print("2. Registrar Atendimento/Ofício (Usuário já cadastrado)")
    print("3. Atualizar Dados de um Usuário")
    print("4. Listar Todos os Usuários")
    print("5. Listar atendimentos e oficios de um usuário")
    print("6. Consultar dados de um cadastro específico")
    print("0. Sair do Sistema")
    print("="*60)
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    while True:
        opcao = exibir_menu()

        match opcao:

            case "1":
                print("\n--- CADASTRO DE NOVO USUÁRIO ---")
                nome = input("Nome completo: ")
                idade = int(input("Idade: "))
                endereco = input("Endereço: ")
                territorio = input("Território de referência: ")

                id_gerado = cadastrar_pessoa(nome, idade, endereco, territorio)

                if id_gerado:
                    print(f"\n[SUCESSO] Usuário cadastrado com ID: {id_gerado}")

                    e_vitima = input("O usuário é uma vítima de violência? (sim/nao): ").lower()

                    if e_vitima == "sim":
                        print("\n--- INICIANDO REGISTRO DE ATENDIMENTO ---")
                        violencia = input("Qual tipo de violência? ")
                        prontuario = input("Número do prontuário: ")
                        desc_oficio = input("Descrição do ofício: ")
                        origem = input("Órgão de origem: ")

                        atendimento.registrar_atendimento_com_oficio(
                            id_gerado, violencia, prontuario, desc_oficio, origem
                        )
                else:
                    print("\n[ERRO] Falha ao cadastrar no banco de dados.")

            case "2":
                print("\n--- REGISTRAR ATENDIMENTO (USUÁRIO EXISTENTE) ---")
                id_busca = input("Digite o ID do usuário: ")
                pessoa = buscar_pessoa_por_id(id_busca)

                if pessoa:
                    print(f"Usuário encontrado: {pessoa[1]}")
                    violencia = input("Tipo de violência: ")
                    prontuario = input("Número do prontuário: ")
                    desc_oficio = input("Descrição: ")
                    origem = input("Órgão de origem: ")

                    atendimento.registrar_atendimento_com_oficio(
                        id_busca, violencia, prontuario, desc_oficio, origem
                    )
                else:
                    print("\n[AVISO] ID não encontrado no sistema.")

            case "3":
                print("\n--- ATUALIZAR CADASTRO ---")
                id_busca = input("Digite o ID do usuário que deseja editar: ")
                pessoa = buscar_pessoa_por_id(id_busca)

                if pessoa:
                    print(f"Dados atuais: Nome: {pessoa[1]}, Idade: {pessoa[2]}")
                    print("(Deixe em branco para manter o valor atual)")

                    novo_nome = input(f"Novo nome [{pessoa[1]}]: ") or pessoa[1]
                    nova_idade = input(f"Nova idade [{pessoa[2]}]: ") or pessoa[2]
                    novo_end = input(f"Novo endereço [{pessoa[3]}]: ") or pessoa[3]
                    novo_terr = input(f"Novo território [{pessoa[4]}]: ") or pessoa[4]

                    editar_cadastro(id_busca, novo_nome, int(nova_idade), novo_end, novo_terr)
                    print("\n[SUCESSO] Cadastro atualizado!")
                else:
                    print("\n[AVISO] Usuário não encontrado.")

            case "4":
                print("\n--- LISTA DE USUÁRIOS NO SISTEMA ---")
                listar_pessoas()

            case "5":
                id = input("Digite o ID do usuário: ")
                print("\n--- DADOS DE ATENDIMENTOS DO USUÁRIO ---")
                atendimento.listar_atendimentos(id)

            case"6":
                id_busca = input("Digite o ID para consulta detalhada: ")
                exibir_detalhes_pessoa(id_busca)

            case "0":
                print("\nEncerrando o sistema CREAS. Até logo!")
                break

            case _:
                print("\n[ERRO] Opção inválida, tente novamente.")