#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import random
from colors import blue

threat_list = (
    'Zorgon the Conqueror',
    "The Hive Armada",
    "Rogue Captain",
    "Space Pirates",
    "Cyber Zombies",
    "Alien Brain Worm"
)

wants_to_list = (
    "Destroy / Corrupt",
    "Steal / Capture",
    "Bond With"
    "Protect / Empower",
    "Build / Synthesize",
    "Pacify / Occupy"
)

the_list = (
    "Space Pirate King/Queen",
    "Void Crystals",
    "Star Dreadnought",
    "Quantum Tunnel",
    "Ancient Space Ruin",
    "Alien Artifact",
)

which_will_list = (
    "Destroy a Solar System",
    "Reverse Time",
    "Enslave a Planet",
    "Start a War / Invasion",
    "Rip a Hole in Reality",
    "Fix Everything"
)

if __name__ == '__main__':
    nb = 1
    if len(sys.argv) > 1:
        nb = int(sys.argv[1])
    for _ in range(nb):
        print "A threat...\n%s wants to %s the %s which will %s" % (
            blue(random.choice(threat_list)),
            blue(random.choice(wants_to_list)),
            blue(random.choice(the_list)),
            blue(random.choice(which_will_list))
            )
        print 20 * "-"
