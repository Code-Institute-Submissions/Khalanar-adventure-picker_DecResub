# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
class Event():
    def __init__(self, text, next_event_0, next_event_1):
        self.text = text
        self.next_event_0 = next_event_0
        self.next_event_1 = next_event_1
    
    def run(self):
        print(f">>{self.text}")
        user_input = input(f"Do you -{self.next_event_0[0]}- or -{self.next_event_1[0]}-?\n")
        if (user_input == self.next_event_0[0]):
            self.next_event_0[1].run()
        elif (user_input == self.next_event_1[0]):
            self.next_event_1[1].run()
        else:
            print("Invalid option, should loop back to the start")
        

event_01 = Event("You said hello back",
    ["event_01 Option1", ""],
    ["event_01 Option2",""])

event_00 = Event("You said hello back",
    ["event_00 Option1", ""],
    ["event_00 Option2",""])
    
game_start = Event("Game Start, what will you do?",
    ["say hello back", event_00],
    ["say bye", event_01])



game_start.run()