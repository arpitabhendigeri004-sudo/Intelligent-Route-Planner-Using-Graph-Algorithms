from src.graph import Graph
from src.bfs_dfs import bfs, dfs
from src.dijkstra import dijkstra, shortest_path
from src.route_summary import (
    generate_route_summary,
    save_report
)
from src.visualization import visualize_graph


city = Graph()

city.add_edge("A", "B", 4)
city.add_edge("A", "C", 2)
city.add_edge("B", "D", 5)
city.add_edge("C", "D", 8)
city.add_edge("C", "E", 10)
city.add_edge("D", "E", 2)


while True:

    print("\n")
    print("=" * 50)
    print("INTELLIGENT ROUTE PLANNER")
    print("=" * 50)

    print("1. Display Graph")
    print("2. BFS Traversal")
    print("3. DFS Traversal")
    print("4. Find Shortest Route")
    print("5. Visualize Graph")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        city.display_graph()

    elif choice == "2":

        bfs(city.graph, "A")

    elif choice == "3":

        dfs(city.graph, "A")

    elif choice == "4":

        source = input(
            "\nEnter Source Node: "
        ).upper()

        destination = input(
            "Enter Destination Node: "
        ).upper()

        distances, previous = dijkstra(
            city.graph,
            source
        )

        path = shortest_path(
            previous,
            source,
            destination
        )

        if path:

            print("\nShortest Path:")
            print(" -> ".join(path))

            print(
                f"\nTotal Distance: {distances[destination]}"
            )

            summary = generate_route_summary(
                path,
                distances[destination]
            )

            print(summary)

            save_report(summary)

        else:

            print("No Path Found")

    elif choice == "5":

        visualize_graph(city.graph)

    elif choice == "6":

        print("\nThank You!")
        break

    else:

        print("\nInvalid Choice")