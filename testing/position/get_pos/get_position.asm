.ORIG x3000

;LD R2  ; stores the x y,z, values
;LD R3 
;LD R4
TRAP x34
add r2 , r2, #0
add r3 , r3, #0
add r4, r4, #0

TRAP x40
HALT



.END