from inventory import gold
import random 

class Npc:
    def __init__(self, name, hp, dmg, g):
        self.npc_name = name
        self.npc_hp = hp
        self.npc_attack = dmg
        self.npc_gold_reward = g