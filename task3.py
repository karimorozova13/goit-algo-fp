import heapq
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(['B', 'C', 'D', 'A', 'E', 'F', 'G', 'H', 'I'])
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'E', weight=1)
G.add_edge('A', 'G', weight=3)
G.add_edge('B', 'D',weight=7)
G.add_edge('D', 'I', weight=9)
G.add_edge('D', 'C', weight=8)
G.add_edge('E', 'H', weight=4)
G.add_edge('H', 'I', weight=6)
G.add_edge('G', 'F', weight=2)
G.add_edge('F', 'C', weight=13)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='teal', font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

def dijkstra(graph,node):
    distances={node:float('inf') for node in graph}
    distances[node]=0
    came_from={node:None for node in graph}
    queue=[(0,node)]
    
    while queue:
        current_distance,current_node=heapq.heappop(queue)
        for next_node,weight in graph[current_node].items():
            distance_temp=current_distance+weight
            if distance_temp<distances[next_node]:
                distances[next_node]=distance_temp
                came_from[next_node]=current_node
                heapq.heappush(queue,(distance_temp,next_node))
    return distances,came_from

def get_shortest_path(came_from, end_node):
    path = []
    current_node = end_node
    while current_node is not None:
        path.insert(0, current_node)
        current_node = came_from[current_node]
    return path

graph  = {
    'B':{ 'A' : 5, 'D':7, },
    'C':{ 'D':8, 'F':13}, 
    'D':{ 'C': 8, 'B': 7, 'I': 9},
    'A':{ 'B':5, 'G': 3, 'E': 1}, 
    'E':{ 'H':4, 'A':1}, 
    'F':{'C': 13, 'G':2}, 
    'G':{ 'F':2, 'A': 3}, 
    'H':{'I': 6, 'E':4}, 
    'I':{ 'D': 9, 'H':6}
}
distances,came_from = dijkstra(graph, 'A')

print(f"| {'Shortest path from->to':<30} | {'Path':<30} | {'Distance':<30} |")
print(f"| {'-'*30} | {'-'*30} | {'-'*30} |")

for target, path in distances.items():
    print(f"| {f'A ->  {target}':<30} | {' -> '.join(get_shortest_path(came_from, target)):<30} | {path:<30} |")
    
plt.show()

