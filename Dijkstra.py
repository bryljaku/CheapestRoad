from Graph import *
from PriorityQueue import PriorityQueue
class Dijkstra(object):
    def search(graph, nodeAId, nodeBId):
        visited = [nodeAId]
        ticket = set()
        nodeA = graph.getNodeById(nodeAId)

        if nodeA.group is not None:
            ticket.add(nodeA.group)

        states_to_visit = PriorityQueue()
        states_to_visit.put(([nodeAId],ticket, 0), 0)
        
        while not states_to_visit.empty():
            path, tickets, cost = states_to_visit.get()
            print(f'{path} {tickets} {cost}')
            currentNode: Node = graph.getNodeById(path[-1])
            if currentNode.id == nodeBId:
                return path, cost, tickets
            for n in currentNode.neighbors:
                if n not in visited:
                    node = graph.getNodeById(n)
                    visited.append(node.id)
                    new_path = path + [node.id]
                    new_cost = graph.getCost(currentNode, node, tickets)
                    new_tickets = tickets
                    if node.group is not None:
                        new_tickets.add(node.group)
            
                    states_to_visit.put((new_path, new_tickets, new_cost), new_cost)

        return [], -1, []