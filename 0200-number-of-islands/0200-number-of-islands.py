from collections import deque

def getEdgeList(grid):
    edges = []
    graph = {}
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == '1':
                graph[(i, j)] = []
                if (j - 1) >= 0 and grid[i][j - 1] == '1':
                    edges.append(((i,j), (i, j - 1)))
                if (j + 1) < len(row) and grid[i][j + 1] == '1':
                    edges.append(((i,j), (i, j + 1)))
                if (i + 1) < len(grid) and grid[i + 1][j] == '1':
                    edges.append(((i,j), (i + 1, j)))
                if (i - 1) >= 0 and grid[i - 1][j] == '1':
                    edges.append(((i,j), (i - 1, j)))
    return edges, graph

def buildGraph(edges, graph):
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def dfs(graph, node, visited):
    st = deque()
    st.append(node)
    visited.add(node)
    while len(st) != 0:
        curr = st.pop()
        for neighbor in graph[curr]:
            if neighbor not in visited:
                st.append(neighbor)
                visited.add(neighbor)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        edges, graph = getEdgeList(grid)
        graph = buildGraph(edges, graph)

        visited = set()
        count = 0
        for node in graph:
            if node not in visited:
                dfs(graph, node, visited)
                count = count + 1
        return count