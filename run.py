
class Event():
    def __init__(self, text, next_event_0, next_event_1):
        self.text = text
        self.next_event_0 = next_event_0
        self.next_event_1 = next_event_1
    
    def run(self):
        print(f"\n>>{self.text}")
        user_input = input(f"Do you -{self.next_event_0[0]}- or -{self.next_event_1[0]}-?\nYou ")
        
        if (user_input == self.next_event_0[0]):
            if (callable(self.next_event_0[1])):
                print("its a function")
                self.next_event_0[1]
            else:
                print("its NOT a function")
                self.next_event_0[1].run()
       
        elif (user_input == self.next_event_1[0]):
            if (callable(self.next_event_1[1])):
                self.next_event_1[1]
            else:
                self.next_event_1[1].run()
        else:
            print(f"\n-{user_input}- is not an option")
            self.run()
        

def do_something():
    print("something was done")

event_01 = Event("Bold option my friend, the wizard is not amused",
    ["Option1", ""],
    ["Option2", ""])

event_00 = Event("Good good, you're one step closer to learning the truth",
    ["Option1", ""],
    ["Option2", ""])
    
game_start = Event("Game Start, what will you do?",
    ["say hello", do_something],
    ["say bye", event_01])



def main():
    game_start.run()

main()