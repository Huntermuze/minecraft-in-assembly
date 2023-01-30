from memory import mem_read, mem_write, Registers, reg_read, reg_write


def get_block(mc):
    """
    Writes block ID into R1. Reads x, y, z values from R2, R3, R4.
    """
    # Read x, y, z from R2, R3, R4
    x = reg_read(Registers.R2)
    y = reg_read(Registers.R3)
    z = reg_read(Registers.R4)
    # Convert to signed 16-bit int
    x = (x + 2**15) % 2**16 - 2**15
    y = (y + 2**15) % 2**16 - 2**15
    z = (z + 2**15) % 2**16 - 2**15
    # Get block ID
    id = mc.getBlock(x, y, z)
    # print(f"ID: {id}")        # Uncomment for debugging
    # Store id value in R1
    reg_write(Registers.R1, id)


def set_block(mc):
    """
    Sets block using R2, R3, R4 for vec3 and R1 for block ID. Reads x, y, z values as signed ints. Reads block ID value from R1.
    """
    # Read x, y, z from R2, R3, R4
    x = reg_read(Registers.R2)
    y = reg_read(Registers.R3)
    z = reg_read(Registers.R4)
    # Convert to signed 16-bit int
    x = (x + 2**15) % 2**16 - 2**15
    y = (y + 2**15) % 2**16 - 2**15
    z = (z + 2**15) % 2**16 - 2**15
    # Read id value in R1
    id = reg_read(Registers.R1)
    # Set block
    mc.setBlock(x, y, z, id)


def set_blocks(mc):
    """
    Sets blocks using R5, R6 for vec3's and R1 for block ID. Reads x1, y1, z1 values as signed ints staring from memory address in R5. Reads x2, y2, z2 values as signed ints starting from memory address in R6. Reads block ID value from R1.
    """
    # Read x1, y1, z1 starting from R5
    x1 = mem_read(reg_read(Registers.R5) + 0)
    y1 = mem_read(reg_read(Registers.R5) + 1)
    z1 = mem_read(reg_read(Registers.R5) + 2)
    # Convert to signed 16-bit int
    x1 = (x1 + 2**15) % 2**16 - 2**15
    y1 = (y1 + 2**15) % 2**16 - 2**15
    z1 = (z1 + 2**15) % 2**16 - 2**15
    # Read x2, y2, z2 starting from R6
    x2 = mem_read(reg_read(Registers.R6) + 0)
    y2 = mem_read(reg_read(Registers.R6) + 1)
    z2 = mem_read(reg_read(Registers.R6) + 2)
    # Convert to signed 16-bit int
    x2 = (x2 + 2**15) % 2**16 - 2**15
    y2 = (y2 + 2**15) % 2**16 - 2**15
    z2 = (z2 + 2**15) % 2**16 - 2**15
    # Read id value in R1
    id = reg_read(Registers.R1)
    # Set block
    mc.setBlocks(x1, y1, z1, x2, y2, z2, id)
