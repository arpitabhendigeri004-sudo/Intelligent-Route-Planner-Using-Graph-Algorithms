import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph):

    G = nx.Graph()

    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    plt.figure(figsize=(8, 6))

    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        font_size=12
    )

    edge_labels = nx.get_edge_attributes(
        G,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels
    )

    plt.title(
        "Intelligent Route Planner Using Graph Algorithms"
    )

    plt.savefig(
        "images/graph_visualization.png"
    )

    plt.show()