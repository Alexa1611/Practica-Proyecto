
from Scanner import Scanner
from Parser import Parser


class Principal:
    @staticmethod
    def ejecutarPrompt():
        while True:
            L1 = input(">>> ")
            if not L1:
                break
            scanner_instancia = Scanner(L1)
            tokens = scanner_instancia.scanTokens()  # Almacenar los tokens generados
            for token in tokens:
                print(token)

            parser_instancia = Parser(tokens)
            parser_instancia.parse()

    @staticmethod
    def error(L1, mj):
        Principal.reportar(L1, "", mj)

    @staticmethod
    def reportar(L1, donde, mj):
        print(f"[L1 {L1}] Error {donde}: {mj}")
        Principal.existenErrores = True


Principal.ejecutarPrompt()