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
event_00 = Event()
event_01 = Event()
event_02 = Event()
event_03 = Event()
event_04 = Event()
event_05 = Event()
event_06 = Event()
trust_gut_gameover = Event()


game_start.create_event(
    "You wake up in the middle of a forest. You are not sure where you are. Judging by the amount of moss in the trees around you it somewhere in the middle of October in the northern hemisphere. You have no memories whatsoever of ever having come to this forest, and something about it unsettles your stomach\nYour trusty sword is firmly in its sheath, which is a good sign, you have not been robbed. Or so you think.",
    [["Check coin purse", event_00],
    ["Unsheath sword", event_01]])
    
event_00.create_event(f"You reach out to your coin purse but it's not in your belt. At least nowhere to be found. You start to panic but realize you're wearing it to the right of your belt instead of the left. Odd, you have always worn it in your left side. There's {player.gold} coins in it. You don't remember how much you had left, or when was the last time you actually used it.",
    [["Unsheath sword", "", event_01],
    ["Quit", sys.exit]])

event_01.create_event("You reach out to your sword but can't unsheathe it. It feels stuck. Upon closer inspection you realise it's not all the way in. You pull harder and manage to unsheath your steel completely covered in dried-out blood, so thick that you think it might have been responsible for getting the sword stuck in your prime leather sheath. While you lament the moment you ever put your dirty sword away you hear some leaves rambling in the bushes to your left.",
    [["Check bushes",event_02],
    ["Hide", ""]])

event_02.create_event("Your brain tells you your sword will be practically useless in this state but your heart is pumping in anticipation. As you approach the bushes, a rat comes out. It's not a normal rat. There is something vicious about the way it looks at you. Like an animal without any self-preservation insticts, like an animal taken away by something dark that you can't begin to comprehend",
    [["Attack", event_03, rat_combat],
    ["run", ""]])
    

event_03.create_event("You continue walking through the dark, dense forest and hear a distant, echoing voice. You feel compelled to follow the voice but your gut wrenches, disapprovingly.",
    [["Trust gut",trust_gut_gameover, gameover],
    ["follow the voice", ""]])

trust_gut_gameover.create_event("Good good, you're one step closer to learning the truth",
    [["Option1", ""],
    ["Option2", ""]])
    


def main():
    game_start.run()

main()