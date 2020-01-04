from Graph import *
import argparse
import itertools
from Dijkstra import Dijkstra
dist_multiplier = 1.0

parser = argparse.ArgumentParser(description='PizzaDelivery path finder')
parser.add_argument("-input", action="store", required=True, type=str, help="Path to file with graph")

args = parser.parse_args()
file_path = args.input
graph = load_graph_from_file(file_path, dist_multiplier)

nodeBId = len(graph.nodes) - 1
path, cost, tickets = Dijkstra.search(graph, 0, nodeBId)
print(f"Full path: {path}\ncost: {cost}\ntickets: {tickets}")
