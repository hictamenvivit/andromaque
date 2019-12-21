import json
import re
from utils import *

class Vers:
    def __init__(self, character, content):
        self.character = character
        self.content = content
    def __str__(self):
        return "{} : {}".format(self.character, self.content)


class Piece:
    def __init__(self, title):
        self.title = title
        self.actes = []

    @property
    def verses(self):
        return [v for a in self.actes for v in a.verses]

class Acte:
    def __init__(self, number):
        self.scenes = []
        self.number = number

    @property
    def verses(self):
        return [v for s in self.scenes for v in s.verses]

class Scene:
    def __init__(self, number):
        self.verses = []
        self.number = number


def find_character(line, persos):
    candidate = sanitize(line.replace('.', ''))
    if candidate in persos:
        return candidate
    raise ValueError("Not a character : %s" % candidate)


def find_scene(string):
    sanitized = sanitize(string.replace('.', ''))
    regex = "S(CÈNE|cène) ([\w,È,\d]*)"
    try:
        return re.search(regex, sanitized).group(2)
    except AttributeError:
        raise ValueError("Not a scene: %s" % string)

def find_acte(string):
    sanitized = sanitize(string.replace('.', ''))
    regex = "ACTE ([\w]*)"
    try:
        return re.search(regex, sanitized).group(1)
    except AttributeError:
        raise ValueError("Not an acte: %s" % string)