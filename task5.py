import heapq
import random
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def visualize_heap(heap, colors):
    G = nx.Graph()
    for i, value in enumerate(heap):
        color = colors.get(value, 'red')
        G.add_node(i, label=str(value), color=color)

        parent_index = (i - 1) // 2
        if parent_index >= 0:
            G.add_edge(parent_index, i)
    
    pos = nx.kamada_kawai_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    node_colors = [G.nodes[node]['color'] for node in G.nodes()]
    
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors, edge_color='tomato', node_size=700, font_size=8, font_color='white', font_weight='bold')
    plt.show()
    
    
def breadth_first_search(graph, queue, visited=None, colors={}, i=0):
    if visited is None:
        visited = set()
    if not queue:
        return
  
    vertex = queue.popleft()
    
    if vertex not in visited:
        print(vertex, end=' ')
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
        colors[vertex] = initial_colors[i]
        i += 1
      
    breadth_first_search(graph, queue, visited, colors, i)
    return  colors

def depth_first_search(graph, vertex, visited=None, colors={}, i=0):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    colors[vertex] = initial_colors[i]
    i += 1
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            
            depth_first_search(graph, neighbour, visited, colors, i)
    return colors

binary_heap = {random.randint(1,99) for _ in range(0, 15)}
binary_heap = list(binary_heap)
heapq.heapify(binary_heap)
graph ={}
print(binary_heap)
for i, value in enumerate(binary_heap):
    graph[value] = [binary_heap[(2*i + 1) % len(binary_heap)], binary_heap[(2*i + 2) % len(binary_heap)]]
    
initial_colors = [
    '#003333', '#004d4d', '#006666', '#008080', '#009999',
    '#00b3b3', '#00cccc', '#00e6e6', '#00ffff', '#1affff',
    '#33ffff', '#4dffff', '#66ffff', '#80ffff', '#99ffff'
]

colors_bfs = breadth_first_search(graph, deque([binary_heap[0]]))
# colors_dfs = depth_first_search(graph, binary_heap[0])

visualize_heap(binary_heap, colors_bfs)
# visualize_heap(binary_heap, colors_dfs)


