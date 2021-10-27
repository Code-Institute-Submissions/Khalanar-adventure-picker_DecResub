from gamemanager import Event, Combat, Enemy

inventory = {
    "gold": 0,
    "sword": 0,
}

rat = Enemy("rat", 10, 2)
        
fight_rat = Combat(rat)

def do_something():
    print("something was done")

event_01 = Event("Bold option my friend, the wizard is not amused",
    [["Option1", ""],
    ["Option2", ""]])

event_00 = Event("Good good, you're one step closer to learning the truth",
    [["Option1", ""],
    ["Option2", ""]])
    
game_start = Event(
    "Game Start, blablablabla?",
    [["say hello", event_00, do_something],
    ["say bye", event_01, ""]])


def main():
    game_start.run()

main()