from user_interface import *


class Contestant:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.reg_num = 0

    def notify(self, winner, contestant_to_be_notified):
        """Takes in the sweepstakes winner and the contestant you want to notify.
        If they are equal then the winner gets his own message. The losers get a different message"""
        if winner.reg_num == contestant_to_be_notified.reg_num:
            print(f"Congratulations, {winner.first_name} {winner.last_name}, you won")
        elif winner.reg_num != contestant_to_be_notified.reg_num:
            print(f"Better luck next time {contestant_to_be_notified.first_name} {contestant_to_be_notified.last_name}")


    def fill_contestant_info(self):
        data = contestant_info_prompt()
        self.first_name = data[0]
        self.last_name = data[1]
        self.email = data[2]
        self.reg_num = int(data[3])
