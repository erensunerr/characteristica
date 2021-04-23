// Generated from /Users/reg/Documents/repos/characteristica/language/characteristica.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class characteristicaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, COMMENT=9, 
		WS=10, STATEMENT=11, NAME=12, COMMA=13;
	public static final int
		RULE_prog = 0, RULE_impr = 1, RULE_stat = 2, RULE_axiom = 3, RULE_tactic = 4, 
		RULE_tacticCall = 5, RULE_arg = 6, RULE_args = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "impr", "stat", "axiom", "tactic", "tacticCall", "arg", "args"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'import'", "'\"'", "';'", "'stat'", "'axiom'", "'tactic'", "'('", 
			"')'", null, null, null, null, "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "COMMENT", "WS", 
			"STATEMENT", "NAME", "COMMA"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "characteristica.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public characteristicaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(characteristicaParser.EOF, 0); }
		public List<ImprContext> impr() {
			return getRuleContexts(ImprContext.class);
		}
		public ImprContext impr(int i) {
			return getRuleContext(ImprContext.class,i);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public List<AxiomContext> axiom() {
			return getRuleContexts(AxiomContext.class);
		}
		public AxiomContext axiom(int i) {
			return getRuleContext(AxiomContext.class,i);
		}
		public List<TacticContext> tactic() {
			return getRuleContexts(TacticContext.class);
		}
		public TacticContext tactic(int i) {
			return getRuleContext(TacticContext.class,i);
		}
		public List<TacticCallContext> tacticCall() {
			return getRuleContexts(TacticCallContext.class);
		}
		public TacticCallContext tacticCall(int i) {
			return getRuleContext(TacticCallContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(21); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(21);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__0:
					{
					setState(16);
					impr();
					}
					break;
				case T__3:
					{
					setState(17);
					stat();
					}
					break;
				case T__4:
					{
					setState(18);
					axiom();
					}
					break;
				case T__5:
					{
					setState(19);
					tactic();
					}
					break;
				case NAME:
					{
					setState(20);
					tacticCall();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(23); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << NAME))) != 0) );
			setState(25);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImprContext extends ParserRuleContext {
		public Token lib;
		public TerminalNode NAME() { return getToken(characteristicaParser.NAME, 0); }
		public ImprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_impr; }
	}

	public final ImprContext impr() throws RecognitionException {
		ImprContext _localctx = new ImprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_impr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			match(T__0);
			setState(28);
			match(T__1);
			setState(29);
			((ImprContext)_localctx).lib = match(NAME);
			setState(30);
			match(T__1);
			setState(31);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(characteristicaParser.NAME, 0); }
		public TerminalNode STATEMENT() { return getToken(characteristicaParser.STATEMENT, 0); }
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(T__3);
			setState(34);
			match(NAME);
			setState(35);
			match(STATEMENT);
			setState(36);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AxiomContext extends ParserRuleContext {
		public ArgsContext toAssume;
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public AxiomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_axiom; }
	}

	public final AxiomContext axiom() throws RecognitionException {
		AxiomContext _localctx = new AxiomContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_axiom);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(T__4);
			setState(39);
			((AxiomContext)_localctx).toAssume = args();
			setState(40);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TacticContext extends ParserRuleContext {
		public TacticCallContext tacticCall() {
			return getRuleContext(TacticCallContext.class,0);
		}
		public TacticContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tactic; }
	}

	public final TacticContext tactic() throws RecognitionException {
		TacticContext _localctx = new TacticContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_tactic);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(T__5);
			setState(43);
			tacticCall();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TacticCallContext extends ParserRuleContext {
		public ArgsContext variables;
		public ArgsContext requirements;
		public ArgsContext results;
		public TerminalNode NAME() { return getToken(characteristicaParser.NAME, 0); }
		public List<ArgsContext> args() {
			return getRuleContexts(ArgsContext.class);
		}
		public ArgsContext args(int i) {
			return getRuleContext(ArgsContext.class,i);
		}
		public TacticCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tacticCall; }
	}

	public final TacticCallContext tacticCall() throws RecognitionException {
		TacticCallContext _localctx = new TacticCallContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tacticCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(NAME);
			setState(46);
			match(T__6);
			setState(47);
			((TacticCallContext)_localctx).variables = args();
			setState(48);
			match(T__7);
			setState(49);
			match(T__6);
			setState(50);
			((TacticCallContext)_localctx).requirements = args();
			setState(51);
			match(T__7);
			setState(52);
			match(T__6);
			setState(53);
			((TacticCallContext)_localctx).results = args();
			setState(54);
			match(T__7);
			setState(55);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(characteristicaParser.NAME, 0); }
		public TerminalNode STATEMENT() { return getToken(characteristicaParser.STATEMENT, 0); }
		public ArgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg; }
	}

	public final ArgContext arg() throws RecognitionException {
		ArgContext _localctx = new ArgContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_arg);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			_la = _input.LA(1);
			if ( !(_la==STATEMENT || _la==NAME) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgsContext extends ParserRuleContext {
		public List<ArgContext> arg() {
			return getRuleContexts(ArgContext.class);
		}
		public ArgContext arg(int i) {
			return getRuleContext(ArgContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(characteristicaParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(characteristicaParser.COMMA, i);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_args);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			arg();
			setState(64);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(60);
					match(COMMA);
					setState(61);
					arg();
					}
					} 
				}
				setState(66);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17F\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2"+
		"\6\2\30\n\2\r\2\16\2\31\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3"+
		"\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\7\tA\n\t\f\t\16\tD\13\t\3\t\3B\2\n\2"+
		"\4\6\b\n\f\16\20\2\3\3\2\r\16\2C\2\27\3\2\2\2\4\35\3\2\2\2\6#\3\2\2\2"+
		"\b(\3\2\2\2\n,\3\2\2\2\f/\3\2\2\2\16;\3\2\2\2\20=\3\2\2\2\22\30\5\4\3"+
		"\2\23\30\5\6\4\2\24\30\5\b\5\2\25\30\5\n\6\2\26\30\5\f\7\2\27\22\3\2\2"+
		"\2\27\23\3\2\2\2\27\24\3\2\2\2\27\25\3\2\2\2\27\26\3\2\2\2\30\31\3\2\2"+
		"\2\31\27\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33\34\7\2\2\3\34\3\3\2\2"+
		"\2\35\36\7\3\2\2\36\37\7\4\2\2\37 \7\16\2\2 !\7\4\2\2!\"\7\5\2\2\"\5\3"+
		"\2\2\2#$\7\6\2\2$%\7\16\2\2%&\7\r\2\2&\'\7\5\2\2\'\7\3\2\2\2()\7\7\2\2"+
		")*\5\20\t\2*+\7\5\2\2+\t\3\2\2\2,-\7\b\2\2-.\5\f\7\2.\13\3\2\2\2/\60\7"+
		"\16\2\2\60\61\7\t\2\2\61\62\5\20\t\2\62\63\7\n\2\2\63\64\7\t\2\2\64\65"+
		"\5\20\t\2\65\66\7\n\2\2\66\67\7\t\2\2\678\5\20\t\289\7\n\2\29:\7\5\2\2"+
		":\r\3\2\2\2;<\t\2\2\2<\17\3\2\2\2=B\5\16\b\2>?\7\17\2\2?A\5\16\b\2@>\3"+
		"\2\2\2AD\3\2\2\2BC\3\2\2\2B@\3\2\2\2C\21\3\2\2\2DB\3\2\2\2\5\27\31B";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}