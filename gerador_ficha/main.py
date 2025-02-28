from .rolagem import gerar_atributos
from .ficha import criar_ficha

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

def main():
    print("=== Gerador de Fichas de Old Dragon ===")
    
    atributos = gerar_atributos()
    print("\nAtributos Gerados:")
    for atributo, valor in atributos.items():
        print(f"{atributo}: {valor}")
    
    classe = escolher_classe()
    if not classe:
        print("Escolha inválida! Tente novamente.")
        return
    
    criar_ficha(classe, atributos)

if __name__ == "__main__":
    main()