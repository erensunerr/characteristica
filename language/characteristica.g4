grammar characteristica;

prog        :   
                (impr  | stat
                |axiom | tactic      
                |tacticCall)+ 
                EOF
            ;


impr        :   'import' '"' lib=NAME '"' ';';
stat        :   'stat' NAME STATEMENT ';';
axiom       :   'axiom' toAssume=args ';';

tactic      :   'tactic' tacticCall;

tacticCall  :   NAME
                '(' variables=args ')'
                '(' requirements=args ')'
                '(' results=args ')' ';'
            ;

arg         :   (NAME | STATEMENT);
args        :   arg(COMMA arg)*?;



COMMENT     :   ('#' .+? '\r'? '\n') -> skip;
WS          :   [ \t\n\r]+? -> skip;
STATEMENT   :   '{' .*? '}';
NAME        :   [a-zA-Z][a-zA-Z._1-9]*;
COMMA       :   ',';


