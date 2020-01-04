import math
from typing import *

class Neighbor:
    def __init__(self, nodeId, distance):
        self.nodeId = nodeId
        self.distance = distance

class Node:
    def __init__(self, nodeId, ticket_price, group):
        self.nodeId = nodeId
        self.ticket_price = ticket_price
        self.group = group
        self.neighbors: DefaultDict[(int, Neighbor)] = {}

    def __lt__(self, other):
        return self.nodeId < other.nodeId

    def __le__(self, other):
        return self.nodeId <= other.nodeId

    def __gt__(self, other):
        return self.nodeId > other.nodeId

    def __ge__(self, other):
        return self.nodeId >= other.nodeId

    def addNeighbor(self, neighbor, distance: float):
        n = Neighbor(neighbor.nodeId, distance)
        self.neighbors[neighbor.nodeId] = n


class Edge:
    def __init__(self, nodeA, nodeB, travel_cost):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.travel_cost = travel_cost

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def addNode(self, node: Node):
        self.nodes[node.nodeId] = node

    def createAndAddEdge(self, nodeA, nodeB, travel_cost):
        self.nodes[nodeA.nodeId].addNeighbor(self.nodes[nodeB.nodeId], travel_cost)
        self.nodes[nodeB.nodeId].addNeighbor(self.nodes[nodeA.nodeId], travel_cost)
        self.edges.append(Edge(nodeA.nodeId, nodeB.nodeId, travel_cost))

    def addEdge(self, edge: Edge):
        nodeA = self.getNodeByID(edge.nodeA)
        nodeB = self.getNodeByID(edge.nodeB)
        return self.createAndAddEdge(nodeA, nodeB, edge.travel_cost)

    def getNodeByID(self, nodeId: int) -> Node:
        return self.nodes[nodeId]

    def getCost(self, nodeA, nodeBId, tickets):
        ticket_cost = 0
        if self.nodes[nodeB.id].group not in tickets:
            ticket_cost = nodeB.ticket_price
        return self.nodes[nodeA.nodeId].neighbors[nodeB.nodeId].travel_cost + ticket_cost

    def getNeighbors(self, node: Node) -> DefaultDict[(int, Neighbor)]:
        return self.nodes[node.nodeId].neighbors

def load_graph_from_file(path):
    file = open(path, 'r')

    graph = Graph()
    #add nodes
    for line in file:
        l = line.rstrip('\n')
        if '#' in l:
            break
        dict = l.split(' ')
        nodeId = int(dict[0])
        ticket_price = float(dict[1])
        group = float(dict[2])
        graph.addNode(Node(nodeId, x, y))

    #add edges
    for line in file:
        l = line.rstrip('\n')
        if 'eof' in l:
            break
        dict = l.split(' ')
        nodeId1 = int(dict[0])
        nodeId2 = int(dict[1])
        travel_cost = float(dict[2])*dist_multiplier
        e = Edge(nodeId1, nodeId2, travel_cost)
        graph.addEdge(e)
    file.close()    
    return graph