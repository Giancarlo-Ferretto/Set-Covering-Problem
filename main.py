import networkx as nx
from dataset.regionGraph import regionGraph

# dibuja el grafo en regionGraph.png
import matplotlib 
matplotlib.use("Agg")
import matplotlib.pyplot as plt
graphFigure = plt.figure()

nx.draw(regionGraph, ax=graphFigure.add_subplot(111), with_labels=True)
graphFigure.savefig("regionGraph.png")