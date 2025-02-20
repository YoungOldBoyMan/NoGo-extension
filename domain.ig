#blackactions
%action 1
:action occupy
:parameters (?x, ?y)
:precondition (open(?x,?y), NOT(suicideblack(?x, ?y)), NOT(killwhite(?x, ?y)))
:effect (black(?x,?y))
%-------------------------------
#whiteactions
%action 1
:action occupy
:parameters (?x, ?y)
:precondition (open(?x,?y), NOT(suicidewhite(?x, ?y)), NOT(killblack(?x, ?y)))
:effect (white(?x,?y))