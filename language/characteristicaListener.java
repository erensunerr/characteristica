// Generated from characteristica.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link characteristicaParser}.
 */
public interface characteristicaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link characteristicaParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(characteristicaParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link characteristicaParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(characteristicaParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link characteristicaParser#impr}.
	 * @param ctx the parse tree
	 */
	void enterImpr(characteristicaParser.ImprContext ctx);
	/**
	 * Exit a parse tree produced by {@link characteristicaParser#impr}.
	 * @param ctx the parse tree
	 */
	void exitImpr(characteristicaParser.ImprContext ctx);
	/**
	 * Enter a parse tree produced by {@link characteristicaParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(characteristicaParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link characteristicaParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(characteristicaParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link characteristicaParser#axiom}.
	 * @param ctx the parse tree
	 */
	void enterAxiom(characteristicaParser.AxiomContext ctx);
	/**
	 * Exit a parse tree produced by {@link characteristicaParser#axiom}.
	 * @param ctx the parse tree
	 */
	void exitAxiom(characteristicaParser.AxiomContext ctx);
	/**
	 * Enter a parse tree produced by {@link characteristicaParser#tacticCall}.
	 * @param ctx the parse tree
	 */
	void enterTacticCall(characteristicaParser.TacticCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link characteristicaParser#tacticCall}.
	 * @param ctx the parse tree
	 */
	void exitTacticCall(characteristicaParser.TacticCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link characteristicaParser#tactic}.
	 * @param ctx the parse tree
	 */
	void enterTactic(characteristicaParser.TacticContext ctx);
	/**
	 * Exit a parse tree produced by {@link characteristicaParser#tactic}.
	 * @param ctx the parse tree
	 */
	void exitTactic(characteristicaParser.TacticContext ctx);
	/**
	 * Enter a parse tree produced by {@link characteristicaParser#arg}.
	 * @param ctx the parse tree
	 */
	void enterArg(characteristicaParser.ArgContext ctx);
	/**
	 * Exit a parse tree produced by {@link characteristicaParser#arg}.
	 * @param ctx the parse tree
	 */
	void exitArg(characteristicaParser.ArgContext ctx);
	/**
	 * Enter a parse tree produced by {@link characteristicaParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(characteristicaParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link characteristicaParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(characteristicaParser.ArgsContext ctx);
}