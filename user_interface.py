def output_text(text):
    print(text)


def continue_prompt():
    continue_bool = input("Add more? (y/n) >")
    return continue_bool


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
