from Graph import *
import argparse
import itertools

dist_multiplier = 1.0

parser = argparse.ArgumentParser(description='PizzaDelivery path finder')
parser.add_argument("-input", action="store", required=True, type=str, help="Path to file with graph")

args = parser.parse_args()
file_path = args.input
graph = load_graph_from_file(file_path)


fullPath = []
pathCost = 0
print("\n" + "Full path: ")
print(list(map(lambda x: x.nodeId, fullPath)))

for i in range(0, len(fullPath) - 1):
    pathCost += graph.getCost(fullPath[i], fullPath[i+1])