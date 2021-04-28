from user_interface import *


class Contestant:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.reg_num = 0

    def notify(self, is_winner):
        print(f"{is_winner.first_name} {is_winner.last_name} wins the sweepstakes!")

    def fill_contestant_info(self):
        data = contestant_info_prompt()
        self.first_name = data[0]
        self.last_name = data[1]
        self.email = data[2]
        self.reg_num = data[3]
