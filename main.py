from language.characteristicaLexer import characteristicaLexer
from language.characteristicaParser import characteristicaParser
from visitor import CustomVisitor
from antlr4 import FileStream, CommonTokenStream
import sys
from internals.proofVerify import *

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cv = CustomVisitor()
        fst = FileStream(sys.argv[1])
        lex = characteristicaLexer(fst)
        tokenst = CommonTokenStream(lex)
        parser = characteristicaParser(tokenst)
        tree = parser.prog()
        cv.visit(tree)
        tcAxList = tcList_to_tcAxList(cv.tcList)
        verify(tcAxList)
        for stat in cv.statDict.values():
            print(f"{stat} {stat.isVerified}")

    

