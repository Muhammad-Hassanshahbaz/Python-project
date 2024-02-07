import sys
import os
import data
import matplotlib.pyplot as plt
import networkx as nx


def clear_screen():
    os.system('cls')


def mode_of_transportation(option):
    match option:
        case 1:
            return 2
        case 2:
            return 0
        case 3:
            return 1
        case 4:
            return 3
        case _:
            return -1
    

def shortest_path(graph, starting_point, hospitals, extra_cost):
    infinite = sys.maxsize
    nodes_queue = []
    visited = []
    nodes_queue.append(starting_point)

    node_data = {}
    for key, value in graph.items():
        node_data[key] = {'cost': infinite, 'pred': []}

    node_data[starting_point]['cost'] = 0
    while nodes_queue:
        temp = nodes_queue.pop(0)
        if temp not in visited:
            visited.append(temp)
            for j in graph[temp]:
                nodes_queue.append(j)
                cost = node_data[temp]['cost'] + graph[temp][j] + extra_cost
                if cost < node_data[j]['cost']:
                    node_data[j]['cost'] = cost
                    node_data[j]['pred'] = node_data[temp]['pred'] + [temp]

    max_time = sys.maxsize

    for hospital in hospitals:
        if node_data[hospital]['cost'] < max_time:
            closest = hospital
            max_time = node_data[hospital]['cost']

    max_time_2 = sys.maxsize

    for hospital in hospitals:
        if node_data[hospital]['cost'] > max_time and node_data[hospital]['cost'] < max_time_2:
            second_closest = hospital
            max_time_2 = node_data[hospital]['cost']


    print("The route for the closest hospital to your location is:  " +
          str(node_data[closest]['pred'] + [closest]))
    print("Total time to travel: " + str(node_data[closest]['cost']) + " mins")
    print("\n ------------------------------------------------------------------------------------------- \n")
    print("The route for the second closest hospital to your location is:  " +
          str(node_data[second_closest]['pred'] + [second_closest]))
    print("Total time to travel: " +
          str(node_data[second_closest]['cost']) + " mins")


    G = nx.Graph(graph)
    pos = nx.spring_layout(G)

    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", edge_color="gray", linewidths=0.5, arrowsize=10)

    # Highlight the shortest path
    if len(node_data[closest]['pred']) != 0:
        shortest_path_edges = [(node_data[closest]['pred'][i], node_data[closest]['pred'][i+1]) for i in range(len(node_data[closest]['pred'])-1)]
        shortest_path_edges.append((node_data[closest]['pred'][-1], closest))
        nx.draw_networkx_nodes(G, pos, nodelist=node_data[closest]['pred'] + [closest], node_color="orange", node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color="orange", width=2)
    else:
        shortest_path_edges = [(node_data[second_closest]['pred'][i], node_data[second_closest]['pred'][i+1]) for i in range(len(node_data[second_closest]['pred'])-1)]
        shortest_path_edges.append((node_data[second_closest]['pred'][-1], second_closest))
        nx.draw_networkx_nodes(G, pos, nodelist=node_data[second_closest]['pred'] + [second_closest], node_color="orange", node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color="orange", width=2)



    plt.show()

if __name__ == "__main__":

    area_option = [dt for dt in data.graph.keys()]

    mode = mode_of_transportation(int(input(
        "Select your mode of transportation:\n1. Car\n2. Bike\n3. Auto\n4. By Walk\t")))

    while mode == -1:
        print("Select a Valid Option.")
        mode = mode_of_transportation(int(input(
            "Select your mode of transportation:\n1. Car\n2. Bike\n3. Auto\n4. By Walk")))
    clear_screen()

    for i in range(len(area_option)):
        print(f"{i+1}: {area_option[i]}")

    index = int(input("Enter the index no. of the area to select: "))
    
    shortest_path(data.graph, area_option[index-1], data.hospitals, mode)
