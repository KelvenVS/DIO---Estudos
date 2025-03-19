import datetime, os

def menu():
    saldo = 0
    limite_por_saque = 500
    saques_por_dia = 3
    trans_por_dia = 10
    
    extrato = {
        "Operação": [],
        "Data/Hora": [],
        "Saldo Anterior": [],
        "Valor": [],
        "Saldo Atual": []
        }
    usuarios = {
        'nome': [],
        'data_nascimento': [],
        'cpf': [],
        'endereco' : []}
    contas = []
    
    ### Auxiliares    
    def registrar_extrato(data):
        data = list(data)
        for key,value in zip(extrato,data):
            extrato[key].append(value)       
        
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
        nonlocal contas
        numero = f"{len(contas)+1:06d}"
        return numero
        
    ### Visualizar
    def option_visualizar_extrato():
        limpar_menu()
        if not extrato["Operação"]:
            print(f"Não Foram realizadas movimentações")
        else:
            print(f"{'Operação':<15}{'Data/Hora':<20}{'Saldo Anterior':>15}{'Valor':>15}{'Saldo Atual':>15}")
            
            for operacao, data_hora, saldo_anterior, valor, saldo in zip(
                extrato["Operação"], 
                extrato["Data/Hora"], 
                extrato["Saldo Anterior"], 
                extrato["Valor"], 
                extrato["Saldo Atual"]
            ):
                print(f"{operacao:<15}{data_hora:<20}{format_value(saldo_anterior):>15}{format_value(valor):>15}{format_value(saldo):>15}")

    def option_visualizar_saldo():
        print(f'O saldo atual é de {format_value(saldo)}')

    ### Operações Bancárias
    def option_sacar():
        limpar_menu()
        nonlocal saques_por_dia
        nonlocal trans_por_dia
        nonlocal saldo
        nonlocal option
        saldo_anterior = saldo
        
        valor = safe_input(float,'Digite o valor do saque: R$')
        
        if saques_por_dia <= 0 or trans_por_dia <= 0:
            print(f'O limite diário de saques ou transações foi excedido. Por favor, tente novamente mais tarde.')
        elif valor > saldo:
            print(f'Não é possivel sacar o valor {format_value(valor)}.')
            option_visualizar_saldo()
        elif valor > limite_por_saque:
            print(f'Não é possível sacar o valor {format_value(valor)}, pois excede o limite permitido por saque: {format_value(limite_por_saque)}.')
        else:
            print(f'Realizando o saque de {format_value(valor)}')
            saldo-=valor
            saques_por_dia-=1
            trans_por_dia-=1
            data = (menu_keys[option - 1],date_now(),saldo_anterior,valor,saldo)
            registrar_extrato(data)
            option_visualizar_saldo()
            
    def option_depositar():
        limpar_menu()
        nonlocal saldo
        saldo_anterior = saldo
        nonlocal option
        nonlocal trans_por_dia
        if trans_por_dia <= 0:
            print('O limite diário transações foi excedido')
        else:
            valor = safe_input(float,f'Digite o valor do depósito: R$ ')
            print(f'Depositando {format_value(valor)}')
            saldo+=valor
            trans_por_dia-=1
            data = (menu_keys[option - 1],date_now(),saldo_anterior,valor,saldo)
            registrar_extrato(data)
            option_visualizar_saldo()
    
    ### Usuários
    def criar_usuario():
        nonlocal usuarios
        print(f'Bem Vindo ao cadastro do banco:')
        cpf = safe_input(int,'Por favor, insira seu CPF (apenas números): ')
        
        if cpf in usuarios['cpf']:
            print('CPF ja cadastrado !!!')
        else:
            nome = safe_input(str,'Por favor, insira seu nome: ')
            data_nascimento = safe_input(str,'Por favor, insira sua data de nascimento (DD/MM/AAAA): ')
            endereco = safe_input(str,'Por favor, insira seu endereço: ')
            
            data = [nome,data_nascimento,cpf,endereco]
            for key,value in zip(usuarios,data):
                usuarios[key].append(value) 
        
    def criar_conta():
        nonlocal usuarios
        nonlocal contas
        print(f'Bem vindo ao cadastro de conta:')
        
        cpf = safe_input(int,'Por favor, insira seu CPF (apenas números): ')
        agencia = '0001'
        numero = gerar_numero_conta()
        extrato = []
        
        if cpf not in usuarios['cpf']:
            print('Usuário não cadastrado')
        else:
            contas.append({
                'cpf': cpf,
                'agencia' : agencia,
                'numero' : numero,
                'extrato' : []
            })
            print(f'Conta adicionada com sucesso')
        
    ### Menu
    menu_dict = {
        'Sacar': option_sacar,
        'Depositar': option_depositar,
        'Visualizar Extrato': option_visualizar_extrato,
        'Visualizar Saldo': option_visualizar_saldo,
        'Cadastrar Usuário': criar_usuario,
        'Cadastrar Conta': criar_conta,
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