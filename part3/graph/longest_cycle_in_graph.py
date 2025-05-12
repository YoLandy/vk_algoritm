class Solution:
    def longestCycle(self, edges):
        n = len(edges)
        visited = [False] * n
        max_cycle = -1

        for node in range(n):
            if not visited[node]:
                # Track the path to detect cycles
                path = {}
                current = node
                length = 0

                while current != -1:
                    if visited[current]:
                        # Check if the current node is in the current path (cycle detected)
                        if current in path:
                            cycle_length = length - path[current]
                            max_cycle = max(max_cycle, cycle_length)
                        break

                    visited[current] = True
                    path[current] = length
                    current = edges[current]
                    length += 1

        return max_cycle


# сверху - это то что у дипсика попросил оптимизировать, ниже - мое оригинальное
class Solution:
    def longestCycle(self, edges):
        n = len(edges)
        self.visited = []

        cycle_lengths = []

        for i in range(len(edges)):
            if i in self.visited:
                continue

            cycle_lengths.append(self.get_cycle_length(edges, i))

        return max(cycle_lengths)

    def get_cycle_length(self, edges, i):

        cycle = []

        if i == -1:
            return -1

        length = 0

        while True:
            next_i = edges[i]
            edges[i] = length
            self.visited.append(i)
            cycle.append(i)
            if next_i == -1:
                return -1

            if next_i in cycle:
                return length - edges[next_i] + 1

            if next_i in self.visited:
                return -1

            i = next_i
            length += 1
