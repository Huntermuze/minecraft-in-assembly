from memory import Registers, reg_read, reg_write
import os

if os.name == "nt":
    import msvcrt
else:
    from getch import getch


def get_world_height(mc):
    """
    Reads the two 16-bit integers stored in R5 and R6, representing x and z respectively, and 
    passes them to the mcpi getHeight() method, returning the world height at those coordinates.
    Stores the final result in R5.
    """

    x = reg_read(Registers.R5)
    z = reg_read(Registers.R6)

    # Convert from unsigned int to 16-bit signed int.
    x = (x + 2**15) % 2**16 - 2**15
    z = (z + 2**15) % 2**16 - 2**15

    y_value = mc.getHeight(x, z)

    # Write the y_value to register 5.
    reg_write(Registers.R5, y_value)
