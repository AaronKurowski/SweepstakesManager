from user_interface import contestant_info_prompt


class Contestant:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.reg_num = 0

    def notify(self, is_winner, sweepstakes):
        print(f"\n{is_winner.first_name} {is_winner.last_name} is the winner of {sweepstakes.name}!")
        for key, value in sweepstakes.contestants.items():
            print(f"Sorry {value.first_name} {value.last_name} you didn't win this time.")

    def fill_contestant_info(self):
        data = contestant_info_prompt()
        self.first_name = data[0]
        self.last_name = data[1]
        self.email = data[2]
        self.reg_num = int(data[3])
