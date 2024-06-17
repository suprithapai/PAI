import sys

def prim_algorithm():
    n = int(input("Enter the number of vertices: "))

    if n == 0:
        print("Number of vertices is 0. Exiting.")
        return

    cost = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)

    print("Enter the graph data:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost[i][j] = int(input(f"({i},{j}): "))
            if cost[i][j] == 0:
                cost[i][j] = sys.maxsize  # Use a large number to represent no edge

    visited[1] = True  # Start from the first vertex
    ne = 1
    mincost = 0
    print("The edges of the spanning tree are:")

    while ne < n:
        min_cost = sys.maxsize
        a = -1
        b = -1

        for i in range(1, n + 1):
            if visited[i]:
                for j in range(1, n + 1):
                    if not visited[j] and cost[i][j] < min_cost:
                        min_cost = cost[i][j]
                        a = i
                        b = j

        if a != -1 and b != -1:
            print(f"{ne}: Edge ({a},{b}) = {min_cost}")
            mincost += min_cost
            visited[b] = True
            cost[a][b] = cost[b][a] = sys.maxsize  # Reset the cost to prevent re-selection
            ne += 1

    print(f"Minimum cost is {mincost}")

if __name__ == "__main__":
    prim_algorithm()
