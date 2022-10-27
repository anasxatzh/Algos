# DFS ALGORITHM:

# 1.Put all the vertices on top of a stack
# 2.Take the top item of the stack and add it to the visited list
# 3.Create a list of that vertex's adjacent nodes
# From these nodes add the ones which are not in the visited list
# ON TOP OF THE STACK (add them)
# 4.Repeat 2 and 3 until the stack is empty!

visited = set()
def dfs_alg(graph,node,visited):
    if node not in visited:
        print(node) 
        visited.add(node) 
        for neighbour in graph[node]:
            dfs_alg(graph,neighbour,visited)
            
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
print(dfs_alg(graph,'5', visited))

