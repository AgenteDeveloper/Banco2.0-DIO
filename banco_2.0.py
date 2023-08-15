def menu():
    return input(
        """
        Seja bem vindo ao Banco TB!

        Selecione uma das operações abaixo para continuar:

        [D] - Depositar
        [S] - Sacar
        [E] - Extrato
        [N] - Novo Cadastro
        [C] - Nova Conta
        [Q] - Sair

        => """
    )

def saque(*,saldo,valor,extrato,limite,numero_saques,limite_diario):
    execede_saldo = valor > saldo

    execede_limite = valor > limite         
    
    execede_diario = numero_saques >= limite_diario

    if execede_saldo:
        print("Valor inserido é maior do que seu saldo. Tente novamente")
            
    elif execede_limite:
        print("Valor maior que limite permitido. Tente novamente")
            
    elif execede_diario:
        print("Limite diário alcançado, tente novamente amanhã.")

    elif valor > 0:
        saldo -= valor

        extrato += f"Saque: R$ {valor:.2f} \n"

        numero_saques += 1

        print("Valor sacado com sucesso")
    else:
        print("Valor inserido inválido, tente novamente") 

    return saldo,extrato

def deposito(*,saldo,valor,extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} \n"
        print("Valor depositado com sucesso!")
    else:
         print("Valor inserido inválido, tente novamente") 

    return(saldo,extrato)

def exibir_extrato(saldo,/,*, extrato):
    print("\n<<<<<<Extrato>>>>>")
    print("Sem movimentações na conta" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f} \n")
    print("<<<<<<<<<>>>>>>>>>")
    print()

def cadastro_usuario(usuarios):
    cpf = input("Informe seu CPF para consulta de disponibilidade, apenas numeros: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("< Usuário já Cadastrado, tente novamente >")
        return
    
    nome = input("Insira o seu nome completo: ")
    data_nascimento = input("Insira sua data de nascimento (dia, mes, ano): ")
    endereco = input("Insira o seu endereco com logradouro - nº - CEP e cidade/sigla estado ")

    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    
    print("<Usuário Criado com sucesso! Bem vindo ao nosso banco!>")

def cadastro_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\n <Conta criada com sucesso>")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}

    print("Usuario não encontrado, reiniciando criação de conta")

def filtro_usuario(cpf,usuario):
    usuario_filtrar = [usuario for usuario in usuario if usuario["cpf"] == cpf]
    return(usuario_filtrar[0] if usuario_filtrar else None)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_diario = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = input(menu)

        if opcao == "D":
            valor = float(input("Insira o valor a ser depositado: "))

            saldo,extrato = deposito(saldo,valor,extrato)

             


        elif opcao == "S":
            valor = float(input("Insira o valor a ser sacado: "))

            saldo,extrato = saque(

                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_diario=limite_diario,
            )

            
        elif opcao == "E":

            exibir_extrato(saldo, extrato=extrato)


            # print("\n<<<<<<Extrato>>>>>")
            # print("Sem movimentações na conta" if not extrato else extrato)
            # print(f"Saldo: R$ {saldo:.2f} \n")
            # print("<<<<<<<<<>>>>>>>>>")

        elif opcao == "N":
            cadastro_usuario(usuarios)

        elif opcao == "C":
            numero_conta = len(contas) + 1
            conta = cadastro_conta(AGENCIA, numero_conta,usuarios)

            if conta:
                contas.append(conta)
         

        elif opcao == "Q":
            break
        
        else:
         print("Operação inexistente, tente novamente com uma das opções disponiveis")   

if __name__ == "__main__":
    main()