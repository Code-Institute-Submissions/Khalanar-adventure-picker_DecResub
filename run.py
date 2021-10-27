from gamemanager import Event, Combat, Enemy, player



rat = Enemy("rat", 10, 2)
        
rat_combat = Combat(rat)


def do_something():
    print("something was done")

event_01 = Event("You continue walking through the dark, dense forest and you hear a distant echoing voice. You feel compelled to follow the voice but your gut wrenches disapprovingly",
    [["Trust gut", ""],
    ["follow the voice", ""]])

event_00 = Event("Good good, you're one step closer to learning the truth",
    [["Option1", ""],
    ["Option2", ""]])
    
game_start = Event(
    "Game Start, blablablabla?",
    [["say hello", event_00, do_something],
    ["attack", event_01, rat_combat]])


def main():
    game_start.run()

main()