import networkx as nx
import matplotlib.pyplot as plt

from helpers import average_clustering_coefficient, average_degree, density, clustering_coefficient

#------------------------------------------------------------#
#--------- Lab 5: Using Graph Libraries in Python -----------#
#------------------------------------------------------------#



# Load the .graph file
filename = "aves-sparrow-social.edges"
fh = open(filename, "rb")

# Data Format :  node1 node2 weight year
G: nx.Graph = nx.edgelist.read_edgelist(fh,nodetype=int,data=(("weight", float),("year",int),))

# Close file
fh.close()

# Draw graph using the matplotlib library
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.savefig("graph.png")



#------------------------------------------------------------#
#----------- No of nodes and edges calculation --------------#
#------------------------------------------------------------#

no_of_nodes = G.number_of_nodes()
no_of_edges = G.number_of_edges()

print("No of Nodes: " , str(no_of_nodes))
print("No of Edges: " , str(no_of_edges))


#------------------------------------------------------------#
#--------------- Average Degree calculation -----------------#
#------------------------------------------------------------#

print("Average degree: ", average_degree(G))


#------------------------------------------------------------#
#------------------- Density Calculation --------------------#
#------------------------------------------------------------#

print("Density: ",density(G))


#------------------------------------------------------------#
#------------------- Diameter Calculation -------------------#
#------------------------------------------------------------#

Dia  =  nx.algorithms.distance_measures.diameter(G)
print("Diameter: ",Dia)


#------------------------------------------------------------#
#------------ Clustering Coefficient Calculation ------------#
#------------------------------------------------------------#

Dia  =  average_clustering_coefficient(G)
