import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G=nx.Graph()

# Add nodes and edges
#G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12])
#G.add_edges_from([(1,2), (2,3), (3,4), (4,5), (4,6), (6,7), (8,9),(8,10), (9,10), (9,11),(10,12)])

# for confirming its a breadth first search 
#G.add_nodes_from([1,2,3,4])
#G.add_edges_from([(1,2), (2,4), (1,3), (3,4)])

# Example 1
#G.add_nodes_from([1,2,3,4,5])
#G.add_edges_from([(1,2), (2,4), (1,3), (3,4), (4,5)])

# Example 2
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2), (2,4), (2,3), (2,3), (3,4), (4,5)])



# Dsiplay the network
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show(block=False)


A=nx.to_dict_of_dicts(G) # Get adjacency matrix as dictionary of dictionaries

# Breadth First Search function
def bfsearch(graph, v, w):
    q = deque()         # initialize the queue
    visited = set()     # initialize visited list
    path = {}           # initialize the path from v to each visited node
    q.append(v)         # add source to the queue

    connection = False  
    while q:
        #print(q)
        vertex = q.popleft()    # extract 1st element of the queue
        #print(vertex)
        visited.add(vertex)     # add the vertex to visited list

        # iterating over all the neighbours of given vertex
        for neighbor in graph[vertex]:
            #print(neighbor)
            if neighbor == w:   # if destination is found, break 
                connection = True
                path[neighbor] = vertex  # Store the parent of the destination vertex
                break

        if connection:
            break  # Break out of the while loop as well

        for neighbor in graph[vertex]:
            if neighbor not in visited: #if neighbour is not visited
                path[neighbor] = vertex
                visited.add(neighbor)
                q.append(neighbor)

    if connection:
        print(path)
        return 1, reconstruct_path(path, v, w)
    else:
        return 0, []

def reconstruct_path(path, start, end):
    result = []
    current = end
    while current != start:
        result.insert(0, current)
        current = path[current]
    result.insert(0, start)
    return result


while True:
    user_input = input("Enter start and end nodes (format: a b), or 'exit' to quit: ").strip().lower()

    if user_input == 'exit':
        break

    try:
        a, b = map(int, user_input.split())
        result, path = bfsearch(A, a, b)

        if result:
            print(f"Connection found. Path: {path}")
        else:
            print("No connection found.")

    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
