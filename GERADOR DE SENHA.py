import random
import string
import json
import os

# --- GERAÇÃO DE SENHA---

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres_disponiveis = string.ascii_lowercase
    if usar_maiusculas:
        caracteres_disponiveis += string.ascii_uppercase
    if usar_numeros:
        caracteres_disponiveis += string.digits
    if usar_simbolos:
        caracteres_disponiveis += string.punctuation

    if not caracteres_disponiveis:
        return "Erro: Selecione pelo menos um tipo de caractere."

    senha = ''.join(random.choice(caracteres_disponiveis) for _ in range(tamanho))
    return senha

# --- GERENCIAMENTO DE SENHAS ---

ARQUIVO_SENHAS = "meu_gerenciador.json"

def salvar_senha(servico, usuario, senha):
    """Salva uma senha no arquivo JSON."""
    dados = carregar_senhas()
    dados[servico] = {"usuario": usuario, "senha": senha}
    
    with open(ARQUIVO_SENHAS, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print(f"\n[Sucesso] Senha para '{servico}' salva!")

def carregar_senhas():
    """Lê o arquivo JSON e retorna um dicionário."""
    if not os.path.exists(ARQUIVO_SENHAS):
        return {}
    with open(ARQUIVO_SENHAS, "r") as arquivo:
        return json.load(arquivo)

def listar_senhas():
    """Exibe todas as senhas salvas."""
    dados = carregar_senhas()
    if not dados:
        print("\nNenhuma senha encontrada.")
        return

    print("\n=== SENHAS ARMAZENADAS ===")
    for servico, info in dados.items():
        print(f"Serviço: {servico} | Usuário: {info['usuario']} | Senha: {info['senha']}")

# --- INTERFACE DE TESTE ATUALIZADA ---

if __name__ == "__main__":
    while True:
        print("\n--- MENU ---")
        print("1. Gerar e Salvar Nova Senha")
        print("2. Ver Senhas Salvas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            servico = input("Nome do serviço (ex: Netflix, Gmail): ")
            usuario = input("Nome de usuário/e-mail: ")
            tam = int(input("Tamanho da senha desejado: "))
            
            # Chama sua função original
            nova_senha = gerar_senha(tamanho=tam)
            
            # Salva usando a nova função
            salvar_senha(servico, usuario, nova_senha)
            print(f"Senha gerada: {nova_senha}")

        elif opcao == "2":
            listar_senhas()

        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")