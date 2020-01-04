import math
from typing import *

class Neighbor:
    def __init__(self, id, travel_cost):
        self.id = id
        self.travel_cost = travel_cost

class Node:
    def __init__(self, id, ticket_price, group):
        self.id = id
        self.ticket_price = ticket_price
        self.group = group
        self.neighbors: DefaultDict[(int, Neighbor)] = {}

    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id

    def __gt__(self, other):
        return self.id > other.id

    def __ge__(self, other):
        return self.id >= other.id

    def addNeighbor(self, neighbor, distance: float):
        n = Neighbor(neighbor.id, distance)
        self.neighbors[neighbor.id] = n


class Edge:
    def __init__(self, nodeA, nodeB, travel_cost):
        if travel_cost < 0:
            raise Exception("Incorrect distance between node " + str(nodeA.id) + " and node " + str(nodeB.id))
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.travel_cost = travel_cost

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def addNode(self, node: Node):
        self.nodes[node.id] = node

    def createAndAddEdge(self, nodeA, nodeB, travel_cost):
        self.nodes[nodeA.id].addNeighbor(self.nodes[nodeB.id], travel_cost)
        self.nodes[nodeB.id].addNeighbor(self.nodes[nodeA.id], travel_cost)
        self.edges.append(Edge(nodeA.id, nodeB.id, travel_cost))

    def addEdge(self, edge: Edge):
        nodeA = self.getNodeById(edge.nodeA)
        nodeB = self.getNodeById(edge.nodeB)
        return self.createAndAddEdge(nodeA, nodeB, edge.travel_cost)

    def getNodeById(self, id: int) -> Node:
        return self.nodes[id]

    def getCost(self, nodeA, nodeB, tickets):
        ticket_cost = 0
        if self.nodes[nodeB.id].group not in tickets:
            ticket_cost = nodeB.ticket_price
        return self.nodes[nodeA.id].neighbors[nodeB.id].travel_cost + ticket_cost

    def getNeighbors(self, node: Node) -> DefaultDict[(int, Neighbor)]:
        return self.nodes[node.id].neighbors

def load_graph_from_file(path, dist_multiplier):
    file = open(path, 'r')

    graph = Graph()
    #add nodes
    for line in file:
        l = line.rstrip('\n')
        if '#' in l:
            break
        dict = l.split(' ')
        id = int(dict[0])
        ticket_price = float(dict[1])
        group = dict[2]
        graph.addNode(Node(id, ticket_price, group))

    #add edges
    for line in file:
        l = line.rstrip('\n')
        if 'eof' in l:
            break
        dict = l.split(' ')
        id1 = int(dict[0])
        id2 = int(dict[1])
        travel_cost = float(dict[2])*dist_multiplier
        e = Edge(id1, id2, travel_cost)
        graph.addEdge(e)
    file.close()    
    return graph