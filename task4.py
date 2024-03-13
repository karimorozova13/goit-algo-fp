import heapq
import random
import networkx as nx
import matplotlib.pyplot as plt

def visualize_heap(heap):
    G = nx.Graph()
    print(heap)
    for i, value in enumerate(heap):
        G.add_node(i, label=str(value))

        parent_index = (i - 1) // 2
        if parent_index >= 0:
            G.add_edge(parent_index, i)

    pos = nx.kamada_kawai_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    node_colors = ['purple' if node == 0 else 'teal' for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors, edge_color='tomato', node_size=700, font_size=8, font_color='white', font_weight='bold')
    plt.show()


if __name__ == '__main__':
    binary_heap = [random.randint(1,99) for _ in range(0, 15)]
    heapq.heapify(binary_heap)
    visualize_heap(binary_heap)