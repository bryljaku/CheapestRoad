import argparse
def get_parser():
    parser = argparse.ArgumentParser(description='Trip')
    parser.add_argument("-input", action="store", required=False, type=str, help="Path to file with graph")
    parser.add_argument("-hour_cost", action="store", required=True, type=int, help="hour cost")
    parser.add_argument("-number_of_nodes", action="store", required=False, type=int, help="Number of nodes")
    parser.add_argument("-number_of_groups", action="store", required=False, type=int, help="number of groups")
    parser.add_argument("-even_groups", action="store", required=False, type=int, help="should cities in one group have even costs")
    parser.add_argument("-max_city_ticket_price", action="store", required=False, type=int, help="max city ticket price")
    parser.add_argument("-min_city_ticket_price", action="store", required=False, type=int, help="min city ticket price")
    parser.add_argument("-max_road_ticket_price", action="store", required=False, type=int, help="max city ticket price")
    parser.add_argument("-min_road_ticket_price", action="store", required=False, type=int, help="min city ticket price")
    parser.add_argument("-max_distance", action="store", required=False, type=int, help="max distance")
    parser.add_argument("-min_distance", action="store", required=False, type=int, help="min distance")
    parser.add_argument("-test", action="store", required=False, type=int, help="If you want to enter test mode, set this argument to anything")
    return parser
