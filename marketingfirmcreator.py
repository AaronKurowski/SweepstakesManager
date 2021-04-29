from marketingfirm import MarketingFirm
from user_interface import manager_type_prompt
from sweepstakesstackmanager import SweepstakesStackManager
from sweepstakesqueuemanager import SweepstakesQueueManager


class MarketingFirmCreator:
    def __init__(self):
        pass

    def choose_manager_type(self):
        choice = manager_type_prompt()
        if choice == 'stack':
            return MarketingFirm(SweepstakesStackManager())
        elif choice == 'queue':
            return MarketingFirm(SweepstakesQueueManager())
