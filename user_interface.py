from sweepstakesstackmanager import SweepstakesStackManager
from sweepstakesqueuemanager import SweepstakesQueueManager


def output_text(text):
    print(text)


def contestant_info_prompt():
    first_name = input("Enter first name >")
    last_name = input("Enter last name >")
    email = input("Enter email >")
    reg_num = input("Enter registration number >")
    info_list = [first_name, last_name, email, reg_num]
    return info_list


def display_contestant_info(contestant):
    output_text(f"First name: {contestant.first_name}\nLast name: {contestant.last_name}"
                f"\nEmail: {contestant.email}\nRegistration #: {contestant.reg_num}")


def manager_type_prompt():
    pick_manager = input("Stack or Queue manager? >")
    if pick_manager.lower() == 'stack':
        return SweepstakesStackManager()
    else:
        return SweepstakesQueueManager()
