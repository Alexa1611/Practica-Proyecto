from enum import Enum

class TipoToken(Enum):
    Identificador = 1
    Select = 2
    From = 3
    Distinct= 4
    COMA = 5
    PUNTO = 6
    ASTERISCO = 7
    EOF = 8