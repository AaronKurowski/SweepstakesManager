from contestant import Contestant
from marketingfirmcreator import MarketingFirmCreator


if __name__ == '__main__':
    manager = MarketingFirmCreator()
    marketing_firm = manager.choose_manager_type()
    sweepstake = marketing_firm.create_sweepstakes('test')
    print(sweepstake.name)
    sweepstake.register_contestant()