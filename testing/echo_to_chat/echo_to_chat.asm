.ORIG x3000
LEA R1, store_message

LEA R0, user_input
trap x40 ; print all register values
trap x22 ; output string

LOOP    trap x20 ; gets the next character of the input
        trap x21 ; output character to console to see what you're typing
        STR R0, R1, #0 ; store current character in R0 in R1 of offset #0
        ADD R1, R1, #1 ; increment R1 by 1 to allow allocation of the current character
        ADD R0, R0, #-13 ; ASCII code of ENTER key is #13, therefore we will get zero by adding -13 to it
        BRz OUTSIDE ; if the previous line is 0, then the message is finished
        BRnp LOOP ; if the previous line isnt 0, then the message is not finished and must move to the next character

OUTSIDE trap x40 ; print all register values
                 ; NOTE: R0 will be 0 if message is outputted correctly (meaning last character entered was the ENTER key)
                 ;       R1 will be the original value of R1 + the length of the outputted message if outputted correctly (space and enter included)
        LEA R0, output_message 
        trap x22 ; output string

        LEA R0, store_message
        trap x22 ; output string
        trap x30 ; call the custom trap for the echo python function

        LEA R0, empty_line
        trap x22 ; output string
        trap x25 ; halt

user_input .stringz "\n\nPlease enter a message to have outputted: "
output_message .stringz "\nYour message is: " 
empty_line .stringz "\nCheck minecraft to see the message in game as well. \n"
store_message .blkw #99 ; allocate some memory to store the message

.END
