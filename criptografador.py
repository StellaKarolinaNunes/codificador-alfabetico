import os
import time

def limpar_tela():
    """
    Limpa a tela do terminal de forma compatível com diferentes sistemas operacionais.
    Funciona tanto em Windows quanto em Linux/macOS.
    """
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux ou macOS
        os.system('clear')

def criptografar_por_posicao(texto):
    """
    Converte cada letra do texto para sua posição correspondente no alfabeto.
    Letras maiúsculas e minúsculas são tratadas igualmente.
    Caracteres que não são letras (como números, espaços e símbolos) são ignorados.

    Exemplo:
        Entrada: "abc"
        Saída: "123"
    """
    texto_processado = texto.lower()
    resultado = ""
    
    for caractere in texto_processado:
        if 'a' <= caractere <= 'z':
            posicao = ord(caractere) - ord('a') + 1
            resultado += str(posicao)
    
    return resultado

# ================================================================
#              CRIPTOGRAFADOR POR POSIÇÃO DO ALFABETO
# ================================================================

# Limpa o terminal para uma exibição limpa
limpar_tela()

# Apresentação do programa
print("=" * 55)
print("       CRIPTOGRAFADOR SIMPLES POR POSIÇÃO DO ALFABETO")
print("=" * 55)
print("\nEste programa transforma cada letra de um texto em um número,")
print("baseado na sua posição no alfabeto (a=1, b=2, ..., z=26).")
print("Caracteres não alfabéticos (como espaços e pontuações) são ignorados.\n")
print("-" * 55)

# ---------------------- ENTRADA DO USUÁRIO ----------------------
texto_digitado = input("Por favor, digite o texto que você quer 'criptografar': ")

# ---------------------- PROCESSAMENTO ---------------------------
# Criptografa o texto digitado pelo usuário
texto_criptografado = criptografar_por_posicao(texto_digitado)

# ---------------------- SAÍDA / RESULTADO -----------------------
# Aguarda um momento antes de limpar a tela
time.sleep(1)
limpar_tela()

# Exibe o texto original e o resultado da criptografia
print("\n" + "=" * 55)
print("                 RESULTADO DA CRIPTOGRAFIA")
print("=" * 55)
print(f"\n   Texto Original:       '{texto_digitado}'")
print(f"   Texto Criptografado:  {texto_criptografado}\n")
print("-" * 55)
print("   Criptografia concluída com sucesso! 😉")
print("=" * 55)

# Espera alguns segundos antes de encerrar o programa
time.sleep(3)
