from heapq import *

def dijkstra(start, finish, graph):
    queue = []
    heappush(queue,(0,start))
    visited_weight = {start: 0}
    visited = {start}

    while queue:
        current_weight, current_node = heappop(queue)
        if current_node == finish:
            break

        next_nodes = graph[current_node]
        for next_node in next_nodes:
            neigh_weight, neigh_node = next_node
            new_weight = visited_weight[current_node] + neigh_weight

            if neigh_node not in visited_weight or new_weight < visited_weight[neigh_node]
                heappush(queue,(new_weight,neigh_node))
                visited_weight[neigh_node] = new_weight
                visited[neigh_node] = current_node
    return visited



