> docs.python.org/3/reference/grammar.html

expr: 		term (('+'|'-') term)\*

term: 		factor (('\*'|'/'|'%'|'//') factor)\*

factor: 	('+'|'-') factor | power

power:		atom\_expr ['^' factor]

atom\_expr:	atom ('('[arglist]')')\*

atom:		'('expr')' | IDENTIFIER | FLOAT | INTEGER 

arglist:	expr (',' expr)\*
