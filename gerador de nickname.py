import random
import string

def gerar_nickname(nome, sobrenome):
    # Obter pedaços aleatórios do nome e sobrenome
    parte_nome = nome[:random.randint(1, len(nome))].lower()
    parte_sobrenome = sobrenome[:random.randint(1, len(sobrenome))].lower()

    # Alternar entre maiúsculas e minúsculas
    parte_nome = ''.join(random.choice([c.upper(), c.lower()]) for c in parte_nome)
    parte_sobrenome = ''.join(random.choice([c.upper(), c.lower()]) for c in parte_sobrenome)

    # Inserir um caractere especial aleatório
    simbolo = random.choice(['_', '.', '-', ''])

    # Gerar um número aleatório entre 100 e 999
    numero = random.randint(100, 999)

    # Criar o nickname
    nickname = f"{parte_nome}{simbolo}{parte_sobrenome}{numero}"
    return nickname

# Exemplo de uso
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nickname = gerar_nickname(nome, sobrenome)
print(f"Seu nickname gerado é: {nickname}")
