class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # Iterate through pairs of inputs (i and i + 1)
        # strings a and b
        # if a[i] == b[i]: continue
        # if a[i] != b[i]: insert edge [a[i], b[i]]

        # Not sure how to handle the size discrepancy issue

        edges = []

        totalLetters = set()
        for word in words:
            for letter in word:
                totalLetters.add(letter)

        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            for j in range(max(len(a), len(b))):
                if j >= len(b):
                    return ""
                
                if j >= len(a):
                    break
                
                if a[j] == b[j]:
                    continue 
                
                if a[j] != b[j]:
                    edges.append([a[j], b[j]])
                    break
        
        print(edges)
        
        graph = defaultdict(list)

        indegree = defaultdict(int)

        for letter in totalLetters:
            graph[letter] = []
            indegree[letter] += 0

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        print(indegree)

        topo_sort = []

        q = deque()

        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            curr_node = q.popleft()
            topo_sort.append(curr_node)

            for nei in graph[curr_node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        print(topo_sort)
        if len(topo_sort) != len(list(graph.keys())):
            return ""
        
        return "".join(topo_sort)
        
        

        