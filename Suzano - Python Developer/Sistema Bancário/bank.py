import datetime, os

usuarios = []
contas = []

def menu():
   
    ### Auxiliares    
    def registrar_extrato(data):
        extrato_linha = {
        "Operação": None,
        "Data/Hora": None,
        "Saldo Anterior": None,
        "Valor": None,
        "Saldo Atual": None
        }
        
        data = list(data)
        for key,value in zip(extrato_linha,data):
            extrato_linha[key] = value 
        return extrato_linha     
        
    def date_now():
        d = datetime.datetime.now()
        return d.strftime("%d/%m/%Y %H:%M")
    
    def format_value(value):
        return (f'R$ {value:.2f}')
        
    def exit_prog():
        print("Saindo do programa...")
        exit()
    
    def safe_input(data_type, prompt):
        while True:
            try:
                return data_type(input(prompt))
            except ValueError:
                print(f"Entrada inválida! Digite um valor do tipo {data_type.__name__}.")
            
    def limpar_menu():
        os.system('cls') if os.name == 'nt' else  os.system('clear')
        
    def gerar_numero_conta():
        global contas
        numero = f"{len(contas)+2106:06d}"
        return numero
        
    ### Visualizar
    def option_visualizar_extrato():
        limpar_menu()
        
        num_conta = safe_input(str,f'Insira o número da conta: ')
        conta = buscar_conta(num_conta)
        if conta is None:
            return
        
        if not conta["extrato"]:
            print(f"Não Foram realizadas movimentações")
        else:
            print(f"{'Operação':<15}{'Data/Hora':<20}{'Saldo Anterior':>15}{'Valor':>15}{'Saldo Atual':>15}")
            
            for extrato in conta["extrato"]:
                print(f"{extrato['Operação']:<15}{extrato['Data/Hora']:<20}{format_value(extrato['Saldo Anterior']):>15}{format_value(extrato['Valor']):>15}{format_value(extrato['Saldo Atual']):>15}")
            
    def option_visualizar_saldo(conta=None):
        if conta is None:
            num_conta = safe_input(str,f'Insira o número da conta: ')
            conta = buscar_conta(num_conta)
            if conta is None:
                print('Conta não encontrada')
                return
            else:
                print(f"O saldo da conta {conta['numero']} é de {format_value(conta['saldo'])}")
        else:
            print(f"O saldo da conta {conta['numero']} é de {format_value(conta['saldo'])}")    

    ### Operações Bancárias
    def option_sacar():
        limpar_menu()
        
        num_conta = safe_input(str,f'Insira o número da conta: ')

        conta = buscar_conta(num_conta)
        if conta is None:
            return
        
        valor = safe_input(float,'Digite o valor do saque: R$')
        
        if conta['saques_limite'] <= 0 or conta['transacoes_limite'] <= 0:
            print(f'O limite diário de saques ou transações foi excedido. Por favor, tente novamente mais tarde.')
        elif valor > conta['saldo']:
            print(f'Não é possivel sacar o valor {format_value(valor)}.')
            option_visualizar_saldo()
        elif valor > conta['limite_por_saque']:
            print(f"Não é possível sacar o valor {format_value(valor)}, pois excede o limite permitido por saque: {format_value(conta['limite_por_saque'])}.")
        else:
            print(f'Realizando o saque de {format_value(valor)}')
            nonlocal option
            saldo_anterior = conta['saldo']
            conta['saldo']-=valor
            conta['saques_limite']-=1
            conta['transacoes_limite']-=1
            data = (menu_keys[option - 1],date_now(),saldo_anterior,valor,conta['saldo'])
            conta['extrato'].append(registrar_extrato(data))
            option_visualizar_saldo(conta)
            
    def option_depositar():
        limpar_menu()
        num_conta = safe_input(str,f'Insira o número da conta: ')
        conta = buscar_conta(num_conta)
        if conta is None:
            return

        if conta['transacoes_limite'] <= 0:
            print('O limite diário transações foi excedido')
        else:
            nonlocal option
            saldo_anterior = conta['saldo']
            valor = safe_input(float,f'Digite o valor do depósito: R$ ')
            print(f'Depositando {format_value(valor)}')
            conta['saldo']+=valor
            conta['transacoes_limite']-=1
            data = (menu_keys[option - 1],date_now(),saldo_anterior,valor,conta['saldo'])
            conta['extrato'].append(registrar_extrato(data))
            option_visualizar_saldo(conta)
    
    ### Usuários
    def criar_usuario():
        global usuarios
        print(f'Bem Vindo ao cadastro do banco:')
        cpf = safe_input(int,'Por favor, insira seu CPF (apenas números): ')
        
        if verificar_cadastro_usuario(cpf):
            print('Esse CPF ja foi cadastrado !!!')
            return   
    
        nome = safe_input(str,'Por favor, insira seu nome: ')
        data_nascimento = safe_input(str,'Por favor, insira sua data de nascimento (DD/MM/AAAA): ')
        endereco = safe_input(str,'Por favor, insira seu endereço: ')
        
        usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco' : endereco}

        usuarios.append(usuario)
        
    def criar_conta():
        global usuarios
        global contas
        
        print(f'Bem vindo ao cadastro de conta:')
        cpf = safe_input(int,'Por favor, insira seu CPF (apenas números): ')

        if verificar_cadastro_usuario(cpf):
            pass
        else:
            print('Usuário não cadastrado')
            return
        
        conta = {
            'cpf': cpf,
            'agencia' : '0001',
            'numero' : gerar_numero_conta(),
            'saldo' : 500,
            'saques_limite' : 3,
            'transacoes_limite' : 10,
            'limite_por_saque' : 500,
            'extrato' : []}
        
        contas.append(conta)
        print(f'Conta adicionada com sucesso')
    
    def listar_usuarios():
        global usuarios
        if usuarios == []:
            print('Não há usuários cadastrados')
        else:
            for elem in usuarios:
                print(elem)
    
    def listar_contas():
        global contas
        
        for conta in contas:
            print(conta)
    
    def verificar_cadastro_usuario(cpf):
        global usuarios
        for usuario in usuarios:
            if usuario['cpf'] == cpf:
                return True
        return False      
    
    def buscar_conta(num_conta):
        global contas
        for conta in contas:
            if conta['numero'] == num_conta:
                return conta
        print('Conta não encontrada.')
        return None

    
    ### Menu
    menu_dict = {
        'Sacar': option_sacar,
        'Depositar': option_depositar,
        'Visualizar Extrato': option_visualizar_extrato,
        'Visualizar Saldo': option_visualizar_saldo,
        'Cadastrar Usuário': criar_usuario,
        'Cadastrar Conta': criar_conta,
        'Listar Usuários' : listar_usuarios,
        'Listar Contas' : listar_contas,
        'Sair': exit_prog}
    
    menu_keys = list(menu_dict.keys())
    while True:
        print(f"{'#'*47} Menu {'#'*47}")
        
        for i, elem in enumerate(menu_keys, 1):
            print(f"{i}. {elem}")
        
        print(f"{'#'*100}") 
        option = int(input(f'Escolha uma das opções: '))

        if option not in range(1,len(menu_keys) + 1):
            print(f'Opção inválida')
        else:
            menu_dict[menu_keys[option - 1]]()

if __name__ == '__main__':
    while True:
        menu()