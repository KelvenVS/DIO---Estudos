def menu():
    saldo = 3000
    limite_por_saque = 500
    saques_por_dia = 3
    extrato = []
    
    def format_value(value):
        return (f'R$ {value:.2f}')
    
    def option_vizualizar_extrato():
        nonlocal extrato
        if extrato == []:
            print(f'Não Foram realizadas movimentações')
        else:
            for operacao,valor,saldo in extrato:
                print(f'{operacao} {valor} {saldo}')
        
    def option_vizualizar_saldo():
        print(f'O saldo atual é de {format_value(saldo)}')
        
    def exit_prog():
        print("Saindo do programa...")
        exit()
    
    def option_sacar():
        nonlocal saques_por_dia
        nonlocal saldo
        nonlocal option
        
        valor = int(input('Digite o valor do saque: '))
        
        if saques_por_dia <= 0:
            print(f'Limite de saque ultrapassado. Tente novamente mais tarde.')
        elif valor > saldo:
            print(f'Não é possivel sacar o valor {format_value(valor)} , pois é maior que o saldo {format_value(saldo)}')
        elif valor > limite_por_saque:
            print(f'Não é possivel sacar o valor {format_value(valor)} , pois é maior que limite por saque / {format_value(limite_por_saque)}')
        else:
            print(f'Sacando {format_value(valor)} de {format_value(saldo)}')
            saldo-=valor
            saques_por_dia-=1
            extrato.append((menu_keys[option - 1],valor,saldo))
            option_vizualizar_saldo()

    def option_depositar():
        valor = int(input('Digite o valor do depósito: '))
        print(f'Depositando {format_value(valor)}')
    
    menu_dict = {
        'Sacar': option_sacar,
        'Depositar': option_depositar,
        'Vizualizar Extrato': option_vizualizar_extrato,
        'Sair': exit_prog
    }
    
    menu_keys = list(menu_dict.keys())
    
    while True:
        print(f"{'#'*25} Menu {'#'*25}")
        
        for i, elem in enumerate(menu_keys, 1):
            print(f"{i}. {elem}")
        
        print(f"{'#'*56}") 
        option = int(input(f'Escolha uma das opções: '))

        if option not in range(1,len(menu_keys) + 1):
            print(f'Opção inválida')
        else:
            menu_dict[menu_keys[option - 1]]()

if __name__ == '__main__':
    while True:
        menu()