class Personagem:
    def __init__(self, classe, atributos):
        self.classe = classe
        self.atributos = atributos

    def __str__(self):
        return (f"Classe: {self.classe}\n"
                f"Atributos:\n"
                f"Força: {self.atributos['Força']}\n"
                f"Destreza: {self.atributos['Destreza']}\n"
                f"Constituição: {self.atributos['Constituição']}\n"
                f"Inteligência: {self.atributos['Inteligência']}\n"
                f"Sabedoria: {self.atributos['Sabedoria']}\n"
                f"Carisma: {self.atributos['Carisma']}")