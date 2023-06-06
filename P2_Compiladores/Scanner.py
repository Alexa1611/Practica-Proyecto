
from contextvars import Token

from TipoToken import TipoToken


class Scanner:
    def __init__(self, source):
        self.source = source + " "
        self.tokens = []

    def scanTokens(self):
        estado = 0
        lexema = ""
        inicioLexema = 0
        palabrasReservadas = {
            "if": TipoToken.IF,
            "else": TipoToken.ELSE,
            # Agrega más palabras reservadas si es necesario
        }

        for i in range(len(self.source)):
            caracter = self.source[i]

            if estado == 0:
                if caracter == '*':
                    self.tokens.append(Token(TipoToken.ASTERISCO, "*", i + 1))
                elif caracter == ',':
                    self.tokens.append(Token(TipoToken.COMA, ",", i + 1))
                elif caracter == '.':
                    self.tokens.append(Token(TipoToken.PUNTO, ".", i + 1))
                elif caracter.isalpha():
                    estado = 1
                    lexema = lexema + caracter
                    inicioLexema = i

            elif estado == 1:
                if caracter.isalpha() or caracter.isdigit():
                    lexema = lexema + caracter
                else:
                    tt = palabrasReservadas.get(lexema)
                    if tt is None:
                        self.tokens.append(Token(TipoToken.IDENTIFICADOR, lexema, inicioLexema + 1))
                    else:
                        self.tokens.append(Token(tt, lexema, inicioLexema + 1))

                    estado = 0
                    i -= 1
                    lexema = ""
                    inicioLexema = 0

        self.tokens.append(Token(TipoToken.EOF, "", len(self.source)))

        return self.tokens
