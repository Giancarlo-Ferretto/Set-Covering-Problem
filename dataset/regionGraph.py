import networkx as nx

# Grafo de comunas a partir del dataset proporcionado en Tarea2-Enunciado.pdf
regionGraph = nx.Graph()

regionGraph.add_node(2)
regionGraph.add_edge(2, 4)
regionGraph.add_edge(2, 28)
regionGraph.add_edge(2, 5)

regionGraph.add_node(3)
regionGraph.add_edge(3, 5)
regionGraph.add_edge(3, 29)
regionGraph.add_edge(3, 27)

regionGraph.add_node(4)
regionGraph.add_edge(4, 25)
regionGraph.add_edge(4, 26)
regionGraph.add_edge(4, 28)
regionGraph.add_edge(4, 2)
regionGraph.add_edge(4, 5)

regionGraph.add_node(5)
regionGraph.add_edge(5, 2)
regionGraph.add_edge(5, 28)
regionGraph.add_edge(5, 4)
regionGraph.add_edge(5, 29)
regionGraph.add_edge(5, 3)

regionGraph.add_node(6)
regionGraph.add_edge(6, 15)
regionGraph.add_edge(6, 7)
regionGraph.add_edge(6, 9)
regionGraph.add_edge(6, 27)
regionGraph.add_edge(6, 28)
regionGraph.add_edge(6, 24)

regionGraph.add_node(7)
regionGraph.add_edge(7, 15)
regionGraph.add_edge(7, 10)
regionGraph.add_edge(7, 8)
regionGraph.add_edge(7, 9)
regionGraph.add_edge(7, 6)

regionGraph.add_node(8)
regionGraph.add_edge(8, 10)
regionGraph.add_edge(8, 7)

regionGraph.add_node(9)
regionGraph.add_edge(9, 7)
regionGraph.add_edge(9, 6)

regionGraph.add_node(10)
regionGraph.add_edge(10, 33)
regionGraph.add_edge(10, 8)
regionGraph.add_edge(10, 7)
regionGraph.add_edge(10, 15)

regionGraph.add_node(11)
regionGraph.add_edge(11, 16)
regionGraph.add_edge(11, 17)
regionGraph.add_edge(11, 13)
regionGraph.add_edge(11, 12)
regionGraph.add_edge(11, 15)
regionGraph.add_edge(11, 24)
regionGraph.add_edge(11, 25)

regionGraph.add_node(12)
regionGraph.add_edge(12, 17)
regionGraph.add_edge(12, 13)
regionGraph.add_edge(12, 15)
regionGraph.add_edge(12, 15)
regionGraph.add_edge(12, 11)

regionGraph.add_node(13)
regionGraph.add_edge(13, 17)
regionGraph.add_edge(13, 33)
regionGraph.add_edge(13, 15)
regionGraph.add_edge(13, 12)

regionGraph.add_node(14)
regionGraph.add_edge(14, 30)
regionGraph.add_edge(14, 37)
regionGraph.add_edge(14, 31)
regionGraph.add_edge(14, 17)
regionGraph.add_edge(14, 16)

regionGraph.add_node(15)
regionGraph.add_edge(15, 12)
regionGraph.add_edge(15, 13)
regionGraph.add_edge(15, 33)
regionGraph.add_edge(15, 10)
regionGraph.add_edge(15, 7)
regionGraph.add_edge(15, 6)
regionGraph.add_edge(15, 24)
regionGraph.add_edge(15, 11)

regionGraph.add_node(16)
regionGraph.add_edge(16, 30)
regionGraph.add_edge(16, 14)
regionGraph.add_edge(16, 17)
regionGraph.add_edge(16, 11)

regionGraph.add_node(17)
regionGraph.add_edge(17, 14)
regionGraph.add_edge(17, 31)
regionGraph.add_edge(17, 35)
regionGraph.add_edge(17, 33)
regionGraph.add_edge(17, 13)
regionGraph.add_edge(17, 12)
regionGraph.add_edge(17, 11)
regionGraph.add_edge(17, 16)

regionGraph.add_node(18)
regionGraph.add_edge(18, 20)
regionGraph.add_edge(18, 34)

regionGraph.add_node(19)
regionGraph.add_edge(19, 22)
regionGraph.add_edge(19, 21)
regionGraph.add_edge(19, 34)

