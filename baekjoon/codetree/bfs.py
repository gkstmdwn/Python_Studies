from collections import deque

def bfs(graph:list, root:int):
    visited = set()
    queue = deque([root])
    visited.add(root)
    
    while queue:
        vertex = queue.popleft()
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)