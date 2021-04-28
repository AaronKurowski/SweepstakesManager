class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self, contestant):
        self.contestants[contestant.reg_num] = contestant

    def pick_winner(self):
        return self.contestants.popitem()

    def print_contestant_info(self, contestant):
        contestant.display_contestant_info()