regionGraph.add_node(20)
regionGraph.add_edge(20, 21)
regionGraph.add_edge(20, 34)
regionGraph.add_edge(20, 18)

regionGraph.add_node(21)
regionGraph.add_edge(21, 19)
regionGraph.add_edge(21, 34)
regionGraph.add_edge(21, 20)

regionGraph.add_node(22)
regionGraph.add_edge(22, 23)
regionGraph.add_edge(22, 19)

regionGraph.add_node(23)
regionGraph.add_edge(23, 22)

regionGraph.add_node(24)
regionGraph.add_edge(24, 25)
regionGraph.add_edge(24, 11)
regionGraph.add_edge(24, 15)
regionGraph.add_edge(24, 6)
regionGraph.add_edge(24, 27)
regionGraph.add_edge(24, 28)
regionGraph.add_edge(24, 26)

regionGraph.add_node(25)
regionGraph.add_edge(25, 11)
regionGraph.add_edge(25, 24)
regionGraph.add_edge(25, 26)
regionGraph.add_edge(25, 4)

regionGraph.add_node(26)
regionGraph.add_edge(26, 25)
regionGraph.add_edge(26, 24)
regionGraph.add_edge(26, 28)
regionGraph.add_edge(26, 4)

regionGraph.add_node(27)
regionGraph.add_edge(27, 3)
regionGraph.add_edge(27, 29)
regionGraph.add_edge(27, 28)
regionGraph.add_edge(27, 24)
regionGraph.add_edge(27, 6)

regionGraph.add_node(28)
regionGraph.add_edge(28, 26)
regionGraph.add_edge(28, 24)
regionGraph.add_edge(28, 27)
regionGraph.add_edge(28, 29)
regionGraph.add_edge(28, 4)
regionGraph.add_edge(27, 5)

regionGraph.add_node(29)
regionGraph.add_edge(29, 5)
regionGraph.add_edge(29, 28)
regionGraph.add_edge(29, 27)
regionGraph.add_edge(29, 3)

regionGraph.add_node(30)
regionGraph.add_edge(30, 34)
regionGraph.add_edge(30, 36)
regionGraph.add_edge(30, 38)
regionGraph.add_edge(30, 16)
regionGraph.add_edge(30, 31)
regionGraph.add_edge(30, 37)
regionGraph.add_edge(30, 14)
regionGraph.add_edge(30, 16)

regionGraph.add_node(31)
regionGraph.add_edge(31, 14)
regionGraph.add_edge(31, 30)
regionGraph.add_edge(31, 38)
regionGraph.add_edge(31, 35)
regionGraph.add_edge(31, 17)

regionGraph.add_node(33)
regionGraph.add_edge(33, 17)
regionGraph.add_edge(33, 35)
regionGraph.add_edge(33, 10)
regionGraph.add_edge(33, 15)
regionGraph.add_edge(33, 13)

regionGraph.add_node(34)
regionGraph.add_edge(34, 19)
regionGraph.add_edge(34, 21)
regionGraph.add_edge(34, 20)
regionGraph.add_edge(34, 18)
regionGraph.add_edge(34, 36)
regionGraph.add_edge(34, 30)

regionGraph.add_node(35)
regionGraph.add_edge(35, 31)
regionGraph.add_edge(35, 33)
regionGraph.add_edge(35, 17)
regionGraph.add_edge(35, 14)

regionGraph.add_node(36)
regionGraph.add_edge(36, 34)
regionGraph.add_edge(36, 38)
regionGraph.add_edge(36, 30)

regionGraph.add_node(37)
regionGraph.add_edge(37, 30)
regionGraph.add_edge(37, 14)

regionGraph.add_node(38)
regionGraph.add_edge(38, 36)
regionGraph.add_edge(38, 31)
regionGraph.add_edge(38, 14)
regionGraph.add_edge(38, 30)

# graph to adjacency matrix
def graphToMatrix(graph):
    # graph to adjacency matrix
    adjacencyMatrix = nx.to_numpy_matrix(regionGraph, nodelist=sorted(regionGraph.nodes))

    # set diagonal to 1
    for i in range(0, len(adjacencyMatrix)):
        adjacencyMatrix[i, i] = 1

    return adjacencyMatrix