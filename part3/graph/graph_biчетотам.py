# ниче крутого не придумал, просто с семинара решение


class Solution:
    def isBipartite(self, graph):
        self.visited = []
        queue = [0]
        color = [None for _ in range(len(graph))]
        color[0] = True

        for i in range(len(graph)):
            if color[i] is None:
                if not self.bfs(graph, i):
                    return False
        return True

    def bfs(self, graph, start):
        queue = [start]
        color = [None for _ in range(len(graph))]
        color[start] = True
        while queue:
            vertex = queue.pop()
            self.visited.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    color[neighbor] = not color[vertex]
                else:
                    if color[neighbor] == color[vertex]:
                        return False
        return True
