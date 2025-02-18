def bfs (graph, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            queue.extend(graph.get(node, []))

def dfs (graph, start, visited = set()):
    if start not in visited:
        print(start, end = " ")
        visited.add(start)
        for neighbor in graph.get(start, []):
            dfs(graph, neighbor, visited)

graph = {1: [2, 3], 2:[4], 3: [], 4: []}
print("\nBFS:")
bfs(graph, 1)
print("\nDFS")
dfs(graph, 1)