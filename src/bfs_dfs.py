from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("\nBFS Traversal:")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print()


def dfs(graph, start, visited=None):

    if visited is None:
        visited = set()
        print("\nDFS Traversal:")

    visited.add(start)

    print(start, end=" ")

    for neighbor, weight in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited