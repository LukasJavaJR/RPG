import time

class Spell:
    def __init__(self, spell_name, mana_cost, dmg, cast):
        self.spell_name = spell_name
        self.mana_cost = mana_cost
        self.damage = dmg
        self.casting_time = cast

    def cast(self, casting_time):
        print("───────────────────────────────")
        print("CASTING:")
        for i in range(0, int(casting_time)):
            print("▢ ", end="", flush=True)
            time.sleep(0.5)
        print("")