def output_text(text):
    print(text)


def continue_prompt():
    continue_bool = input("All done? Continue to next step? (y/n)")
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


def menu_facade():
    my_manager = MarketingFirmCreator().choose_manager_type()
    """Create your sweepstakes"""
    while True:
        new_sweepstakes = my_manager.manager.create_sweepstakes()
        my_manager.manager.insert_sweepstakes(new_sweepstakes)

        while True:
            contestant = Contestant()
            contestant.fill_contestant_info()
            new_sweepstakes.register_contestant(contestant)
            print("contestant registered!")
            add_more_contestants = continue_prompt()
            if add_more_contestants.lower() == 'y' or 'yes':
                continue
            else:
                break
        add_another_sweepstakes = continue_prompt()
        if add_another_sweepstakes.lower() == 'y' or 'yes':
            continue
        else:
            break

def get_sweepstakes_name():
    name = input("Name your sweepstakes >")
    return name
