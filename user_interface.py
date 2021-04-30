import smtplib


def output_text(text):
    print(text)


def continue_prompt():
    continue_bool = input("Add more? (y/n) >")
    return continue_bool


def select_winner_prompt():
    select_the_winner = input("Select a winner for sweepstakes? (y/n) >")
    if select_the_winner.lower() == 'y':
        return True
    else:
        return False


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
    try:
        if pick_manager.lower() == 'stack':
            return 'stack'
        elif pick_manager.lower() == 'queue':
            return 'queue'
    except:
        print("Type again")


def get_sweepstakes_name():
    name = input("Name your sweepstakes >")
    return name



def send_email(contestants):
    sender = 'sweepstakesManager@domain.com'
    receivers = []
    for contestant in contestants:
        contestant.email += receivers

    message = f"""From: From Person <sweepstakesManager@domain.com>
                    To: To Person <{receivers}>
                    Subject: TESTING 123

                    This is a test"""

    try:
        smtp_obj = smtplib.SMTP('localhost')
        smtp_obj.sendmail(sender, receivers, message)
        print("email successful")
    except smtplib.SMTPException:
        print("Error: email not sent")
