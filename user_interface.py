from sweepstakesstackmanager import SweepstakesStackManager
from sweepstakesqueuemanager import SweepstakesQueueManager


def output_text(text):
    print(text)


def get_contestant_info():
    pass


def display_contestant_info(self):
    output_text(f"First name: {self.first_name}\nLast name: {self.last_name}"
                f"\nEmail: {self.email}\nRegistration #: {self.reg_num}")


def manager_type_prompt():
    pick_manager = input("Stack or Queue manager? >")
    if pick_manager.lower() == 'stack':
        return SweepstakesStackManager()
    else:
        return SweepstakesQueueManager()
