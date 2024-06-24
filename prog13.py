def read_matrix(n):
    cost = [[999] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost[i][j] = int(input(f"({i},{j}): "))
            if cost[i][j] == 0:
                cost[i][j] = 999
    return cost

def min_distance(a, b):
    return min(a, b)

def shortest_path(n, s, cost):
    dist = [999] * (n + 1)
    vis = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dist[i] = cost[s][i]
    
    dist[s] = 0
    vis[s] = 1
    
    for _ in range(1, n + 1):
        c = 999
        u = -1
        
        for i in range(1, n + 1):
            if vis[i] == 0 and dist[i] <= c:
                c = dist[i]
                u = i
                
        if u == -1:
            break
        
        vis[u] = 1
        
        for i in range(1, n + 1):
            dist[i] = min_distance(dist[i], dist[u] + cost[u][i])
    
    return dist

def main():
    n = int(input("Enter the number of vertices: "))
    
    if n == 0:
        print("Number of vertices is zero. Exiting...")
        return
    
    print("Enter the cost adjacency matrix (999 for infinite):")
    cost = read_matrix(n)
    
    s = int(input("Enter the source vertex: "))
    
    dist = shortest_path(n, s, cost)
    
    for i in range(1, n + 1):
        print(f"The shortest path between vertex {s} and {i} is {dist[i]}")

if __name__ == "__main__":
    main()
