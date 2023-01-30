.orig x3000


clear               
and r0, r0, #0  ; reserve for output string
and r1, r1, #0  ; store block ID
and r2, r2, #0  ; store x
and r3, r3, #0  ; store y
and r4, r4, #0  ; store z
and r5, r5, #0
and r6, r6, #0
and r7, r7, #0  ; reserve for subroutines


; print initial message
init_str            .stringz "\nTesting get/set blocks.\n"
lea r0, init_str
trap x22


; get player pos
trap x34                ; x,y,z gets stored in r2,r3,r4
lea r0, get_pos_str     ; load get_pos_str into r0
trap x22                ; print get_pos_str
get_pos_str         .stringz "Current player vec3 (x, y, z) loaded into R2, R3, R4.\n"
jsr print_registers     ; print values in all registers

add r3, r3, #-1         ; decrement y-value to get tile below player
lea r0, y_decremented_str
trap x22
y_decremented_str   .stringz "y-value decremented by one to get vec3 beneath player.\n"

; get block id
trap x31
lea r0, get_block_str
trap x22
get_block_str       .stringz "Current block ID stored in R1.\n"
jsr print_registers

add r1, r1, #1      ; change block id 
lea r0, increment_block_str
trap x22
increment_block_str .stringz "Block ID incremented by 1.\n"
lea r0, new_block_str
trap x22
new_block_str       .stringz "New block ID stored in R1.\n"
jsr print_registers

; set different block underneath player
trap x32
lea r0, set_block_str
trap x22
set_block_str       .stringz "New block set in Minecraft world.\n------------------\n"
br end_program

; SUBROUTINES
print_registers
trap x40
ret


end_program
trap x25    ; halt

.end