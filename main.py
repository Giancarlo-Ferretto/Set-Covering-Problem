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
regionArray = graphToMatrix(regionGraph)

# costs of communes
costs = [1, 1.5, 1.2, 2, 3, 2, 1, 1, 3, 4, 3, 3, 2, 2.5, 1.5, 2, 2, 3, 2, 2, 3, 2, 3, 3, 1, 2.5, 2, 3.5, 2, 1.5, 2, 3, 3.5, 2, 2.5, 1.5]

# check if a commune is illuminated
def isCommuneIlluminated(commune, solution):
    if solution[commune] == 1:
        return True
    else:
        for neighbor in range(len(solution)):
            if regionArray[commune, neighbor] == 1 and solution[neighbor] == 1:
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

# generate a random solution
def generateRandomSolution():
    solution = [0] * len(regionArray)
    while isRegionIlluminated(solution) == False:
        solution[random.randint(0, len(solution)-1)] = 1
    return solution

#swap mutation
def swapMutation(solution, mutations=1):
    for i in range(mutations):
        index = random.randint(0, len(solution)-1)
        if solution[index] == 1:
            solution[index] = 0
        else:
            solution[index] = 1
    if isRegionIlluminated(solution) == False: return swapMutation(solution, mutations+1)
    return solution

# first solution
print(">>> Random solution:")
firstSolution = generateRandomSolution()
print("First solution: ", firstSolution)
print("Cost of first solution: ", calculateSolutionCost(firstSolution))
print("Is first solution region illuminated? ", isRegionIlluminated(firstSolution))
print("[test] Is first commune of first solution illuminated? ", isCommuneIlluminated(0, firstSolution))
print("[test] Is second commune of first solution illuminated? ", isCommuneIlluminated(1, firstSolution))
print(" ")

# simulated annealing algorithm
def simulatedAnnealing(initialSolution):
    initialSolutionCost = calculateSolutionCost(initialSolution)
    currentSolution = initialSolution
    currentCost = initialSolutionCost
    temperature = 100000
    while temperature > 0.1:
        neighbor = swapMutation(currentSolution)
        neighborCost = calculateSolutionCost(neighbor)
        delta = neighborCost - currentCost
        if delta < 0:
            currentSolution = neighbor
            currentCost = neighborCost
        else:
            probability = math.exp(-delta/temperature)
            if random.random() < probability:
                currentSolution = neighbor
                currentCost = neighborCost
        if(initialSolutionCost < currentCost):
            currentSolution = initialSolution
            currentCost = initialSolutionCost
        temperature *= 0.999
    return currentSolution

# simulated annealing solutions
print(">>> Simulated annealing solutions:")

resultsCost = []
bestSolution = firstSolution
bestSolutionCost = calculateSolutionCost(firstSolution)
for i in range(10):
    simulatedAnnealingSolution = simulatedAnnealing(bestSolution)
    simulatedAnnealingSolutionCost = calculateSolutionCost(simulatedAnnealingSolution)
    print("[execution:", i+1,"] Simulated-annealing solution: ", simulatedAnnealingSolution)
    print("[execution:", i+1,"] Cost of simulated-annealing solution: ", simulatedAnnealingSolutionCost)
    print("[execution:", i+1,"] Is simulated-annealing solution region illuminated? ", isRegionIlluminated(simulatedAnnealingSolution))
    resultsCost.append(simulatedAnnealingSolutionCost)

    if simulatedAnnealingSolutionCost < bestSolutionCost:
        bestSolution = simulatedAnnealingSolution
        bestSolutionCost = simulatedAnnealingSolutionCost

resultsCostAverage = sum(resultsCost)/len(resultsCost)
resultsCostStandardDeviation = math.sqrt(sum([(x-resultsCostAverage)**2 for x in resultsCost])/len(resultsCost))

print("Results cost average: ", resultsCostAverage)
print("Results cost standard deviation: ", resultsCostStandardDeviation)
print("Best solution: ", bestSolution)
print("Best solution cost: ", bestSolutionCost)