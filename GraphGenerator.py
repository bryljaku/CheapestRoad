from Graph import *
import random
class GraphGenerator(object):

#simple generator, under development 
 
    def generate(number_of_nodes, number_of_groups, even_cost_in_one_group, max_ticket_price, min_ticket_price, max_distance, min_distance):
        graph = Graph()
        ticket_prizes_in_groups = {}
        if even_cost_in_one_group:
            for g in range(number_of_groups):
                ticket_prizes_in_groups[g] = random.randint(min_ticket_price, max_ticket_price)
        for i in range(number_of_nodes):
            group = random.randrange(number_of_groups)
            ticket_price = random.randint(min_ticket_price, max_ticket_price)
            if even_cost_in_one_group:
                ticket_price = ticket_prizes[group]
            graph.addNode(Node(i, ticket_price, group))


        first_connected_node = random.randrange(number_of_nodes)
        connected = [first_connected_node]
        for i in range(number_of_nodes):
            if i == first_connected_node:
                continue
            node_a = graph.getNodeById(i)
            node_b = graph.getNodeById(random.choice(connected))
            distance = random.randint(min_distance, max_distance)
            graph.createAndAddEdge(node_a, node_b, distance)
            connected.append(i)
        

        return graph