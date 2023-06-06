class Principal:
   
    @staticmethod
    def ejecutarPrompt():
        while True:
            L1 = input(">>> ")
            if not L1:
                break 
            Principal.ejecutar(L1)
            Principal.existenErrores = False

    @staticmethod
    def ejecutar(source):
        scanner = scanner(source)
        tokens = scanner.scanTokens()

        parser = parser(tokens)
        parser.parse()

    @staticmethod
    def error(L1, mj):
        Principal.reportar(L1, "", mj)

    @staticmethod
    def reportar(L1, donde, mj):
        print(f"[L1 {L1}] Error {donde}: {mj}")
        Principal.existenErrores = True

