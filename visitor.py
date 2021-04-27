from language.characteristicaVisitor import characteristicaVisitor
from internals.utils import logger
from internals.statement import Statement
from internals.tactic import TacticCall, Tactic
from antlr4 import FileStream, CommonTokenStream
from language.characteristicaLexer import characteristicaLexer
from language.characteristicaParser import characteristicaParser

class CustomVisitor(characteristicaVisitor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.statDict = {}
        self.tcList = []
        self.tacticDict = {}

    def visitImpr(self, ctx):
        filename = ctx.lib.text
        logger.debug(f"Importing {filename}.")
        fs = FileStream(filename)
        lex = characteristicaLexer(fs)
        tokenst = CommonTokenStream(lex)
        parser = characteristicaParser(tokenst)
        tree = parser.prog()
        self.visit(tree)
    
    def visitStat(self, ctx):
        statName = ctx.NAME().getText()
        statLiteral = ctx.STATEMENT().getText()
        logger.debug(f"Visited statement: {statName}.")
        if statName in self.statDict.keys():
            logger.warning(f"Redefined {statName}.")
        s = Statement(statLiteral, statName)
        self.statDict[statName] = s
        return s

    def visitAxiom(self, ctx):
        axName = ctx.NAME().getText()
        logger.debug(f"Visited axiom: {axName}")
        self.statDict[axName].isVerified = True
        return self.statDict[axName]
    
    def visitTacticCall(self, ctx):
        tacName = ctx.NAME().getText()
        if not tacName in self.tacticDict.keys():
            logger.warning(f"Calling undefined tactic {tacName}.")
            return
        tc = TacticCall(
            self.tacticDict[tacName],
            [x.getText() for x in ctx.variables.arg()],
            [self.statDict[x.getText()] for x in ctx.requirements.arg()],
            [self.statDict[x.getText()] for x in ctx.results.arg()]
        )        
        self.tcList += [tc]
        return tc
    
    def visitTactic(self, ctx):
        tc = ctx.tacticCall()
        tacName = tc.NAME().getText()
        t = Tactic( 
                tacName,
                [x.getText() for x in tc.variables.arg()],
                [self.statDict[x.getText()] for x in tc.requirements.arg()],
                [self.statDict[x.getText()] for x in tc.results.arg()]
                )
        self.tacticDict[tacName] = t
        return t