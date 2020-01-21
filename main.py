from Graph import *
import argparse
import itertools
from Dijkstra import *
from GraphGenerator import GraphGenerator
dist_multiplier = 1.0

parser = argparse.ArgumentParser(description='PizzaDelivery path finder')
parser.add_argument("-input", action="store", required=True, type=str, help="Path to file with graph")

args = parser.parse_args()
file_path = args.input
graph = load_graph_from_file(file_path, dist_multiplier)
#graph = GraphGenerator.generate(80000, 3, False, 40, 0, 100, 30)
nodeBId = len(graph.nodes) - 1
nodeAId = 1

reversable_nodes = get_reversable_nodes(graph)
print(f'reversable nodes: {reversable_nodes}')
a = dijkstra(graph, nodeAId, nodeBId, reversable_nodes=reversable_nodes)
print(a)