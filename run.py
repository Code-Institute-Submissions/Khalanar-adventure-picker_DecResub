
inventory = {
    "gold": 3,
    "sword": 0,
    
}

class Event():
    def __init__(self, text, next_events):
        self.text = text
        self.next_events = next_events
    
    def _evaluate_next_event(self, user_input):
        
        command_found = False
        for event in self.next_events:
            if (user_input == event[0]):
                command_found = True
                
                if(event[2]):
                    if(callable(event[2])):
                        print("Extra action to be taken")
                        event[2]()
                else:
                    print("NO extra action to be taken")
                
                event[1].run()
                
        if (not command_found):
            print(f"\n-{user_input}- is not an option")
            self.run()
    
    def run(self):
        print(f"\n>>{self.text}")
        input_options = [event[0] for event in self.next_events]
        action_string = " | ".join([str(option) for option in input_options])
        print(f"What will you do? (type one of the following options):")
        user_input = input(f"{action_string}\n")
        
        self._evaluate_next_event(user_input)
        
        
        

def do_something():
    print("something was done")

event_01 = Event("Bold option my friend, the wizard is not amused",
    [["Option1", ""],
    ["Option2", ""]])

event_00 = Event("Good good, you're one step closer to learning the truth",
    [["Option1", ""],
    ["Option2", ""]])
    
game_start = Event("Game Start, blablablabla?",
    [["say hello", event_00, do_something],
    ["say bye", event_01, ""]])


def main():
    game_start.run()

main()