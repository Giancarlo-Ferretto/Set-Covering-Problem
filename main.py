import random
import math
import networkx as nx
from dataset.regionGraph import regionGraph, graphToMatrix

# dibuja el grafo en regionGraph.png
import matplotlib 
matplotlib.use("Agg")
import matplotlib.pyplot as plt
graphFigure = plt.figure()

nx.draw(regionGraph, ax=graphFigure.add_subplot(111), with_labels=True)
graphFigure.savefig("regionGraph.png")

# communesdataset
binaryMatrix = graphToMatrix(regionGraph)

# costs of communes
costs = [1, 1.5, 1.2, 2, 3, 2, 1, 1, 3, 4, 3, 3, 2, 2.5, 1.5, 2, 2, 3, 2, 2, 3, 2, 3, 3, 1, 2.5, 2, 3.5, 2, 1.5, 2, 3, 3.5, 2, 2.5, 1.5]

# check if a commune is illuminated
def isCommuneIlluminated(commune, solution):
    if solution[commune] == 1:
        return True
    else:
        for neighbor in range(len(solution)):
            if binaryMatrix[commune, neighbor] == 1 and solution[neighbor] == 1:
                return True
    return False

# check if a region is illuminated
def isRegionIlluminated(solution):
    for i in range(len(solution)):
        if isCommuneIlluminated(i, solution) == False:
            return False
    return True

# calculate the cost of a solution
def calculateSolutionCost(solution):
    cost = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            cost += costs[i]
    return cost

# first solution vector
firstSolution = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# generate a random illuminated region solution
def generateRandomIlluminatedRegionSolution():
    solution = [0] * len(binaryMatrix)
    while isRegionIlluminated(solution) == False:
        solution[random.randint(0, len(solution)-1)] = 1
    return solution

print("First solution: ", firstSolution)
print("Cost of first solution: ", calculateSolutionCost(firstSolution))
print("Is first solution illuminated? ", isRegionIlluminated(firstSolution))
print("Is first commune of first solution illuminated? ", isCommuneIlluminated(0, firstSolution))
print(" ")
print(" ")

# simulated annealing algorithm
def simulatedAnnealing(solution):
    currentSolution = solution
    currentCost = calculateSolutionCost(currentSolution)
    temperature = 100000
    while temperature > 0.1:
        neighbor = generateRandomIlluminatedRegionSolution()
        neighborCost = calculateSolutionCost(neighbor)
        if neighborCost < currentCost:
            currentSolution = neighbor
            currentCost = neighborCost
        else:
            delta = neighborCost - currentCost
            probability = math.exp(-delta/temperature)
            if random.random() < probability:
                currentSolution = neighbor
                currentCost = neighborCost
        temperature *= 0.99
    return currentSolution

resultsCost = []
for i in range(10):
    simulatedAnnealingSolution = simulatedAnnealing(firstSolution)
    print("[execution:", i+1,"] Simulated-annealing solution: ", simulatedAnnealingSolution)
    print("[execution:", i+1,"] Cost of simulated-annealing solution: ", calculateSolutionCost(simulatedAnnealingSolution))
    print("[execution:", i+1,"] Is simulated-annealing solution region illuminated? ", isRegionIlluminated(simulatedAnnealingSolution))
    resultsCost.append(calculateSolutionCost(simulatedAnnealingSolution))

resultsCostAverage = sum(resultsCost)/len(resultsCost)
resultsCostStandardDeviation = math.sqrt(sum([(x-resultsCostAverage)**2 for x in resultsCost])/len(resultsCost))

print("Results cost average: ", resultsCostAverage)
print("Results cost standard deviation: ", resultsCostStandardDeviation)