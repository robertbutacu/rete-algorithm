from src.Builder import Builder
from src.parser.Parser import Parser

if __name__ == "__main__":
    parser = Parser()
    builder = Builder()

    parsedFile = parser.parseFile("E:\\Projects\\turtle\\docs\\examples\\Blocchi.clp")

    print(builder.build(parsedFile))
