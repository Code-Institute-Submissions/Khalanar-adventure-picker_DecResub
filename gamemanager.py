import time
import random

class Player():
    """
    
    """
    def __init__(self, gold, weapon, hitpoints):
        self.gold = gold
        self.weapon = weapon
        self.hitpoints = hitpoints
        
    def calculate_damage_points(self):
        damage = random.randrange(0, 4)
        return damage
        
    def spend_gold(self, amount):
        self.gold -= amount
    
    def earn_gold(self, amount):
        self.gold += amount
        
    def take_damage(self, damage_taken):
        self.hitpoints -= damage_taken
        print(f"You take {damage_taken}p of damage ({self.hitpoints} left)")
        
        if (self.hitpoints <= 0):
            self.gameover()
        
    def gameover(self):
        print("GAME OVER")
        
        
player = Player(0, "sword", 100)
    
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
                        event[2].run()
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
        self.enemy = enemy
        print(f"You are facing a mighty {self.enemy.name}")
        self.combat_delay_seconds = 2
    
    def run(self):
        while self.enemy.hitpoints > 0:
            player.take_damage(self.enemy.damage)
            time.sleep(self.combat_delay_seconds)
            
            self.enemy.take_damage(player.calculate_damage_points())
            time.sleep(self.combat_delay_seconds)
            print("")
        print(f"{self.enemy.name} is dead!")

class Enemy():
    """
    Class to create enemies
    """
    def __init__(self, name, hitpoints, damage):
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage
    
    def take_damage(self, damage_taken):
        self.hitpoints -= damage_taken
        self.hitpoints = 0 if self.hitpoints < 0 else self.hitpoints
        print(f"{self.name} takes {damage_taken}p of damage ({self.hitpoints} left)")