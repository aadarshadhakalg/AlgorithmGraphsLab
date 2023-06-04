import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

from graph_helper import GraphHelper

#------------------------------------------------------------#
#--------- Lab 5: Using Graph Libraries in Python -----------#
#------------------------------------------------------------#
aves_sparrpw_social: GraphHelper = GraphHelper("networks/smallnetworks/aves-sparrow-social.edges",data=(("weight", float),("year",int),))
aves_sparrpw_social.save_graph("graph/aves_sparrpw_social.png")
print("No of Nodes: " , str(aves_sparrpw_social.G.number_of_nodes()))
print("No of Edges: " , str(aves_sparrpw_social.G.number_of_edges()))
print("Average degree: ", aves_sparrpw_social.average_degree())
print("Density: ",aves_sparrpw_social.density())
print("Diameter: ",aves_sparrpw_social.diameter())
print("Average Clustering Coefficient: ",aves_sparrpw_social.average_clustering_coefficient())

print("\n----------------------------------------------------\n")


#------------------------------------------------------------#
#------------------- For 5 Big Networks ---------------------#
#------------------------------------------------------------#
bio_ce_cx: GraphHelper = GraphHelper("networks/bignetworks/bio-CE-CX.edges",data=(("weight", float),))
bio_ce_cx.save_degree_distribution("degree_distributions/bio_ce_cx.png")
bio_grid_fruitfly: GraphHelper = GraphHelper("networks/bignetworks/bio-grid-fruitfly.edges",delimiter=",")
bio_grid_fruitfly.save_degree_distribution("degree_distributions/bio_grid_fruitfly.png")
bio_grid_human: GraphHelper = GraphHelper("networks/bignetworks/bio-grid-human.edges",delimiter=",")
bio_grid_human.save_degree_distribution("degree_distributions/bro_grid_human.png")
bio_grid_yeast: GraphHelper = GraphHelper("networks/bignetworks/bio-grid-yeast.edges",delimiter=",")
bio_grid_yeast.save_degree_distribution("degree_distributions/bio_grid_yeast.png")
bio_worm_net: GraphHelper = GraphHelper("networks/bignetworks/bio-WormNet-v3.edges",data=(("weight", float),))
bio_worm_net.save_degree_distribution("degree_distributions/bio_worm_net.png")

all_graphs = [bio_ce_cx,bio_grid_fruitfly, bio_grid_human, bio_grid_yeast, bio_worm_net]
data = []
for graph in all_graphs:
    data.append([graph.G.number_of_nodes(),graph.G.number_of_edges(),graph.average_degree(),graph.density(),graph.diameter(),graph.average_clustering_coefficient()])

print(tabulate(data,headers=["Nodes","Edges","Average Degree","Density","Diameter","Clustering Coefficient"]))
