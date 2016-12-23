> docs.python.org/3/reference/grammar.html

```
expr: 		term (('+'|'-') term)*
term: 		factor (('*'|'/'|'%'|'//') factor)*
factor: 	('+'|'-') factor | power
power:		atom_expr ['^' factor]
atom_expr:	atom ('('[arglist]')')*
atom:		'('expr')' | IDENTIFIER | FLOAT | INTEGER 
arglist:	expr (',' expr)*
```
