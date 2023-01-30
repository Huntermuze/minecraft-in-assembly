from memory import mem_read, mem_write, Registers, reg_read, reg_write
from utils import sign_extend
from mcpi import minecraft
import sys
import os
if os.name == "nt":
    import msvcrt
else:
    from getch import getch

# Import trap functions.
from block import get_block
from block import set_block
from block import set_blocks
from echo import echo_to_chat
from get_set_pos import get_pos, set_pos_15
from get_set_pos import set_pos
from world_height import get_world_height

_mc = minecraft.Minecraft.create()


class Halt(Exception):
    """Thrown to indicate HALT instruction has been executed."""
    pass


def _GETC():
    """get character from keyboard,
     character is not echoed onto the console. """
    if os.name == "nt":
        ch = msvcrt.getch()
    else:
        ch = getch()
    reg_write(Registers.R0, ord(ch))


def _OUT():
    """output a character"""
    sys.stdout.write(chr(reg_read(Registers.R0)))
    sys.stdout.flush()


def _PUTS():
    """output a word string"""
    for i in range(reg_read(Registers.R0), 2**16):
        ch = mem_read(i)
        if ch == 0:  # check if the char is not null then print this char
            break
        sys.stdout.write(chr(ch))
    sys.stdout.flush()  # equal to fflush() in c


def _IN():
    """input a single character, echoed onto the console"""
    sys.stdout.write("Enter a character: ")
    sys.stdout.flush()
    reg_write(Registers.R0, ord(sys.stdin.read(1)))


def _PUTSP():
    """output a byte string"""
    for i in range(reg_read(Registers.R0), 2**16):
        c = mem_read(i)
        if c == 0:
            break
        sys.stdout.write(chr(c & 0xFF))
        char = c >> 8
        if char:
            sys.stdout.write(chr(char))
    sys.stdout.flush()


def _HALT():
    """halt the program"""
    raise Halt()

# Import trap implementation functions from separate file(s) and invoke them within their respective trap.


def _ECHO_TO_CHAT():
    echo_to_chat(_mc)


def _GET_BLOCK():
    get_block(_mc)


def _SET_BLOCK():
    set_block(_mc)


def _SET_BLOCKS():
    set_blocks(_mc)


def _GET_HEIGHT():
    get_world_height(_mc)


def _GET_PLAYER_POS():
    get_pos(_mc)


def _SET_PLAYER_POS():
    set_pos(_mc)


def _SET_PLAYER_POS_15():
    set_pos_15(_mc)


def _OUT_NUMERIC():
    """output a number"""
    sys.stdout.write(str(reg_read(Registers.R0)))
    sys.stdout.flush()


def _PRINT_ALL_REG():
    """
    Prints values in all registers to the console; general register values (R1~R5) as integers, R0, R6, R7 & program counter as hex, flag as binary.
    """
    print("\n🖨  Current registers:")
    r0_val = reg_read(0)
    print(f"R0: {hex(r0_val)}")
    for i in range(1, 6):
        val = reg_read(i)
        print(f"R{i}: {val}")
    r6_val = reg_read(6)
    r7_val = reg_read(7)
    pc_val = reg_read(8)
    cond_val = reg_read(9)
    print(f"R6: {hex(r6_val)}")
    print(f"R7: {hex(r7_val)}")
    print(f"PC: {hex(pc_val)}")
    print(f"COND (nzp): {bin(cond_val)}\n")


class Traps:
    GETC = 0x20         # get character from keyboard
    OUT = 0x21          # output a character
    PUTS = 0x22         # output a word string
    IN = 0x23           # input a string
    PUTSP = 0x24        # output a byte string
    HALT = 0x25         # halt the program
    OUT_NUMERIC = 0x26  # output a number
    # MCPI
    ECHO_TO_CHAT = 0x30
    GET_BLOCK = 0x31
    SET_BLOCK = 0x32
    GET_HEIGHT = 0x33
    GET_PLAYER_POS = 0x34
    SET_PLAYER_POS = 0x35
    SET_PLAYER_POS_15 = 0X36
    SET_BLOCKS = 0x37
    # Debugging
    PRINT_ALL_REG = 0x40


_traps = {
    Traps.GETC: _GETC,
    Traps.OUT: _OUT,
    Traps.OUT_NUMERIC: _OUT_NUMERIC,
    Traps.PUTS: _PUTS,
    Traps.IN: _IN,
    Traps.PUTSP: _PUTSP,
    Traps.HALT: _HALT,
    # MCPI traps
    Traps.ECHO_TO_CHAT: _ECHO_TO_CHAT,
    Traps.GET_BLOCK: _GET_BLOCK,
    Traps.SET_BLOCK: _SET_BLOCK,
    Traps.SET_BLOCKS: _SET_BLOCKS,
    Traps.GET_HEIGHT: _GET_HEIGHT,
    Traps.GET_PLAYER_POS: _GET_PLAYER_POS,
    Traps.SET_PLAYER_POS: _SET_PLAYER_POS,
    Traps.PRINT_ALL_REG: _PRINT_ALL_REG,
    Traps.SET_PLAYER_POS_15: _SET_PLAYER_POS_15
}


def trap_routine(code):
    return _traps[code]
