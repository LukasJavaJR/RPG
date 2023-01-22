import random, time
from npc import Npc
from spell import Spell
from inventory import gold

# NPC LIST:
ogre = Npc("Ogre", 3200, random.randint(120, 190), 80)
wolf  = Npc("Wolf", 2600, random.randint(90, 140), 60)

npc_hp_list = [int(ogre.npc_hp), int(wolf.npc_hp)]

# ┌ ─ ┐ │ └ ┘ 🔥 ❄️ ❤️

def print_spellbook():
    print("SPELLBOOK:")
    print("1 - 🔥 Fireball")
    print("2 - ❄️  Frostbolt")

print("┌───────────────────────────────┐")
print("│ CÍL: ZÍSKAT ALESPOŇ 150 GOLDŮ │")
print("└───────────────────────────────┘")

game_run = True

while game_run:
    print("Máš: " + str(gold) + " goldů.")
    print("Vyber si enemy:")
    print("1 - Ogre")
    print("2 - Wolf")
    pick = int(input("Tvoje volba: "))

    if pick == 1:
        ogre.npc_hp = npc_hp_list[0]
        print("───────────────────────────────")
        print("Zvolil jsi OGRE: HP = ❤️  " + str(ogre.npc_hp))
        enemy_alive = True
        
        while enemy_alive:
            print_spellbook()
            spell_pick = int(input("Tvoje volba: "))

            if spell_pick == 1:
                fireball = Spell("Fireball", 155, random.randint(850, 1337), 6)
                ogre.npc_hp = ogre.npc_hp - fireball.damage
                fireball.cast(fireball.casting_time)
                print("🔥🔥🔥 Fireball hit for " + str(fireball.damage) + " 🔥🔥🔥")
                print("Remaining HP: ❤️  " + str(ogre.npc_hp))
                if ogre.npc_hp <= 0:
                    enemy_alive = False

            if spell_pick == 2:
                frostbolt  = Spell("Frostbolt", 110, random.randint(650, 1210), 4)
                ogre.npc_hp = ogre.npc_hp - frostbolt.damage
                frostbolt.cast(frostbolt.casting_time)
                print("❄️❄️❄️ Frostbolt hit for " + str(frostbolt.damage) + " ❄️❄️❄️")
                print("Remaining HP: ❤️  " + str(ogre.npc_hp))
                if ogre.npc_hp <= 0:
                    enemy_alive = False

        else:
            gold_reward = random.randint(int(ogre.npc_gold_reward*0.8), int(ogre.npc_gold_reward*1.2))
            gold = gold + gold_reward
            print("───────────────────────────────")
            print("ENEMY NPC PORAŽENO")
            print("Získal jsi " + str(gold_reward) + " goldů.")
            if gold >= 150:
                game_run = False
                print("Podařilo se ti úspěšně získat vícE než 150 goldů.")
                print("┌───────────────────────────────┐")
                print("│        VYHRÁL JSI!!!!         │")
                print("└───────────────────────────────┘")
        
    elif pick == 2:
        wolf.npc_hp = npc_hp_list[1]
        enemy = wolf
        print("───────────────────────────────")
        print("Zvolil jsi WOLF: HP = ❤️  " + str(wolf.npc_hp))
        enemy_alive = True
        
        while enemy_alive:
            print_spellbook()
            spell_pick = int(input("Tvoje volba: "))

            if spell_pick == 1:
                fireball = Spell("Fireball", 155, random.randint(850, 1337), 8)
                wolf.npc_hp = wolf.npc_hp - fireball.damage
                fireball.cast(fireball.casting_time)
                print("🔥🔥🔥 Fireball hit for " + str(fireball.damage) + " 🔥🔥🔥")
                print("Remaining HP: ❤️  " + str(wolf.npc_hp))
                if wolf.npc_hp <= 0:
                    enemy_alive = False

            if spell_pick == 2:
                frostbolt  = Spell("Frostbolt", 110, random.randint(650, 1210), 6)
                wolf.npc_hp = wolf.npc_hp - frostbolt.damage
                frostbolt.cast(frostbolt.casting_time)
                print("❄️❄️❄️ Frostbolt hit for " + str(frostbolt.damage) + " ❄️❄️❄️")
                print("Remaining HP: ❤️  " + str(wolf.npc_hp))
                if wolf.npc_hp <= 0:
                    enemy_alive = False

        else:
            gold_reward = random.randint(int(wolf.npc_gold_reward*0.8), int(wolf.npc_gold_reward*1.2))
            gold = gold + gold_reward
            print("───────────────────────────────")
            print("ENEMY NPC PORAŽENO")
            print("Získal jsi " + str(gold_reward) + " goldů.")
            if gold >= 150:
                game_run = False
                print("Podařilo se ti úspěšně získat více než 150 goldů.")
                print("┌───────────────────────────────┐")
                print("│        VYHRÁL JSI!!!!         │")
                print("└───────────────────────────────┘")
