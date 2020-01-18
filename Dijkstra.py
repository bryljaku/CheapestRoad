from Graph import *
from PriorityQueue import PriorityQueue
import time


class Dijkstra(object):
    
    def dijkstra(graph: Graph, s, g):
        start = graph.getNodeById(s)
        goal = graph.getNodeById(g)
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {start.id: None}
        start_tickets = set()
        if start.group is not None:
            start_tickets.add(start.group)
        tickets_earned = {start.id: start_tickets}
        cost_so_far = {start.id: 0}
        startTime = time.perf_counter()

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for i in graph.getNeighbors(current.id).values():
                next_node = graph.getNodeById(i.id)
                new_tickets = set(tickets_earned[current.id])
                new_tickets.add(next_node.group)
                new_cost = graph.getCost(
                    current, next_node, tickets_earned[current.id]) + cost_so_far[current.id]
                if next_node.id not in cost_so_far or new_cost < cost_so_far[next_node.id]:
                    cost_so_far[next_node.id] = new_cost
                    priority = new_cost
                    frontier.put(next_node, priority)
                    came_from[next_node.id] = current.id
                    tickets_earned[next_node.id] = new_tickets

        endTime = time.perf_counter()
        return reconstruct_path(came_from, start.id, goal.id), cost_so_far[goal.id], endTime - startTime

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path