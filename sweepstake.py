from user_interface import *
import random


class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self, contestant):
        self.contestants[contestant.reg_num] = contestant

    def pick_winner(self):
        random_key = random.choice(list(self.contestants))
        return self.contestants[random_key]

    def print_contestant_info(self, contestant):
        display_contestant_info(contestant)
