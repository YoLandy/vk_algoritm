class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # let i - code of name
        self.graph = {}

        # о от н надеюсь
        for i in range(len(accounts)):
            self.graph[i] = accounts[i][1:]

            for account in accounts[i][1:]:
                if account not in self.graph:
                    self.graph[account] = []
                self.graph[account].append(i)

        visited = []
        self.visited_now = []

        result = []

        for vertex in self.graph.keys():
            if vertex in visited:
                continue

            self.dfs(vertex)
            if isinstance(self.visited_now[0], int):
                indx = self.visited_now[0]
            else:
                indx = self.graph[self.visited_now[0]][0]

            name = accounts[indx][0]
            emails = [v for v in self.visited_now if isinstance(v, str)]
            result.append([name] + sorted(emails))

            visited += self.visited_now
            self.visited_now = []

        return result

    def dfs(self, start):
        nodes = self.graph[start]

        for node in nodes:
            if node not in self.visited_now:
                self.visited_now.append(node)
                self.dfs(node)
