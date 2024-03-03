limite_saques = 10

def menu():
    return input("""
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q] Sair
        => """)


def depositar(saldo, valor):
    return saldo + valor if valor > 0 else saldo


def sacar(saldo, valor, limite, numero_saques, limite_saques):
    saque_valido = (
        valor > 0
        and saldo >= valor
        and valor <= limite
        and numero_saques < limite_saques
    )
    return saldo - valor if saque_valido else saldo


def exibir_extrato(saldo):
    print(f"""
        Saldo: R$ {saldo:.2f}
    """)


def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        print("Usuário já cadastrado!")
        return
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("Usuário não encontrado!")
        return
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


def listar_contas(contas):
    for conta in contas:
        print(f"""
            Agência: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
        """)


def main():
    saldo = 0
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo = depositar(saldo, valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo = sacar(saldo, valor, limite, numero_saques, limite_saques)

        elif opcao == "e":
            exibir_extrato(saldo)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta("0001", numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida!")


main()