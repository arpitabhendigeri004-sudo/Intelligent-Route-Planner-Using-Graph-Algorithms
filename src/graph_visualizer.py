import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph, shortest_path=None):

    G = nx.Graph()

    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 6))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3000,
        font_size=10
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

    if shortest_path:

        path_edges = list(
            zip(
                shortest_path[:-1],
                shortest_path[1:]
            )
        )

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path_edges,
            width=5
        )

    return plt