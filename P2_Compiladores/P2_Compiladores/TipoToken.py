from enum import Enum

class TipoToken(Enum):
    IDENTIFICADOR = 1
    SELECT = 2
    FROM = 3
    Distinct= 4
    COMA = 5
    PUNTO = 6
    ASTERISCO = 7
    EOF = 8
