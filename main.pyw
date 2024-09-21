# Copyright (C) 2024 Colin Wang
# License: GPL v3
# Description: A random choice generator
# Github: https://github.com/shs-plus/Rd

import tkinter as tk
import json
import random
import logging
import sys
import tkinter.messagebox as mes
import itertools

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
settings.setdefault('coef', .5)
settings.setdefault('debug', False)
settings.setdefault('exception', [])
settings['copyright'] = "Copyright (c) colinwang1703 \n GPL v3"
DEBUG = settings['debug']
logging.basicConfig(filename='runtime.log', filemode='w', format='[%(levelname)s] %(message)s', level=logging.WARNING)
if DEBUG:
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('Debugging mode enabled')

window = tk.Tk()
window.title(settings['title'])
window.attributes('-topmost', True)
window.geometry(settings['geometry'])
window.resizable(False, False)

label = tk.Label(window, text=settings['copyright'])

def random_choice():
    '''
    A different choosing algorithm.
    For each iteration, normalize the probabilities, choose one, then multiply the probability of the choosed one by .5 (for example)
    Then the results would be more mixed together, rather than chunks of 35 (for example) pieced together
    '''
    n = dict(zip(set(range(1, settings['n'] + 1)) - set(settings['exception']), itertools.repeat(1)))
    logging.debug(f'Setting n')
    while True:
        t = sum(n)
        for p in n:
            n[p] /= t
        yield (p := random.choices(list(n), list(n.values()))[0])
        n[p] *= settings['coef']
        logging.debug(f'Random choice: {p}')
        label['text'] = p

ch = random_choice()

button = tk.Button(window, text="Random Choice", command=lambda: next(ch))
button.place(relx=0.5, rely=0.3, anchor='center')
label.place(relx=0.5, rely=0.7, anchor='center')
window.mainloop()

logging.debug('Exiting')