import heapq


def dijkstra(graph, start):

    distances = {
        node: float("inf")
        for node in graph
    }

    distances[start] = 0

    previous = {}

    pq = [(0, start)]

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                previous[neighbor] = current_node

                heapq.heappush(
                    pq,
                    (distance, neighbor)
                )

    return distances, previous


def shortest_path(previous, start, end):

    path = []

    current = end

    while current != start:

        path.append(current)

        if current not in previous:
            return None

        current = previous[current]

    path.append(start)

    path.reverse()

    return path