# Generated from language/characteristica.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\6\2\30\n\2\r\2\16\2\31")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\7\tA\n\t\f\t")
        buf.write("\16\tD\13\t\3\t\3B\2\n\2\4\6\b\n\f\16\20\2\3\3\2\r\16")
        buf.write("\2C\2\27\3\2\2\2\4\35\3\2\2\2\6#\3\2\2\2\b(\3\2\2\2\n")
        buf.write(",\3\2\2\2\f/\3\2\2\2\16;\3\2\2\2\20=\3\2\2\2\22\30\5\4")
        buf.write("\3\2\23\30\5\6\4\2\24\30\5\b\5\2\25\30\5\n\6\2\26\30\5")
        buf.write("\f\7\2\27\22\3\2\2\2\27\23\3\2\2\2\27\24\3\2\2\2\27\25")
        buf.write("\3\2\2\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31")
        buf.write("\32\3\2\2\2\32\33\3\2\2\2\33\34\7\2\2\3\34\3\3\2\2\2\35")
        buf.write("\36\7\3\2\2\36\37\7\4\2\2\37 \7\16\2\2 !\7\4\2\2!\"\7")
        buf.write("\5\2\2\"\5\3\2\2\2#$\7\6\2\2$%\7\16\2\2%&\7\r\2\2&\'\7")
        buf.write("\5\2\2\'\7\3\2\2\2()\7\7\2\2)*\5\20\t\2*+\7\5\2\2+\t\3")
        buf.write("\2\2\2,-\7\b\2\2-.\5\f\7\2.\13\3\2\2\2/\60\7\16\2\2\60")
        buf.write("\61\7\t\2\2\61\62\5\20\t\2\62\63\7\n\2\2\63\64\7\t\2\2")
        buf.write("\64\65\5\20\t\2\65\66\7\n\2\2\66\67\7\t\2\2\678\5\20\t")
        buf.write("\289\7\n\2\29:\7\5\2\2:\r\3\2\2\2;<\t\2\2\2<\17\3\2\2")
        buf.write("\2=B\5\16\b\2>?\7\17\2\2?A\5\16\b\2@>\3\2\2\2AD\3\2\2")
        buf.write("\2BC\3\2\2\2B@\3\2\2\2C\21\3\2\2\2DB\3\2\2\2\5\27\31B")
        return buf.getvalue()


