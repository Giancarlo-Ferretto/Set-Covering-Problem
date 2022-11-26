class Commune:
    def __init__(self, commune, cost):
        self.commune = commune
        self.cost = cost

    def getCommune(self):
        return self.commune

    def getCost(self):
        return self.cost

    def __str__(self):
     return self.commune