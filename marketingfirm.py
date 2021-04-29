from sweepstake import Sweepstake


class MarketingFirm:
    def __init__(self, manager):
        # dependency injection for manager parameter
        # allows user to choose stack/queue manager before instantiating a firm
        self.manager = manager

    def create_sweepstakes(self, name):
        return Sweepstake(name)
