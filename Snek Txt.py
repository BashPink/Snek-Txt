# -----------------------------------------------------------
# Snek Txt is a free and open source text editor for use, learn from, or modify
# No restriction is placed on the usage of Snek Txt for any purpose.
#
# Created by Aaron Kincer, 2022
# Released under GNU Public License (GPL)
# email aaron.kincer@yahoo.com
# -----------------------------------------------------------
# Version History:
# 1.0.0 - Initial Release (5/6/2022)
# -----------------------------------------------------------
# Known Issues and things to fix
# No way to change Font size
# Screen is not resizable
# God, it's ugly
# -----------------------------------------------------------

import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog

# Global Variables and Program Information
version = "1.0.0"

# Main window
window_main = tk.Tk()
window_main.title("Snek Txt v" + version)     # Change Title from Tk to Snek Txt
window_main.resizable(True, True)             # Set window resizable to true, This doesnt change the size of the grid
text = tk.Text(window_main)
text.grid()


# Save file method
def save_as():
    global text
    t = text.get("1.0", "end-1c")
    save_location = tkinter.filedialog.asksaveasfilename()
    file_1 = open(save_location, "w+")
    file_1.write(t)
    file_1.close()
    
btn_save = tk.Button(window_main, text="Save", command=save_as)
btn_save.grid()

# Event loop
window_main.mainloop()