from Graph import *

class Dijkstra(object):
    def search(graph, nodeAId, nodeBId):
        visited = [nodeAId]
        tickets = set()
        nodeA = graph.getNodeById(nodeAId)

        if nodeA.group is not None:
            tickets.add(nodeA.group)

        states_to_visit = [[nodeAId], 0, [])]
        
        while states_to_visit:
            path, cost, tickets = states_to_visit.pop()
            currentNode: Node = graph.getNodeById(path[-1])
            if currentNode.id == nodeBId:
                return path, cost, tickets
            for n in currentNode.neighbours:
                if n.id not in visited:
                    node = graph.getNodeById(n.id)
                    visited.append(node.id)
                    new_path = path + node.id
                    new_cost = graph.getCost(currentNode, node, tickets)
                    new_tickets = tickets
                    if node.group is not None:
                        tickets.add(node.group)
            
                    states_to_visit.append(new_path, new_cost, new_tickets)

        return [], -1, []