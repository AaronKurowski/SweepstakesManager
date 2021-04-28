from user_interface import *
from marketingfirm import MarketingFirm


class MarketingFirmCreator:
    def __init__(self):
        pass

    def choose_manager_type(self):
        choice = manager_type_prompt()
        return MarketingFirm(choice)
