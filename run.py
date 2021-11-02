import sys
import os
from gamemanager import *


player = Player(3, "sword", 100)

# Declare all enemy types
rat = Enemy("rat", 6, 2)

# Declare all combat events
rat_combat = Combat(rat, player)


def do_something():
    print("something was done")


# Declare all events as empty so they can be referenced no matter when they have their values assigned
game_start = Event()
check_wallet = Event()
unsheath_sword = Event()
approach_bush = Event()
stand_up = Event()
event_04 = Event()
event_05 = Event()
event_06 = Event()
trust_gut_gameover = Event()
approach_bushes_gameover = Event()


game_start.create_event(
    "You wake up in the middle of a forest. You are not sure where you are. Judging by the amount of moss in the trees around you it somewhere in the middle of October in the northern hemisphere. You have no memories whatsoever of ever having come to this forest, and something about it unsettles your stomach\nYour trusty sword is firmly in its sheath, which is a good sign, you have not been robbed. Or so you think.",
    [["Check coin purse", check_wallet],
    ["Unsheath sword", unsheath_sword]])
    
check_wallet.create_event(
    f"You reach out to your coin purse but it's not in your belt. At least nowhere to be found. You start to panic but realize you're wearing it to the right of your belt instead of the left. Odd, you have always worn it in your left side. There's {player.gold} coins in it. You don't remember how much you had left, or when was the last time you actually used it.",
    [["Unsheath sword", unsheath_sword],
    ["Stand up", stand_up]])

unsheath_sword.create_event(
    "You reach out to your sword but can't unsheathe it. It feels stuck. Upon closer inspection you realise it's not all the way in. You pull harder and manage to unsheath your steel, completely covered in dried-out blood so thick that you think it might have been responsible for ruining your prime-leather scabbard. While you lament the moment you ever put your sword away before cleaning it, the bushes to your left start rustling.",
    [["Check bushes",approach_bush],
    ["Hide", ""]])

approach_bush.create_event(
    "Your brain tells you your sword will be practically useless in this state but your heart is pumping with anticipation. As you approach the bushes, a rat comes out. It's not a normal rat. There is something vicious about the way it looks at you. Like an animal without any self-preservation insticts, like an animal taken away by something dark that you can't begin to comprehend",
    [["Attack", event_03, rat_combat],
    ["run", ""]])
    

stand_up.create_event(
    "You stand up, you feel dizzy. You're unsure if for the lack of food or lack of sleep, but it's certainly a feeling you are not used to. Before you can even make sense to whatever is going on with, your gut insticts activate, there is something odd about the bushes next to you.",
    [["Approach",approach_bushes_gameover],
    ["Unsheath sword", event_01]])

event_04.create_event(
    "You continue walking through the dark, dense forest and hear a distant, echoing voice. You feel compelled to follow the voice but your gut wrenches, disapprovingly.",
    [["Trust gut", gameover, trust_gut_gameover],
    ["follow the voice", ""]])

approach_bushes_gameover.create_event(
    "You approach the bushes, head-in, unprepared, and start to regret your boldness. As you reflect on other terrible decisions of your past and how everything turned out just fine in the end, a vicious red-eyed rat jumps through the bushes and latches onto your neck. If only you had been more cautious and readied your sword. You try get the rat out of your neck, but its fangs are so deep into your neck that with every pull you're just helping the rat rip through your throat even faster.\nYou die.\n\n**GAME OVER**",
    [["Restart", game_start],
    ["Exit", sys.exit]])

trust_gut_gameover.create_event(
    "Good good, you're one step closer to learning the truth",
    [["Restart", game_start],
    ["Exit", sys.exit]])
    


def main():
    game_start.run()

main()