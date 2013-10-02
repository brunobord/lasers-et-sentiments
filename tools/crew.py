#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random

style_choices = [
    "Alien",
    "Androïde",
    "Dangereux",
    "Prétentieux",
    "Intrépide",
    "Malin",
    "Sexy"
]

role_choices = [
    "Docteur",
    "Diplomate",
    "Ingénieur",
    "Explorateur",
    "Pilote",
    "Scientifique",
    "Soldat"
]

random.shuffle(style_choices)
random.shuffle(role_choices)
print "\n".join(["%s %s" % (role, style) for style, role in zip(style_choices, role_choices)])
