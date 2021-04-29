from user_interface import *
import random


class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self, contestant):
        """Sets registration number as key; contestant object set as value"""
        self.contestants[contestant.reg_num] = contestant

    def pick_winner(self):
        """Generates a random key in self.contestants and returns object with that key"""
        random_key = random.choice(list(self.contestants))
        return self.contestants.pop(random_key, None)

    def print_contestant_info(self, contestant):
        display_contestant_info(contestant)
