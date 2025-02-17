class Text_Compress:
    def __init__(self):
        import gzip
        self.__gzip = gzip

    def compress(self, texto: str) -> bytes:
        return self.__gzip.compress(texto.encode())

    def decompress(self, texto: bytes) -> str:
        return self.__gzip.decompress(texto).decode()


TEXTO = Text_Compress()

if __name__ == "__main__":
   texto ="To use this script, save it as a .py file (e.g., git_commit.py) and make sure you have installed the OpenAI API client library. You can then run it from the command line like so:"
   print(TEXTO.compress(texto))
   print(TEXTO.decompress(TEXTO.compress(texto)))
