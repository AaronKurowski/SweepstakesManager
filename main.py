from marketingfirmcreator import MarketingFirmCreator
from user_interface import continue_prompt, get_sweepstakes_name
from contestant import Contestant


if __name__ == '__main__':
    # def run_simulation():
        # my_manager = MarketingFirmCreator().choose_manager_type()
        # my_new_sweepstakes = my_manager.create_sweepstakes("test123")
        # my_new_sweepstakes2 = my_manager.create_sweepstakes("anothertest")
        # my_new_sweepstakes3 = my_manager.create_sweepstakes("lasttest")
        # my_manager.manager.insert_sweepstakes(my_new_sweepstakes)
        # my_manager.manager.insert_sweepstakes(my_new_sweepstakes2)
        # my_manager.manager.insert_sweepstakes(my_new_sweepstakes3)
        #
        # print(my_manager.manager.stack.stack[0].name)
        # print(my_manager.manager.stack.stack[1].name)
        # print(my_manager.manager.stack.stack[2].name)
        #
        # get_sweepstakes = my_manager.manager.get_sweepstakes()
        # print(get_sweepstakes.name)
        #
        # print(my_manager.manager.stack.stack[0].name)
        # print(my_manager.manager.stack.stack[1].name)
        # # print(my_manager.manager.stack.stack[2].name)

    def run_simulation():
        my_manager = MarketingFirmCreator().choose_manager_type()
        """Creates new sweepstakes"""
        while True:
            new_sweepstakes_name = get_sweepstakes_name()
            new_sweepstakes = my_manager.create_sweepstakes(new_sweepstakes_name)
            my_manager.manager.insert_sweepstakes(new_sweepstakes)

            while True:
                print("Enter Contestant:\n")
                contestant = Contestant()
                contestant.fill_contestant_info()
                new_sweepstakes.register_contestant(contestant)
                print("Contestant registered")
                add_more_contestants = continue_prompt()
                if add_more_contestants.lower() == 'y' or add_more_contestants.lower() == 'yes':
                    continue
                else:
                    break
            print("Add another sweepstake?")
            add_another_sweepstakes = continue_prompt()
            if add_another_sweepstakes.lower() == 'y' or add_another_sweepstakes.lower() == 'yes':
                continue
            else:
                break


    run_simulation()
