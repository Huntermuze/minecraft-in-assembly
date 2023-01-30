            .ORIG x3000

            ; Load the x coordinate into R5, and the z coordinate in R6. Don't need to clear registers.
            LD R5, x_coord
            LD R6, z_coord

            ; Call the trap to obtain the world height with values in R5 & R6. Stores result in R5. Halt the program when complete.
            TRAP x33
            JSR print
            TRAP x25

            ; Print subroutine which prints the y-value stored in R5 out to console by first clearing R0, then copying R5's contents to R0.
print       AND R0, R0, #0
            ADD R0, R5, #0
            TRAP x26
            RET

            ; R5 = x, R6, = z. R5 = result.
x_coord     .FILL #78
z_coord     .FILL #-354

            .END

