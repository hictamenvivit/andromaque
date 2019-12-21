# coding: utf-8

import re
from models import *
from utils import *


    

def process(title):

    with open('{}.txt'.format(title), 'r') as f:
        lines = f.readlines()

    with open("persos.json", "r") as f:
        all_persos = json.load(f)

    persos = all_persos[title]

    piece = Piece(title=title)
    current_acte = None
    current_character = None
    current_scene = None
    skip = False

    
    for current_line in lines:
        cl = sanitize(current_line)
        # print(cl)
        if skip:
            skip = False
            continue
        if not cl:
            continue

        try:
            acte_number = roman_digits_to_int(find_acte(cl))
            print("Found acte %d" % acte_number)
            current_acte = Acte(number=acte_number)
            piece.actes.append(current_acte)
            continue
        except ValueError:
            pass

        try:
            scene_number = roman_digits_to_int(find_scene(cl))
            print("Found scene %d" % scene_number)
            skip = True
            current_scene = Scene(number=scene_number)
            current_acte.scenes.append(current_scene)
            continue
        except ValueError:
            pass

        try:
            c = find_character(cl, persos)
            current_character = c
            continue
        except ValueError:
            pass
        current_scene.verses.append(Vers(character=current_character, content=cl))
    return piece
        
           
andromaque = process('Andromaque')
britannicus = process("Britannicus")