class characteristicaParser ( Parser ):

    grammarFileName = "characteristica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'\"'", "';'", "'stat'", "'axiom'", 
                     "'tactic'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "WS", "STATEMENT", "NAME", 
                      "COMMA" ]

    RULE_prog = 0
    RULE_impr = 1
    RULE_stat = 2
    RULE_axiom = 3
    RULE_tactic = 4
    RULE_tacticCall = 5
    RULE_arg = 6
    RULE_args = 7

    ruleNames =  [ "prog", "impr", "stat", "axiom", "tactic", "tacticCall", 
                   "arg", "args" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    COMMENT=9
    WS=10
    STATEMENT=11
    NAME=12
    COMMA=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(characteristicaParser.EOF, 0)

        def impr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(characteristicaParser.ImprContext)
            else:
                return self.getTypedRuleContext(characteristicaParser.ImprContext,i)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(characteristicaParser.StatContext)
            else:
                return self.getTypedRuleContext(characteristicaParser.StatContext,i)


        def axiom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(characteristicaParser.AxiomContext)
            else:
                return self.getTypedRuleContext(characteristicaParser.AxiomContext,i)


        def tactic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(characteristicaParser.TacticContext)
            else:
                return self.getTypedRuleContext(characteristicaParser.TacticContext,i)


        def tacticCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(characteristicaParser.TacticCallContext)
            else:
                return self.getTypedRuleContext(characteristicaParser.TacticCallContext,i)


        def getRuleIndex(self):
            return characteristicaParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = characteristicaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [characteristicaParser.T__0]:
                    self.state = 16
                    self.impr()
                    pass
                elif token in [characteristicaParser.T__3]:
                    self.state = 17
                    self.stat()
                    pass
                elif token in [characteristicaParser.T__4]:
                    self.state = 18
                    self.axiom()
                    pass
                elif token in [characteristicaParser.T__5]:
                    self.state = 19
                    self.tactic()
                    pass
                elif token in [characteristicaParser.NAME]:
                    self.state = 20
                    self.tacticCall()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << characteristicaParser.T__0) | (1 << characteristicaParser.T__3) | (1 << characteristicaParser.T__4) | (1 << characteristicaParser.T__5) | (1 << characteristicaParser.NAME))) != 0)):
                    break

            self.state = 25
            self.match(characteristicaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lib = None # Token

        def NAME(self):
            return self.getToken(characteristicaParser.NAME, 0)

        def getRuleIndex(self):
            return characteristicaParser.RULE_impr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpr" ):
                return visitor.visitImpr(self)
            else:
                return visitor.visitChildren(self)




    def impr(self):

        localctx = characteristicaParser.ImprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_impr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(characteristicaParser.T__0)
            self.state = 28
            self.match(characteristicaParser.T__1)
            self.state = 29
            localctx.lib = self.match(characteristicaParser.NAME)
            self.state = 30
            self.match(characteristicaParser.T__1)
            self.state = 31
            self.match(characteristicaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(characteristicaParser.NAME, 0)

        def STATEMENT(self):
            return self.getToken(characteristicaParser.STATEMENT, 0)

        def getRuleIndex(self):
            return characteristicaParser.RULE_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = characteristicaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(characteristicaParser.T__3)
            self.state = 34
            self.match(characteristicaParser.NAME)
            self.state = 35
            self.match(characteristicaParser.STATEMENT)
            self.state = 36
            self.match(characteristicaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxiomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.toAssume = None # ArgsContext

        def args(self):
            return self.getTypedRuleContext(characteristicaParser.ArgsContext,0)


        def getRuleIndex(self):
            return characteristicaParser.RULE_axiom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAxiom" ):
                return visitor.visitAxiom(self)
            else:
                return visitor.visitChildren(self)




    def axiom(self):

        localctx = characteristicaParser.AxiomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_axiom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(characteristicaParser.T__4)
            self.state = 39
            localctx.toAssume = self.args()
            self.state = 40
            self.match(characteristicaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TacticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tacticCall(self):
            return self.getTypedRuleContext(characteristicaParser.TacticCallContext,0)


        def getRuleIndex(self):
            return characteristicaParser.RULE_tactic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTactic" ):
                return visitor.visitTactic(self)
            else:
                return visitor.visitChildren(self)




    def tactic(self):

        localctx = characteristicaParser.TacticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tactic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(characteristicaParser.T__5)
            self.state = 43
            self.tacticCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TacticCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.variables = None # ArgsContext
            self.requirements = None # ArgsContext
            self.results = None # ArgsContext

        def NAME(self):
            return self.getToken(characteristicaParser.NAME, 0)

        def args(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(characteristicaParser.ArgsContext)
            else:
                return self.getTypedRuleContext(characteristicaParser.ArgsContext,i)


        def getRuleIndex(self):
            return characteristicaParser.RULE_tacticCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTacticCall" ):
                return visitor.visitTacticCall(self)
            else:
                return visitor.visitChildren(self)




    def tacticCall(self):

        localctx = characteristicaParser.TacticCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tacticCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(characteristicaParser.NAME)
            self.state = 46
            self.match(characteristicaParser.T__6)
            self.state = 47
            localctx.variables = self.args()
            self.state = 48
            self.match(characteristicaParser.T__7)
            self.state = 49
            self.match(characteristicaParser.T__6)
            self.state = 50
            localctx.requirements = self.args()
            self.state = 51
            self.match(characteristicaParser.T__7)
            self.state = 52
            self.match(characteristicaParser.T__6)
            self.state = 53
            localctx.results = self.args()
            self.state = 54
            self.match(characteristicaParser.T__7)
            self.state = 55
            self.match(characteristicaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(characteristicaParser.NAME, 0)

        def STATEMENT(self):
            return self.getToken(characteristicaParser.STATEMENT, 0)

        def getRuleIndex(self):
            return characteristicaParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = characteristicaParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==characteristicaParser.STATEMENT or _la==characteristicaParser.NAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(characteristicaParser.ArgContext)
            else:
                return self.getTypedRuleContext(characteristicaParser.ArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(characteristicaParser.COMMA)
            else:
                return self.getToken(characteristicaParser.COMMA, i)

        def getRuleIndex(self):
            return characteristicaParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = characteristicaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.arg()
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 60
                    self.match(characteristicaParser.COMMA)
                    self.state = 61
                    self.arg() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





