import operacoes
import this
this.opcao = -1

def menu():
    print('\nEscolha uma das Opções abaixo: \n\n' +
          '1. Cadastrar\n'                        +
          '2. Consultar\n'                        +
          '3. Atualizar Nome \n'                  +
          '4. Atualizar Telefone\n'               +
          '5. Atualizar Endereço\n'               +
          '6. Atualizar Data de Nascimento\n'     +
          '7. Excluir\n'                          +
          '0.Sair\n')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe seu nome: ')
            nome = input()
            print('Informe seu Telefone: ')
            telefone = input()
            print('Informe seu endereço: ')
            endereco = input()
            print('Informe sua data de Nascimento: ')
            dtNasc = input()
            #Chamar o Método Inserir
            operacoes.inserir(nome, telefone, endereco, dtNasc)
        elif this.opcao == 2:
            operacoes.consultar()
        elif this.opcao == 3:
            print("Informe o código que deseja atualizar")
            this.codigo=int(input())
            print("Informe o novo nome: ")
            this.campo = input()
            operacoes.atualizar(this.codigo, 'nome', this.campo)
        elif this.opcao == 4:
            print("informe o código que deseja atualizar")
            this.codigo = int(input())
            print("informe o novo telefone: ")
            this.campo = input()
            operacoes.atualizar(this.codigo, 'telefone', this.campo)
        elif this.opcao == 5:
            print("informe o código que deseja atualizar")
            this.codigo =int(input())
            print("informe o novo Endereço: ")
            this.campo = input()
            operacoes.atualizar(this.campo, 'endereco', this.campo)
        elif this.opcao == 6:
            print("informe o código que deseja atualizar")
            this.codigo= int(input())
            print("informe a nova Data de Nascimento: ")
            this.campo= input()
            operacoes.atualizar(this.codigo, 'dataDeNascimento', operacoes.tratarData(this.campo))
        elif this.opcao == 7:
            print("Informe o código para a exclusão do dado")
            this.codigo = int(input())
            operacoes.excluir(this.codigo)


        else:
            print('Opção escolhida não é válida!')