# https://e-maxx.ru/algo/floyd_warshall_algorithm


def shortest(graph):
    # graph is list of adjacent vertices
    size = len(graph)
    dp = [[1e9 if i != j else 0 for j in range(size)] for i in range(size)]
    for i, node in enumerate(graph):
        for v in node:
            dp[i][v] = 1  # 1 is weight of this path

    for k in range(size):
        for i in range(size):
            for j in range(size):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # each dp[i][j] is the shortest path between i and j nodes
    # the value of 1e9 means there is no path
    return dp
