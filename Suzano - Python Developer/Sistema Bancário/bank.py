def menu():
    saldo = 0
    extrato = []
    
    def option_sacar():
        valor = int(input('Digite o valor do saque: '))
        print(f'Sacando {valor}')
    
    def option_depositar():
        valor = int(input('Digite o valor do depósito: '))
        print(f'Depositando {valor}')
    
    def option_vizualizar_extrato():
        print(f'O saldo atual é de {saldo}')
        
    def exit_prog():
        print("Saindo do programa...")
        exit()
    
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
    while  True:
        menu()