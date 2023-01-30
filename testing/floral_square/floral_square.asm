.orig x3000

clear_all
and r0, r0, #0  ; reserve for output string
and r1, r1, #0  ; store numbers
and r2, r2, #0  ; store x
and r3, r3, #0  ; store y
and r4, r4, #0  ; store z
and r5, r5, #0  ; store numbers/mem addr
and r6, r6, #0  ; store mem addr
and r7, r7, #0  ; reserve for subroutines


welcome_str .stringz "\nFloral Square\n"
lea r0, welcome_str
trap x22

; load length into r1
fixed_length .fill #11      ; USER: Change this value to set arbitrary length (L)
ld r1, fixed_length

length_str .stringz "Square length stored in R1\n"
lea r0, length_str
trap x22
trap x40


; get player pos
trap x34
player_pos_str .stringz "Player pos stored in R2, R3, R4\n"
lea r0, player_pos_str
trap x22
trap x40

; get least x and z for square start
; divide length by 2
subtract_2
add r5, r5, #1
add r1, r1, #-2
brp subtract_2
add r5, r5, #-1
; negate r5
not r5, r5
add r5, r5, #1
; subtract (square length / 2) from x and z
add r2, r2, r5  ; least x
add r4, r4, r5  ; least z

start_vec3_str .stringz "Start vec3 stored in R2, R3, R4\n"
lea r0, start_vec3_str
trap x22
trap x40

; air out cubic area as per Halil's request
; store start vec3 mem addr at R5
start_vec3 .blkw 3
lea r5, start_vec3
; store x1, y1, z1
str r2, r5, #0
str r3, r5, #1
str r4, r5, #2
; store end vec3 mem addr at R6
end_vec3 .blkw 3
lea r6, end_vec3
; load square length
ld r1, fixed_length
; calc end x
add r2, r2, r1
add r3, r3, r1
add r4, r4, r1
; store x2, y2, z2
str r2, r6, #0
str r3, r6, #1
str r4, r6, #2
end_vec3_mem .stringz "Start, end vec3's stored in memory at R5, R6\n"
lea r0, end_vec3_mem
trap x22
trap x40

; load air block id
air_id .fill #0
ld r1, air_id
; air out cube
trap x37    ; set blocks
aired_str .stringz "Cubic area aired out\n"
lea r0, aired_str
trap x22

; re-load starting x, y, z into r2, r3, r4
ldr r2, r5, #0
ldr r3, r5, #1
ldr r4, r5, #2
; get values for flower_id and grass_id
flower_id .fill #37
grass_id .fill #2

; store loop length in memory
ld r5, fixed_length
add r5, r5, #-1
loop_len .blkw 1
sti, r5, loop_len

pos_x_str .stringz "Setting blocks...\n"
lea r0, pos_x_str
trap x22

set_blocks_pos_x
add r3, r3, #-1
ld r1, grass_id
trap x32
add r3, r3, #1
ld r1, flower_id
trap x32
add r2, r2, #1
add r5, r5, #-1
brp set_blocks_pos_x

pos_x_str .stringz "Blocks set in positive x direction.\n"
lea r0, pos_x_str
trap x22
trap x40

ldi r5, loop_len
set_blocks_pos_z
add r3, r3, #-1
ld r1, grass_id
trap x32
add r3, r3, #1
ld r1, flower_id
trap x32
add r4, r4, #1
add r5, r5, #-1
brp set_blocks_pos_z

pos_z_str .stringz "Blocks set in positive z direction.\n"
lea r0, pos_z_str
trap x22
trap x40

ldi r5, loop_len
set_blocks_neg_x
add r3, r3, #-1
ld r1, grass_id
trap x32
add r3, r3, #1
ld r1, flower_id
trap x32
add r2, r2, #-1
add r5, r5, #-1
brp set_blocks_neg_x

neg_x_str .stringz "Blocks set in negative x direction.\n"
lea r0, neg_x_str
trap x22
trap x40

ldi r5, loop_len
set_blocks_neg_z
add r3, r3, #-1
ld r1, grass_id
trap x32
add r3, r3, #1
ld r1, flower_id
trap x32
add r4, r4, #-1
add r5, r5, #-1
brp set_blocks_neg_z

neg_z_str .stringz "Blocks set in negative z direction.\n"
lea r0, neg_z_str
trap x22
trap x40

floral_done_str .stringz "Floral square has been created!\n\nFinal values in registers:\n"
lea r0, floral_done_str
trap x22
trap x40

; halt program
trap x25
.end