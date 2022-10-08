#!/usr/bin/env python

from termcolor import colored
from pyfiglet import Figlet

def render_logo():
    f = Figlet(font='slant')
    print(colored(f.renderText("HTTP traffic logger"), 'yellow'))
