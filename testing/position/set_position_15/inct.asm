.ORIG x3000


trap x34 ; calls get position trap, stores x,y&z values in r2,r3 and r4
trap x40
add r2, r2, #15 ;adds 15 units to the values 
add r3, r3, #15
add r4, r4, #15

trap x36; returns the values into the python file and teleports the player in minecraft
trap x40
HALT
.END