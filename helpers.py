import networkx as nx


#------------------------------------------------------------#
#------------------- Diameter Calculation -------------------#
#------------------------------------------------------------#

def diameter(G:nx.Graph):
    return nx.algorithms.distance_measures.diameter(G)

#------------------------------------------------------------#
#--------------- Average Degree calculation -----------------#
#------------------------------------------------------------#
def average_degree(G: nx.Graph) -> float:
    average_degree = G.degree()
    sum_of_degrees = 0
    for node in average_degree:
        sum_of_degrees += node[1]
    return sum_of_degrees/G.number_of_nodes()


#------------------------------------------------------------#
#------------------- Density Calculation --------------------#
#------------------------------------------------------------#

def density(G: nx.Graph) -> float:
    no_of_edges = G.number_of_edges()
    no_of_nodes = G.number_of_nodes()
    if(no_of_nodes>1):
        D  = (2*no_of_edges)/(no_of_nodes * (no_of_nodes-1))
        return D
    else:
        return 0
    

#------------------------------------------------------------#
#------------------ Clustering Coefficient ------------------#
#------------------------------------------------------------#

def clustering_coefficient(G: nx.Graph,  i:int) -> float:
    neighbours = [n for n in G.neighbors(i)]
    no_of_neighbours = len(list(neighbours))


    sub_graph: nx.Graph =  G.subgraph(neighbours)
    
    num_connections = sub_graph.number_of_edges()

    if(no_of_neighbours > 1):
        return (2*num_connections)/ (no_of_neighbours*(no_of_neighbours-1))
    else:
        return 0


#------------------------------------------------------------#
#-----------Average Clustering Coefficient ------------------#
#------------------------------------------------------------#


def average_clustering_coefficient(G:nx.Graph):
    clustering_coefficients = []
    for node in range(1,53):
        clustering_coefficients.append(clustering_coefficient(G=G, i=node))
    return sum(clustering_coefficients)/len(clustering_coefficients)


