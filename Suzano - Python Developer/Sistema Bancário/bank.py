import datetime

def menu():
    saldo = 0
    limite_por_saque = 500
    saques_por_dia = 3
    extrato = []
    
    def date_now():
        d = datetime.datetime.now()
        return d.strftime("%d/%m/%Y %H:%M")
    
    def format_value(value):
        return (f'R$ {value:.2f}')
    
    def option_visualizar_extrato():
        nonlocal extrato
        if extrato == []:
            print(f'Não Foram realizadas movimentações')
        else:
            print(f"{'Operação':<10}{'Data/Hora':>20}{'Saldo Anterior':>15}{'Valor':>15}{'Saldo Atual':>15}")
            for operacao,data_hora,valor,saldo_anterior,saldo in extrato:
                print(f'{operacao:<10}{data_hora:>20}{format_value(saldo_anterior):>15}{format_value(valor):>15} {format_value(saldo):>15}')

    def option_visualizar_saldo():
        print(f'O saldo atual é de {format_value(saldo)}')
        
    def exit_prog():
        print("Saindo do programa...")
        exit()
    
    def option_sacar():
        nonlocal saques_por_dia
        nonlocal saldo
        saldo_anterior = saldo
        nonlocal option
        
        valor = int(input('Digite o valor do saque: R$'))
        
        if saques_por_dia <= 0:
            print(f'Limite de saque diário ultrapassado. Tente novamente mais tarde.')
        elif valor > saldo:
            print(f'Não é possivel sacar o valor {format_value(valor)}.')
            option_visualizar_saldo()
        elif valor > limite_por_saque:
            print(f'Não é possivel sacar o valor {format_value(valor)} , pois é maior que limite por saque / {format_value(limite_por_saque)}')
        else:
            print(f'Sacando {format_value(valor)} de {format_value(saldo)}')
            saldo-=valor
            saques_por_dia-=1
            extrato.append((menu_keys[option - 1],date_now(),valor,saldo_anterior,saldo))
            option_visualizar_saldo()
            
    def option_depositar():
        nonlocal saldo
        saldo_anterior = saldo
        nonlocal option
        
        valor = int(input('Digite o valor do depósito: R$'))
        print(f'Depositando {format_value(valor)}')
        saldo+=valor
        extrato.append((menu_keys[option - 1],date_now(),valor,saldo_anterior,saldo))
        option_visualizar_saldo()
    
    menu_dict = {
        'Sacar': option_sacar,
        'Depositar': option_depositar,
        'Visualizar Extrato': option_visualizar_extrato,
        'Visualizar Saldo': option_visualizar_saldo,
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