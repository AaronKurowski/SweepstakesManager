from marketingfirmcreator import MarketingFirmCreator
from contestant import Contestant
from user_interface import *


if __name__ == '__main__':
    # manager = MarketingFirmCreator()
    # marketing_firm = manager.choose_manager_type()
    # sweepstake = marketing_firm.create_sweepstakes('test')
    # print(sweepstake.name)
    # sweepstake.register_contestant()

    contestant1 = Contestant()
    contestant1.fill_contestant_info()
    display_contestant_info(contestant1)
