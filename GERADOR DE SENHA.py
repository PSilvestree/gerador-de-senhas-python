import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    """
    Gera uma senha aleatória baseada nos parâmetros fornecidos.
    """
    # Começamos sempre com letras minúsculas
    caracteres_disponiveis = string.ascii_lowercase
    
    # Adicionamos outros tipos de caracteres conforme as opções escolhidas
    if usar_maiusculas:
        caracteres_disponiveis += string.ascii_uppercase
    if usar_numeros:
        caracteres_disponiveis += string.digits
    if usar_simbolos:
        caracteres_disponiveis += string.punctuation

    # Verifica se há pelo menos um tipo de caractere selecionado
    if not caracteres_disponiveis:
        return "Erro: Selecione pelo menos um tipo de caractere."

    # Gera a senha escolhendo caracteres aleatórios do conjunto disponível
    senha = ''.join(random.choice(caracteres_disponiveis) for _ in range(tamanho))
    
    return senha

# --- Testando o Gerador ---
if __name__ == "__main__":
    print("=== Gerador de Senhas ===")
    
    # Exemplo 1: Senha padrão (12 caracteres, todos os tipos)
    senha_padrao = gerar_senha()
    print(f"Senha Padrão (12 chars): {senha_padrao}")
    
    # Exemplo 2: Senha super forte (20 caracteres)
    senha_forte = gerar_senha(tamanho=20)
    print(f"Senha Forte (20 chars):  {senha_forte}")
    
    # Exemplo 3: Apenas letras e números (PIN complexo)
    senha_letras_numeros = gerar_senha(tamanho=8, usar_simbolos=False)
    print(f"Senha sem símbolos:      {senha_letras_numeros}")