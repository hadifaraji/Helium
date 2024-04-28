class Config:
    """
    # flytoday.ir -------------> production -------------> 0
    # stage.flytoday.ir --------> semi_production -------> 1
    # production.flytoday.ir ------> self.stage ---------> 2
    """

    def __init__(self):
        self.stage = None
        self.semi_production = None
        self.production = None

    def root(self):
        self.production = "https://flytoday.ir"
        self.semi_production = "https://production.flytoday.ir"
        self.stage = "https://stage.flytoday.ir/"

        root = [self.production,
                self.semi_production,
                self.stage]

        return root[2]