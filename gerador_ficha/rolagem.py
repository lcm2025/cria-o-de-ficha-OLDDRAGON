import random

def rolar_dado(faces=6):
    """Rola um dado com o número de faces especificado."""
    return random.randint(1, faces)

def gerar_atributos():
    """Gera atributos iniciais (rolagem 4d6, descarta o menor)."""
    atributos = {
        "Força": sum(sorted([rolar_dado() for _ in range(4)])[1:]),
        "Destreza": sum(sorted([rolar_dado() for _ in range(4)])[1:]),
        "Constituição": sum(sorted([rolar_dado() for _ in range(4)])[1:]),
        "Inteligência": sum(sorted([rolar_dado() for _ in range(4)])[1:]),
        "Sabedoria": sum(sorted([rolar_dado() for _ in range(4)])[1:]),
        "Carisma": sum(sorted([rolar_dado() for _ in range(4)])[1:])
    }
    return atributos