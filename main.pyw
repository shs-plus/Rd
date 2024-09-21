# Rd 2
# Copyright (c) 2024 SHS Plus
# License: GPL v3
# Description: A random choice generator
# Github: https://github.com/shs-plus/Rd

import tkinter as tk
import logging
import settings
import core

s = settings.Settings()


logging.basicConfig(filename='runtime.log', filemode='w', format='[%(levelname)s] %(message)s', level=logging.WARNING)
if s.debug:
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('Debugging mode enabled')

window = tk.Tk()
window.title(s.title)
window.attributes('-topmost', True)
window.geometry(s.geometry)
window.resizable(False, False)
window.wm_attributes('-toolwindow', True)

label = tk.Label(window, text=s.copyright, font=("Arial", 8))

c = core.Core(s)
c.label = label

button = tk.Button(window, text="Random Choice", command=lambda: next(c.rc),
                   font=("Arial", 12),
                   relief="ridge", bd=3)
button.place(relx=0.5, rely=0.3, anchor='center')
label.place(relx=0.5, rely=0.7, anchor='center')
window.mainloop()

logging.debug('Exiting')