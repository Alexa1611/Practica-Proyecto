from contextvars import Token

from TipoToken import TipoToken


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.identificador = Token(TipoToken.IDENTIFICADOR, "")
        self.select = Token(TipoToken.SELECT, "select")
        self.fron = Token(TipoToken.FROM, "from")
        self.distinct = Token(TipoToken.DISTINCT, "distinct")
        self.coma = Token(TipoToken.COMA, ",")
        self.punto = Token(TipoToken.PUNTO, ".")
        self.asterisco = Token(TipoToken.ASTERISCO, "*")
        self.finCadena = Token(TipoToken.EOF, "")

        self.i = 0
        self.HErrores = False

        self.preanalisis = None

    def parse(self):
        self.i = 0
        self.preanalisis = self.tokens[self.i]
        self.q()

        if not self.HErrores and not self.preanalisis == self.finCadena:
            print("Error en la posición " + self.preanalisis.posicion + ". No se esperaba el token " + self.preanalisis.tipo)
        elif not self.HErrores and self.preanalisis == self.finCadena:
            print("Consulta válida")

    def q(self):
        if self.preanalisis == self.select:
            self.match(self.select)
            self.d()
            self.match(self.fron)
            self.t()
        else:
            self.HErrores = True
            print("Error en la posición " + self.preanalisis.posicion + ". Se esperaba la palabra reservada SELECT.")

    def d(self):
        if self.HErrores:
            return

        if self.preanalisis == self.distinct:
            self.match(self.distinct)
            self.p()
        elif self.preanalisis == self.asterisco or self.preanalisis == self.identificador:
            self.p()
        else:
            self.HErrores = True
            print("Error en la posición " + self.preanalisis.posicion + ". Se esperaba DISTINCT, * o un identificador.")

    def p(self):
        if self.HErrores:
            return

        if self.preanalisis == self.asterisco:
            self.match(self.asterisco)
        elif self.preanalisis == self.identificador:
            self.a()
        else:
            self.HErrores = True
            print("Error en la posición " + self.preanalisis.posicion + ". Se esperaba * o un identificador.")

    def a(self):
        if self.HErrores:
            return

        if self.preanalisis == self.identificador:
            self.a2()
            self.a1()
        else:
            self.HErrores = True
            print("Error en la posición " + self.preanalisis.posicion + ". Se esperaba un identificador.")

    def a1(self):
        if self.HErrores:
            return

        if self.preanalisis == self.coma:
            self.match(self.coma)
            self.a()

    def a2(self):
        if self.HErrores:
            return

        if self.preanalisis == self.identificador:
            self.match(self.identificador)
            self.a3()
        else:
            self.HErrores = True
            print("Error en la posición " + self.preanalisis.posicion + ". Se esperaba un identificador.")

    def a3(self):
        if self.HErrores:
            return

        if self.preanalisis == self.punto:
            self.match(self.punto)
            self.match(self.identificador)

    def t(self):
        if self.HErrores:
            return

        if self.preanalisis == self.identificador:
            self.t2()
            self.t1()
        else:
            self.HErrores = True
            print("Error en la posición " + self.preanalisis.posicion + ". Se esperaba un identificador.")

    def t1(self):
        if self.HErrores:
            return

        if self.preanalisis == self.coma:
            self.match(self.coma)
            self.t()

    def t2(self):
        if self.HErrores:
            return

        if self.preanalisis == self.identificador:
            self.match(self.identificador)
            self.t3()
        else:
            self.HErrores = True
            print("Error en la posición " + self.preanalisis.posicion + ". Se esperaba un identificador.")

    def t3(self):
        if self.HErrores:
            return

        if self.preanalisis == self.identificador:
            self.match(self.identificador)

    def match(self, t):
        if self.HErrores:
            return

        if self.preanalisis.tipo == t.tipo:
            self.i += 1
            self.preanalisis = self.tokens[self.i]
        else:
            self.HErrores = True
            print("Error en la posición " + self.preanalisis.posicion + ". Se esperaba un " + t.tipo)
