from user_interface import *


class Contestant:
    def __init__(self, first_name, last_name, email_address, number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.reg_num = number

    def notify(self, is_winner):
        print(f"{is_winner.first_name} {is_winner.last_name} wins the sweepstakes!")

    def get_contestant_info(self):
        self.first_name = get_contestant_info()
        self.last_name = input("What is your last name? >")
        self.email = input("What is your email? >")
        self.reg_num = input("Enter registration number. >")
