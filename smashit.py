#!/usr/bin/env python3

import random
import sys
import select

class SmashItEngine:
    def __init__(self, ui, xp, lvl, choice_function=random.choice):
        self.ui = ui
        self.choice_function = choice_function
        self.actions = ["bopit", "smashit", "twizzleit"]
        self.xp = xp
        self.lvl = lvl


    def start(self):
        response_time = 5
        self.ui.start()
        while True:
            response = self.take_turn()
            if response == True:
                self.ui.correct()
            elif response == False:
                self.ui.fail()
                break
            else:
                self.ui.timedout()
                break

    def end(self):
        print("The Game Has Ended!")
        print("You Got To Level ", self.lvl)
        yn = input("Try Again(Y/N)? ")
        yn.capitalise
        #still need to put in
        
    def next_action(self):
        return self.choice_function(self.actions)

    def take_turn(self):
        self.xp += 1
        action = self.next_action()
        resp_time = 6 - self.lvl
        self.level_up(resp_time)
        if self.lvl > 1:
            return self.ui.get_response_to(action, resp_time)
        else:
            return self.ui.get_response_to(action, 1)

    def level_up(self, response_time):
        if self.xp >= 5:
            print("\nLevel Up!\nResponse Time is now: {}\n".format(response_time))
            self.xp = 0
            self.lvl += 1
        else:
            pass


class SmashItTextUI:
    def __init__(self):
        self.responses = {
            "start": "Starting the Game in 3 seconds!",
            "bopit": "Bop It! (press B)",
            "smashit": "Smash It! (press S)",
            "twizzleit": "Twizzle It! (press T)"
        }
        self.action_expected = {
            "bopit": "b",
            "smashit": "s",
            "twizzleit": "t"
        }

    def get_response_to(self, action, response_time):
        print(action)
        print(self.responses[action])

        user_response = self.get_response_from_user(response_time)
        if user_response == None:
            return None

        expected_response = self.action_expected[action]
        return user_response.strip().lower() == expected_response

    def get_response_from_user(self, response_time):
        i, o, e = select.select([sys.stdin], [], [], response_time)
        return i[0].readline() if i else None

    def fail(self):
        print("You Lose!")
        SmashItEngine.end()

    def correct(self):
        print("Correct!!")

    def timedout(self):
        print("Too Slow!")
        SmashItEngine.end()

    def start(self):
        print("Starting Game...")

ui = SmashItTextUI()
smashitengine = SmashItEngine(ui, 0, 1)
smashitengine.start()


