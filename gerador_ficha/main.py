from .rolagem import gerar_atributos
from .ficha import criar_ficha

# Prioridades de atributos por classe
PRIORIDADES_CLASSE = {
    "Clérigo": ["Sabedoria", "Força", "Constituição", "Destreza", "Inteligência", "Carisma"],
    "Guerreiro": ["Força", "Constituição", "Destreza", "Sabedoria", "Inteligência", "Carisma"],
    "Ladrão": ["Destreza", "Constituição", "Força", "Carisma", "Inteligência", "Sabedoria"],
    "Mago": ["Inteligência", "Destreza", "Constituição", "Força", "Sabedoria", "Carisma"]
}

def escolher_classe():
    print("Escolha a classe do seu personagem:")
    print("1 - Clérigo")
    print("2 - Guerreiro")
    print("3 - Ladrão")
    print("4 - Mago")
    
    escolha = input("Digite o número da classe desejada: ").strip()
    classes = {
        "1": "Clérigo",
        "2": "Guerreiro",
        "3": "Ladrão",
        "4": "Mago"
    }
    return classes.get(escolha, None)

def alocar_atributos(classe, valores_rolados):
    """Aloca os valores rolados aos atributos conforme a prioridade da classe."""
    prioridades = PRIORIDADES_CLASSE[classe]
    valores_ordenados = sorted(valores_rolados, reverse=True)
    atributos = {}
    for i, atributo in enumerate(prioridades):
        atributos[atributo] = valores_ordenados[i]
    return atributos

def main():
    print("=== Gerador de Fichas de Old Dragon ===")
    
    # Gerar valores rolados
    valores_rolados = [sum(sorted([random.randint(1, 6) for _ in range(4)])[1:]) for _ in range(6)]
    print("\nValores Rolados:", valores_rolados)
    
    # Escolher classe
    classe = escolher_classe()
    if not classe:
        print("Escolha inválida! Tente novamente.")
        return
    
    # Alocar atributos conforme a prioridade da classe
    atributos = alocar_atributos(classe, valores_rolados)
    
    # Criar e exibir a ficha
    criar_ficha(classe, atributos)

if __name__ == "__main__":
    main()