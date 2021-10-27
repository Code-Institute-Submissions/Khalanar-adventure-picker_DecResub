class Event():
    """
    Class used to create new events. Events take in a @text to be displayed when run, and a list of possible @next_events. List for next_events include the keyword to trigger the event, the event that will be triggered, and optionally a function that will run right before running the event. Use the optional function to extend functionality for adding resources, or starting a combat loop
    """
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
        
class Combat():
    """
    Event used to create combat scenarios
    """
    def __init__(self, enemy):
        
        print(f"You are facing a mighty {enemy.name}")

class Enemy():
    """
    Class to create enemies
    """
    def __init__(self, name, hit_points, damage):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage