from Graph import *
import argparse
import itertools
from Dijkstra import *
from GraphGenerator import GraphGenerator
import sys
from input_utils import *


args = get_parser().parse_args()
file_path = args.input
hour_cost = args.hour_cost
number_of_nodes = args.number_of_nodes
number_of_groups = args.number_of_groups
even_cost_in_one_group = False
even_groups = args.even_groups
max_city_ticket_price = args.max_city_ticket_price
min_city_ticket_price = args.min_city_ticket_price
max_road_ticket_price = args.max_road_ticket_price
min_road_ticket_price = args.min_road_ticket_price
max_distance = args.max_distance 
min_distance = args.min_distance

graph = None
if file_path is not None:
    graph = load_graph_from_file(file_path, hour_cost)
else:
    print("You did not provide input file\nGraph will be generated for you.")
    if number_of_nodes is None:
        number_of_nodes = int(input("enter number of nodes "))
    if number_of_groups is None:   
        number_of_groups = int(input("enter number of groups "))
    even_cost_in_one_group = False
    if even_groups is None:
        even_groups = int(input("Dou you want ticket costs in a group of cities to be even? \n0-no 1-yes "))
    if (even_groups == 1):
        even_cost_in_one_group = True
    if max_city_ticket_price is None:
        max_city_ticket_price = int(input("enter max city ticket price "))
    if min_city_ticket_price is None:    
        min_city_ticket_price = int(input("enter min city ticket price "))
    if max_road_ticket_price is None:  
        max_road_ticket_price = int(input("enter max road ticket price "))
    if min_road_ticket_price is None:
        min_road_ticket_price = int(input("enter min road ticket price "))
    if max_distance is None:
        max_distance = int(input("enter max hours to travel a road "))
    if min_distance is None:
        min_distance = int(input("enter min hours to travel a road "))
    graph = GraphGenerator.generate(
            number_of_nodes,
            number_of_groups,
            even_cost_in_one_group,
            max_city_ticket_price,
            min_city_ticket_price,
            max_distance,
            min_distance,
            max_road_ticket_price,
            min_road_ticket_price,
            hour_cost)

if args.test is None:
    nodeBId = len(graph.nodes) - 1
    nodeAId = 1
    start_time = time.perf_counter()
    reversable_nodes = get_reversable_nodes(graph)
    path, cost, tickets = dijkstra(graph, nodeAId, nodeBId, reversable_nodes=reversable_nodes)
    end_time = time.perf_counter()
    print(f'path: {path}\ncost: {cost}\ntime: {end_time - start_time}\nnumber of reversable nodes: {len(reversable_nodes)}')

else: # creating test file
    max_nodes = int(input("enter max nodes"))
    step = int(input("enter step between iterations"))

    f = open(f'test_{number_of_nodes}_{max_nodes}_{number_of_groups}','w+')
    print(even_cost_in_one_group)
    for num_nodes in range(number_of_nodes, max_nodes, step):
        graph = GraphGenerator.generate(
            num_nodes,
            number_of_groups,
            even_cost_in_one_group,
            max_city_ticket_price,
            min_city_ticket_price,
            max_distance,
            min_distance,
            max_road_ticket_price,
            min_road_ticket_price, 
            hour_cost
        )
        nodeBId = len(graph.nodes) - 1
        nodeAId = 1
        start_time = time.perf_counter()
        reversable_nodes = set()
        if not even_cost_in_one_group:
            reversable_nodes = set(get_reversable_nodes(graph))
        path, cost, tickets = dijkstra(graph, nodeAId, nodeBId, reversable_nodes=reversable_nodes)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        num_of_reversable = len(reversable_nodes)
        num_edges = len(graph.edges)
        s = f'{num_nodes};{num_edges};{elapsed_time};{number_of_groups};{num_of_reversable}\n'
        f.write(s)

    f.close()





