inverseIndex = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
}

distanceGraph = {
    "A": [0, 2, 0, 0, 0, 0, 6, 0],
    "B": [2, 0, 7, 0, 2, 0, 0, 0],
    "C": [0, 7, 0, 3, 0, 3, 0, 0],
    "D": [0, 0, 3, 0, 0, 0, 0, 2],
    "E": [0, 2, 0, 0, 0, 2, 1, 0],
    "F": [0, 0, 3, 0, 2, 0, 0, 2],
    "G": [6, 0, 0, 0, 1, 0, 0, 4],
    "H": [0, 0, 0, 2, 0, 2, 4, 0]
}

def findConnections(graph, source):
    connections = []
    for index, node in enumerate(graph[source]):
        if node != 0:
            connections.append(inverseIndex[index])
    return connections

def shortestPath(graph, source, destination):
    distances = {}

    for node in graph:
        distances[node] = float("inf")

    distances[source] = 0
    previous = {}
    visited = []

    while len(visited) < len(graph):
        current = None

        for node in graph:
            if node not in visited:
                if current is None or distances[node] < distances[current]:
                    current = node

        if current is None or distances[current] == float("inf"):
            break

        if current == destination:
            break

        visited.append(current)

        for node in findConnections(graph, current):
            if node not in visited:
                index = list(inverseIndex.keys())[list(inverseIndex.values()).index(node)]
                newDistance = distances[current] + graph[current][index]

                if newDistance < distances[node]:
                    distances[node] = newDistance
                    previous[node] = current

    if distances[destination] == float("inf"):
        print("No path found")
        return

    path = []
    current = destination

    while current != source:
        path.append(current)
        current = previous[current]

    path.append(source)
    path.reverse()
    print("Path:", path)
    print("Distance:", distances[destination])

shortestPath(distanceGraph, "A", "D")
