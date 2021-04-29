from marketingfirmcreator import MarketingFirmCreator


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
            new_sweepstakes = my_manager.create_sweepstakes('test')
            print(new_sweepstakes)
            my_manager.manager.insert_sweepstakes(new_sweepstakes)
            break
            # print("Contestant registered")


    run_simulation()
