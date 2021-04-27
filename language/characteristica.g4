grammar characteristica;

prog        :
                (impr  | stat
                |axiom | tactic      
                |tacticCall)*
                EOF
            ;


impr        :   'import' '"' lib=IMPR_NAME '"' ';';
stat        :   'stat' NAME STATEMENT;
axiom       :   'axiom' NAME ';';

tacticCall  :   NAME
                '(' variables=args ')'
                '(' requirements=args ')'
                '(' results=args ')' ';'
            ;

tactic      :   'tactic' tacticCall;

arg         :   (NAME);
args        :   arg (COMMA arg)*?;

COMMENT     :   ('#' .+? '\r'? '\n') -> skip;
WS          :   [ \t\n\r]+? -> skip;
STATEMENT   :   '{' .*? '}' ';';
NAME        :   [a-zA-Z][a-zA-Z._1-9]*;
IMPR_NAME   :   [a-zA-Z][a-zA-Z._1-9/]*;
COMMA       :   ',';