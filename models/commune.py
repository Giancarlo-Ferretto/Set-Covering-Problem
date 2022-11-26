class Commune:
    def __init__(self, id, commune, cost):
        self.id = id
        self.commune = commune
        self.cost = cost

    def getId(self):
        return self.id

    def getCommune(self):
        return self.commune

    def getCost(self):
        return self.cost

    def __str__(self):
     return str(self.id)