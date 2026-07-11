class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        visited = set()
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for n in adj[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False
            return True

        return dfs(0, None) and len(visited) == n