'''
You are given a graph and a number x as input. Your task is to print the DFS traversal nodes of the input graph starting from node x. Complete the following function in order to give the required output.

Input Format:
The first line of input contains a list containing sets representing a graph. The second line of input contains the number x. 
Output Format:
Complete the function in order to return the required output.

Sample Input 0:
[[1,0],[2,0],[3,0],[3,2]]
3

Sample Output 0:
3 0 2 
'''

def dfs_traversal(visited, graph, node):  
    if node not in visited:
        print (node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs_traversal(visited, graph, neighbour)

graph = [[1,0],[2,0],[3,0],[3,2]]
visited = set() 
node_start = int(input(""))
dfs_traversal(visited, graph,node_start)
 