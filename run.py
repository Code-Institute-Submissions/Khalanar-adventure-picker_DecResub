import sys
import os
from gamemanager import *


player = Player(0, "sword", 100)

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
trust_gut_gameover = Event()


game_start.create_event(
    "Game Start, blablablabla?",
    [["say hello", event_00],
    ["attack", event_01, rat_combat]])
    
trust_gut_gameover.create_event("Trusting your gut proved to be a mistake, you died",
    [["Restart", "", game_start],
    ["Quit", sys.exit]])

event_01.create_event("You continue walking through the dark, dense forest and hear a distant, echoing voice. You feel compelled to follow the voice but your gut wrenches, disapprovingly.",
    [["Trust gut",trust_gut_gameover, gameover],
    ["follow the voice", ""]])

event_00.create_event("Good good, you're one step closer to learning the truth",
    [["Option1", ""],
    ["Option2", ""]])
    



def main():
    game_start.run()

main()