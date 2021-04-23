# Generated from language/characteristica.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\6\nA\n\n\r\n\16")
        buf.write("\nB\3\n\5\nF\n\n\3\n\3\n\3\n\3\n\3\13\6\13M\n\13\r\13")
        buf.write("\16\13N\3\13\3\13\3\f\3\f\7\fU\n\f\f\f\16\fX\13\f\3\f")
        buf.write("\3\f\3\r\3\r\7\r^\n\r\f\r\16\ra\13\r\3\16\3\16\5BNV\2")
        buf.write("\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\3\2\5\5\2\13\f\17\17\"\"\4\2C\\c|\7\2\60")
        buf.write("\60\63;C\\aac|\2h\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5$\3\2\2\2\7&\3\2\2\2")
        buf.write("\t(\3\2\2\2\13-\3\2\2\2\r\63\3\2\2\2\17:\3\2\2\2\21<\3")
        buf.write("\2\2\2\23>\3\2\2\2\25L\3\2\2\2\27R\3\2\2\2\31[\3\2\2\2")
        buf.write("\33b\3\2\2\2\35\36\7k\2\2\36\37\7o\2\2\37 \7r\2\2 !\7")
        buf.write("q\2\2!\"\7t\2\2\"#\7v\2\2#\4\3\2\2\2$%\7$\2\2%\6\3\2\2")
        buf.write("\2&\'\7=\2\2\'\b\3\2\2\2()\7u\2\2)*\7v\2\2*+\7c\2\2+,")
        buf.write("\7v\2\2,\n\3\2\2\2-.\7c\2\2./\7z\2\2/\60\7k\2\2\60\61")
        buf.write("\7q\2\2\61\62\7o\2\2\62\f\3\2\2\2\63\64\7v\2\2\64\65\7")
        buf.write("c\2\2\65\66\7e\2\2\66\67\7v\2\2\678\7k\2\289\7e\2\29\16")
        buf.write("\3\2\2\2:;\7*\2\2;\20\3\2\2\2<=\7+\2\2=\22\3\2\2\2>@\7")
        buf.write("%\2\2?A\13\2\2\2@?\3\2\2\2AB\3\2\2\2BC\3\2\2\2B@\3\2\2")
        buf.write("\2CE\3\2\2\2DF\7\17\2\2ED\3\2\2\2EF\3\2\2\2FG\3\2\2\2")
        buf.write("GH\7\f\2\2HI\3\2\2\2IJ\b\n\2\2J\24\3\2\2\2KM\t\2\2\2L")
        buf.write("K\3\2\2\2MN\3\2\2\2NO\3\2\2\2NL\3\2\2\2OP\3\2\2\2PQ\b")
        buf.write("\13\2\2Q\26\3\2\2\2RV\7}\2\2SU\13\2\2\2TS\3\2\2\2UX\3")
        buf.write("\2\2\2VW\3\2\2\2VT\3\2\2\2WY\3\2\2\2XV\3\2\2\2YZ\7\177")
        buf.write("\2\2Z\30\3\2\2\2[_\t\3\2\2\\^\t\4\2\2]\\\3\2\2\2^a\3\2")
        buf.write("\2\2_]\3\2\2\2_`\3\2\2\2`\32\3\2\2\2a_\3\2\2\2bc\7.\2")
        buf.write("\2c\34\3\2\2\2\b\2BENV_\3\b\2\2")
        return buf.getvalue()


class characteristicaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    COMMENT = 9
    WS = 10
    STATEMENT = 11
    NAME = 12
    COMMA = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'\"'", "';'", "'stat'", "'axiom'", "'tactic'", 
            "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "WS", "STATEMENT", "NAME", "COMMA" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "COMMENT", "WS", "STATEMENT", "NAME", "COMMA" ]

    grammarFileName = "characteristica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


