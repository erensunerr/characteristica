# Generated from characteristica.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .characteristicaParser import characteristicaParser
else:
    from characteristicaParser import characteristicaParser

# This class defines a complete generic visitor for a parse tree produced by characteristicaParser.

class characteristicaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by characteristicaParser#prog.
    def visitProg(self, ctx:characteristicaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by characteristicaParser#impr.
    def visitImpr(self, ctx:characteristicaParser.ImprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by characteristicaParser#stat.
    def visitStat(self, ctx:characteristicaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by characteristicaParser#axiom.
    def visitAxiom(self, ctx:characteristicaParser.AxiomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by characteristicaParser#tacticCall.
    def visitTacticCall(self, ctx:characteristicaParser.TacticCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by characteristicaParser#tactic.
    def visitTactic(self, ctx:characteristicaParser.TacticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by characteristicaParser#arg.
    def visitArg(self, ctx:characteristicaParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by characteristicaParser#args.
    def visitArgs(self, ctx:characteristicaParser.ArgsContext):
        return self.visitChildren(ctx)



del characteristicaParser