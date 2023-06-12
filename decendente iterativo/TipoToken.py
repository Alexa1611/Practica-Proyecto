from enum import Enum

class TipoToken(Enum):
    IDENTIFICADOR = "IDENTIFICADOR"
    SELECT = "select"
    FROM = "from"
    DISTINCT = "distinct"
    COMA = ","
    PUNTO = "."
    ASTERISCO = "*"
    EOF = "EOF"