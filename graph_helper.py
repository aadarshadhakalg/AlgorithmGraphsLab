from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


class GraphHelper:

    G : nx.Graph

    def __init__(self,filename,data=None, delimiter=" "):
        fh = open(filename, "rb")
        # Data Format :  node1 node2 weight year
        self.G = nx.edgelist.read_edgelist(fh,nodetype=int,data=data,delimiter=delimiter)
        # Close file
        fh.close()
        print("Graph Loaded: ", filename)


    #------------------------------------------------------------#
    #------------------- Diameter Calculation -------------------#
    #------------------------------------------------------------#

    def diameter(self):
        if nx.is_connected(self.G):
            return nx.algorithms.distance_measures.diameter(self.G)
        else:
            return "Disconnected"

    #------------------------------------------------------------#
    #--------------- Average Degree calculation -----------------#
    #------------------------------------------------------------#
    def average_degree(self) -> float:
        degrees = [degree for _, degree in self.G.degree()]
        return sum(degrees)/self.G.number_of_nodes()


    #------------------------------------------------------------#
    #------------------- Density Calculation --------------------#
    #------------------------------------------------------------#

    def density(self) -> float:
        no_of_edges = self.G.number_of_edges()
        no_of_nodes = self.G.number_of_nodes()
        if(no_of_nodes>1):
            D  = (2*no_of_edges)/(no_of_nodes * (no_of_nodes-1))
            return D
        else:
            return 0
        

    #------------------------------------------------------------#
    #------------------ Clustering Coefficient ------------------#
    #------------------------------------------------------------#

    def clustering_coefficient(self) -> float:
        clustering_coefficients = {}
        for node in self.G.nodes():
            neighbors = set(self.G.neighbors(node))
            k = len(neighbors)
            if k < 2:
                clustering_coefficients[node] = 0.0
            else:
                num_connected_edges = sum(1 for i, j in combinations(neighbors, 2) if self.G.has_edge(i, j))
                clustering_coefficients[node] = 2.0 * num_connected_edges / (k * (k - 1))

        return clustering_coefficients


    #------------------------------------------------------------#
    #-----------Average Clustering Coefficient ------------------#
    #------------------------------------------------------------#


    def average_clustering_coefficient(self) -> float:
        clustering_coefficients =  self.clustering_coefficient()
        return sum(clustering_coefficients.values()) / len(clustering_coefficients)
    

    def save_graph(self, name:str):
        nx.draw(self.G, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.savefig(name)

    def show_graph(self):
        nx.draw(self.G, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()



