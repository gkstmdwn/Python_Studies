# https://www.codetree.ai/missions/2/problems/determine-escapableness-with-2-ways/introduction

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

def possibility(x, y):
    if not (0 <= x and x < N and 0 <= y and y < M):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True


def dfs(x, y):
    dxs, dys = [0, 1], [1, 0]
    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
        if possibility(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

if __name__ == "__main__":
    visited[0][0] = 1
    dfs(0, 0)
    print(visited[N-1][M-1])