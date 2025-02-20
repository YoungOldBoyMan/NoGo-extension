suicideblack = ((white(?x + 1, ?y) | 
(black(?x+1, ?y) white(?x +1, ?y+1) white(?x +1, ?y-1) white(?x + 2, ?y)) | 
(black(?x +2, ?y) (white(?x+2, ?y+1) white(?x+2, ?y-1)) | black(?x+2, ?y+1) white(?x+2, ?y+2) white(?x+1, ?y+1) | black(?x+2, ?y-1) white(?x+2, ?y-2) white(?x+1, ?y-1) ))

NU ER VI 2 UDE ^^^^^^^^^^^^^^^:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D


(black(?x+1, ?y+1) (white(?x +2, ?y+1) white(?x, ?y+1) white(?x + 1, ?y+2) | 

(black(?x+1, ?y-1) (white(?x, ?y-1) white(?x +1, ?y-2) white(?x + 2, ?y-1) | 



)





    white(?x - 1, ?y) 





    (white(?x, ?y+1) | 
    (black(?x, ?y+1) (white(?x +1, ?y+1) white(?x +1, ?y+2) white(?x - 1, ?y+1) | 
    (black(?x, ?y+2) white(?x+1, ?y+2))) 
)) 








white(?x, ?y-1))
 
)