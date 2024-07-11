#INPUTS
# matrix W represents the graph

w = [[0, 2, 2, 1, 4],
     [2, 0, 3, 2, 3],
     [2, 3, 0, 2, 2],
     [1, 2, 2, 0, 4],
     [4, 3, 2, 4, 0]]

# the vertex that we want to find the minimum cycle for

destination = 0 
#-----------------------------------------------------------


n = len(w) # number of verticse
vertices = list(range(n)) # index of each vertex
cost = [[-1]*(2**(n-1)) for _ in range(n)] # the cost to move from vertex i to the destination while mving only once and exactly once form the given set of vertices

def all_subcombinations(nums):
     results = []
  
     def dfs(i, curr_list):
          results.append(curr_list.copy())
          for j in range(i, len(nums)):
               curr_list.append(nums[j])
               dfs(j + 1, curr_list)
               curr_list.pop()

     dfs(0, [])
     return results

vertices.remove(destination)
col_list = all_subcombinations(vertices)

def find_col(list):
     global col_list
     return col_list.index(list)
   

def D(vertex, vertex_list, destination, w, cost) -> list:
     if  not vertex_list:
         cost[vertex][0] = w[vertex][destination]
         return [destination]
     else:
          min = 10**6 - 1 # a big number
          k = 0
          path = [0]
          for i in vertex_list:
               if w[vertex][i] == -1: continue
               A = vertex_list.copy()
               A.remove(i)
               col = find_col(A)
               if cost[i][col] == -1:
                    p = D(i, A, destination, w, cost)
               else:
                    p = []
               x = w[vertex][i] + cost[i][col]
               if min > x:
                    min = x
                    k = i
                    path = p + [k]
          cost[vertex][find_col(vertex_list)] = min
          return path


p = D(destination, vertices, destination, w, cost)

print(f"sum of costs: {cost[destination][n-1]}")
print("the path:")

print([destination] + list(reversed(p)) + [destination])