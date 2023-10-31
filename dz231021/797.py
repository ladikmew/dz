class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        finish = len(graph)-1
        def dfs(cur_node, path, res):
            if cur_node==finish:
                res.append(path)

            for next in graph[cur_node]: 
                dfs(next,path+[next] ,res)

        res = []
        dfs(0,[0],res)
        return res
