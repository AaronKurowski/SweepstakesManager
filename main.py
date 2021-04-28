from marketingfirmcreator import MarketingFirmCreator
from contestant import Contestant
from user_interface import *
from sweepstakesstackmanager import SweepstakesStackManager
from marketingfirm import MarketingFirm


if __name__ == '__main__':
    pass
    # manager = MarketingFirmCreator()
    # marketing_firm = manager.choose_manager_type()
    # sweepstake = marketing_firm.create_sweepstakes('test')
    # print(sweepstake.name)
    # sweepstake.register_contestant()

    # contestant1 = Contestant()
    # contestant1.fill_contestant_info()
    # display_contestant_info(contestant1)

    # manager = MarketingFirmCreator().choose_manager_type()
    # test = manager.create_sweepstakes('test')
    # manager.stack.insert_sweepstakes(test)

    manager = MarketingFirmCreator()
    my_stack_man = manager.choose_manager_type()
    new_stakes = my_stack_man.create_sweepstakes('stake test')

    contestant1 = Contestant()
    contestant1.fill_contestant_info()
    new_stakes.print_contestant_info(contestant1)
    new_stakes.register_contestant(contestant1)

    contestant2 = Contestant()
    contestant2.fill_contestant_info()
    new_stakes.print_contestant_info(contestant2)
    new_stakes.register_contestant(contestant2)

    winner = new_stakes.pick_winner()

    print(winner.first_name)


    # print(new_stakes.contestants[contestant1.reg_num].first_name)
    # print(new_stakes.contestants[contestant2.reg_num].first_name)
