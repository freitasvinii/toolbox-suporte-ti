import os
import platform
import socket
import shutil
import time

def limpar_tela():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def info_sistema():
    print("-" * 30)
    print("INFORMAÇÕES DO SISTEMA")
    print("-" * 30)
    print(f"Sistema Operacional: {platform.system()} {platform.release()}")
    print(f"Nome da Máquina: {socket.gethostname()}")
    print(f"Processador: {platform.processor()}")
    print("-" * 30)
    input("\nPressione Enter para voltar...")

def verificar_rede():
    print("-" * 30)
    print("TESTE DE CONECTIVIDADE (PING)")
    print("-" * 30)
    host = "google.com"
    # O parametro -n é para Windows, -c é para Linux
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = f"ping {param} 4 {host}"
    
    print(f"Pingando {host}...")
    os.system(comando)
    print("-" * 30)
    input("\nPressione Enter para voltar...")

def verificar_disco():
    print("-" * 30)
    print("ESPAÇO EM DISCO")
    print("-" * 30)
    # Pega o espaço do disco principal
    total, usado, livre = shutil.disk_usage("/")
    
    # Converte bytes para GB
    print(f"Total: {total // (2**30)} GB")
    print(f"Usado: {usado // (2**30)} GB")
    print(f"Livre: {livre // (2**30)} GB")
    print("-" * 30)
    input("\nPressione Enter para voltar...")

def menu():
    while True:
        limpar_tela()
        print("=== FERRAMENTA DE SUPORTE TI ===")
        print("1. Exibir Informações do Sistema")
        print("2. Testar Conectividade (Ping Google)")
        print("3. Verificar Espaço em Disco")
        print("0. Sair")
        print("================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            info_sistema()
        elif opcao == '2':
            verificar_rede()
        elif opcao == '3':
            verificar_disco()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu()