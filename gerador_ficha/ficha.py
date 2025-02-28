from .personagem import Personagem

def criar_ficha(classe, atributos):
    """Cria e exibe a ficha do personagem."""
    personagem = Personagem(classe, atributos)
    print("\n=== Ficha do Personagem ===")
    print(personagem)
