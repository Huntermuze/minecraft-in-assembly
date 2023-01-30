

.orig x3000

trap x34 ; calls the get position trap, and stores the x,y,z values into r2,r3,r4 respectively
trap x40
LEA R0, user_input
trap x22

jsr LOOP

LOOP    trap x20  ;code taken from the echo function to read characters from user, following comments also taken from file for convinience
        trap x21 
        STR R0, R1, #0 ; store current character in R0 in R1 of offset #0
        ADD R1, R1, #1 ; increment offset by #1 ready to store next character
        ADD R0, R0, #-13 ; ASCII code of ENTER key is #13, therefore we will get zero by adding -13 to it
        BRZ STORE1
        BRnp LOOP ; if the previous line isnt 0, then the message is not finished and must move to the next character



STORE1
add r2, r2, R1 ; adds the values into the registers 
add r3, r3, R1
add r4, r4, r1




trap x35 ; calls itself to function
trap x40


user_input .stringz "\n\n This program will count the amount of characters you type, and teleport the player that many spaces in the x,y,z axis.\n\n Hit enter when you finish typing:"

halt
.end
