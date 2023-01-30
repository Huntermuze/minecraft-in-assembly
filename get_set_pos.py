from memory import mem_read, mem_write, Registers, reg_read, reg_write
from utils import sign_extend
import os
if os.name == "nt":
    import msvcrt
else:
    from getch import getch

import sys

from mcpi import minecraft


def get_pos(mc):

    x, y, z = mc.player.getTilePos()
    # print(f"x: {x}, y: {y}, z: {z}")      # Uncomment for debugging
    reg_write(Registers.R2, x)
    reg_write(Registers.R3, y)
    reg_write(Registers.R4, z)
    # pass v3.x ,y , z to get_posision tests somehow


def set_pos(mc):

    pos_x = reg_read(Registers.R2)  # reads registers for the int values,
    pos_y = reg_read(Registers.R3)
    pos_z = reg_read(Registers.R4)
    # Convert to signed 16-bit int
    pos_x = (pos_x + 2**15) % 2**16 - 2**15
    pos_y = (pos_y + 2**15) % 2**16 - 2**15
    pos_z = (pos_z + 2**15) % 2**16 - 2**15

    mc.player.setPos(pos_x, pos_y, pos_z)


def set_pos_15(mc):

    pos_x = reg_read(Registers.R2)  # reads registers for the int values,
    pos_y = reg_read(Registers.R3)
    pos_z = reg_read(Registers.R4)

    pos_x = (pos_x + 2**15) % 2**16 - 2**15
    pos_y = (pos_y + 2**15) % 2**16 - 2**15
    pos_z = (pos_z + 2**15) % 2**16 - 2**15
    mc.player.setPos(pos_x, pos_y, pos_z)
