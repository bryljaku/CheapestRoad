from Graph import *
from PriorityQueue import PriorityQueue
import time


def dijkstra(graph: Graph, s, g, starter_tickets=[], start_cost=0, previous_path=[], reversable_nodes=[], is_recurrency_dijkstra=False):
    start = graph.getNodeById(s)
    goal = graph.getNodeById(g)
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start.id: None}
    start_tickets = set(starter_tickets)
    if start.group is not None:
        start_tickets.add(start.group)
    tickets_earned = {start.id: start_tickets}
    cost_so_far = {start.id: start_cost}
    reverse_states = []

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break

        if current.id in reversable_nodes:
            if came_from[current.id] is not None and current.group not in tickets_earned[came_from[current.id]]:
                print("g1")
                reverse_states.append((reconstruct_path(came_from, s, current.id), cost_so_far[current.id], tickets_earned[current.id]))
            elif came_from[current.id] is None and not is_recurrency_dijkstra:
                print("g2")
                reverse_states.append([current.id], cost_so_far[current.id], tickets_earned[current.id])

        for i in graph.getNeighbors(current.id).values():
            next_node = graph.getNodeById(i.id)
            new_tickets = set(tickets_earned[current.id])
            new_tickets.add(next_node.group)
            new_cost = graph.getCost(current, next_node, tickets_earned[current.id]) + cost_so_far[current.id]
            
            if next_node.id not in cost_so_far or new_cost < cost_so_far[next_node.id]:
                cost_so_far[next_node.id] = new_cost
                priority = new_cost
                frontier.put(next_node, priority)
                came_from[next_node.id] = current.id
                tickets_earned[next_node.id] = new_tickets


    best_path = previous_path + reconstruct_path(came_from, start.id, goal.id)
    print(previous_path)
    best_cost = cost_so_far[goal.id]
    best_tickets = tickets_earned[goal.id]

    for state in reverse_states: # state = previous_path, previous_cost, previous_tickets
        p, c, t = dijkstra(graph=graph, s=state[0][-1], g=g, starter_tickets=state[2], start_cost=state[1], previous_path=state[0], reversable_nodes=reversable_nodes, is_recurrency_dijkstra=True)
        if c < best_cost:
            best_path = p
            best_cost = c
            best_tickets = t
    
    best_path = clean_path(best_path) # clean path from 'duplicates' e.g [1, 0, 0, 2] -> [1,0,2]. Duplicates occur due to recurrency dijkstra

    return best_path, best_cost, best_tickets


def clean_path(path):
    cleaned_path = []
    for n in path:
        if len(cleaned_path) == 0 or cleaned_path[-1] != n:
            cleaned_path.append(n)
    return cleaned_path

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path







def get_reversable_nodes(graph: Graph):
    mean_edge_price = sum(e.travel_cost for e in graph.edges) / len(graph.edges)
    max_ticket_prices_from_groups = get_max_ticket_prices(graph)
    reversable_groups = get_reverse_groups(graph)
    reversable_nodes = []
    for node in graph.nodes.values():
        if node.group in reversable_groups and node.ticket_price + mean_edge_price*2 < max_ticket_prices_from_groups[node.group]:
            reversable_nodes.append(node.id)
    return reversable_nodes


def get_max_ticket_prices(graph):
    max_ticket_prices = {}
    for node in graph.nodes.values():
        if node.group not in max_ticket_prices:
            max_ticket_prices[node.group] = node.ticket_price
        max_ticket_prices[node.group] = max(node.ticket_price, max_ticket_prices[node.group])
    return max_ticket_prices


def get_reverse_groups(graph):
    group_count = {}
    for n in graph.nodes.values():
        if n.group not in group_count:
            group_count[n.group] = 0
        group_count[n.group] += 1
    groups_to_reverse = []
    for group, count in group_count.items():
        if count > 1 and check_if_big_difference(graph, group):
            groups_to_reverse.append(group)
    return groups_to_reverse


def check_if_big_difference(graph, group):
    ticket_prices = []
    for node_id in graph.nodes:
        node = graph.getNodeById(node_id)
        if node.group == group:
            ticket_prices.append(node.ticket_price)
    return max(ticket_prices) > min(ticket_prices)+30 #lets hardcode it that its worth to return