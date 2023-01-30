from memory import mem_read, mem_write, Registers, reg_read, reg_write
from utils import sign_extend
import os
if os.name == "nt":
    import msvcrt
else:
    from getch import getch


def echo_to_chat(mc):
    message_to_chat = '' # empty string
    for i in range(reg_read(Registers.R0), 2**16): # Loop through every character in the string contained in R0 (store_message)
        ch = mem_read(i) # Using mem_read function to convert register character to the correct ASCII character
        if ch == 0: # Breaking condition (if ch is null)
            break
        message_to_chat += chr(ch) # Append current character to string
    message_to_chat = message_to_chat[:-1] # This is done to remove the 'enter' character that is counted as part of the string (weird bug with mc.postToChat)
    mc.postToChat(message_to_chat) # post to minecraft
