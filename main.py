
from services.pessoas import cadastrar_pessoa
from services.atendimento import registrar_atendimento_com_oficio

if __name__ == "__main__":

    print("BANCO DE DADOS PARA O CREAS - CENTRO DE REFERÊNCIA ESPECIALIZADO DE ASSISTÊNCIA SOCIAL - SUAS")
    print("Bem-vindo ao sistema de cadastro de usuários do CREAS!")

    cadastrar = input("Deseja cadastrar um novo usuário?")

    if cadastrar.lower() == "sim":

        nome = input("Digite o nome do usuário: ")
        vitima = input("O usuário é uma vítima de violência? ")
        idade = int(input("Digite a idade do usuário: "))
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        territorio = input("Digite o território de referência de acordo com o CRAS da região do seu endereço: ")
        telefone = input("Digite o telefone do usuário: ")


        cadastrar_pessoa(nome, idade, endereco, territorio)

        print("Usuário cadastrado com sucesso!")


        violencia = input("Qual tipo de violência o usuário sofreu? ")
        numero_prontuario = input("Número do prontuário: ")
        descricao = input("Descrição do ofício: ")
        orgao_origem = input("Órgão de origem: ")

        registrar_atendimento_com_oficio(
            pessoa_id=1,
            tipo_violencia=violencia,
            numero_prontuario=numero_prontuario,
            descricao=descricao,
            orgao_origem=orgao_origem
        )

    else:
        print("Encerrando o sistema.")