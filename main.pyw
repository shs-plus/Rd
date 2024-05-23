# Copyright (C) 2024 Colin Wang
# License: GPL v3
# Description: A random choice generator
# Github: https://github.com/colinwang1703/rd/

import tkinter as tk
import json
import random
import logging
import sys
import tkinter.messagebox as mes

try:
    with open('settings.json') as f:
        settings = json.load(f)
except FileNotFoundError:
    mes.showerror('Error', 'settings.json not found, using default settings')
    settings = {}
except json.JSONDecodeError:
    mes.showerror('Error', 'Invalid settings.json: JSON decode error')
    sys.exit(1)

settings.setdefault('title', 'Rd')
settings.setdefault('geometry', '210x100')
settings.setdefault('n', 35)
settings.setdefault('debug', False)
settings.setdefault('exception', [])
settings['copyright'] = "Copyright (c) colinwang1703 \n GPL v3"
DEBUG = settings['debug']
logging.basicConfig(filename='runtime.log', filemode='w', format='[%(levelname)s] %(message)s', level=logging.WARNING)
if DEBUG:
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('Debugging mode enabled')

def set_n():
    global n
    n = set(range(1, settings['n'] + 1))
    for i in settings['exception']:
        n.remove(i)
    logging.debug(f'Setting n')

set_n()
window = tk.Tk()
window.title(settings['title'])
window.attributes('-topmost', True)
window.geometry(settings['geometry'])
window.resizable(False, False)

label = tk.Label(window, text=settings['copyright'])

def random_choice():
    global n
    if not n:
        set_n()
    p = random.choice(list(n))
    label['text'] = p
    n.remove(p)
    logging.debug(f'Random choice: {p}')

button = tk.Button(window, text="Random Choice", command=random_choice)
button.place(relx=0.5, rely=0.3, anchor='center')
label.place(relx=0.5, rely=0.7, anchor='center')
window.mainloop()

logging.debug('Exiting')