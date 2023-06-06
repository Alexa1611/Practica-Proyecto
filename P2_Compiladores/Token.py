class Token:
    def __init__(self, tipo, lexema, posicion=0):
        self.tipo = tipo
        self.lexema = lexema
        self.posicion = posicion

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False

        if self.tipo == other.tipo and self.lexema == other.lexema:
            return True

        return False

    def __str__(self):
        return str(self.tipo) + " " + str(self.lexema) + " "
