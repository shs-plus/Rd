import sys
import tkinter.messagebox as mes
import json

class Settings:
    def __init__(self):
        try:
            with open('settings.json') as f:
                settings = json.load(f)
        except FileNotFoundError:
            mes.showerror('Error', 'settings.json not found, using default settings')
            settings = {}
        except json.JSONDecodeError:
            mes.showerror('Error', 'Invalid settings.json: JSON decode error')
            sys.exit(1)

        # Set default values
        settings.setdefault('geometry', '210x100')
        settings.setdefault('n', 35)
        settings.setdefault('rec', 0.5)
        settings.setdefault('debug', False)
        settings.setdefault('exception', [])

        # Assign settings to instance variables
        self.geometry = settings['geometry']
        self.n = settings['n']
        self.rec = settings['rec']
        self.debug = settings['debug']
        self.exception = settings['exception']
        self.title = "Rd 2"
        self.copyright = "Copyright (c) SHS Plus \n GPL v3"