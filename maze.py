# finding possible paths for maze problem
import numpy as np
def verify_position(arr, x, y ):
    if x >= 0 and x < row:
        if y >= 0 and y < col:
            if arr[x][y] == 1:
                return True
    return False
def solve(m):
    sol = np.zeros((row, col), dtype=int)
    move = ""
    if maze_sol(arr, 0, 0, sol, move) == False:
        return False
def maze_sol(arr, x, y, sol, move):
    if x == row - 1 and y == col - 1 and arr[x][y]== 1:
        sol[x][y] = 1
        print(move, end=" ")
        return True

    if verify_position(arr, x, y) == True:
        if sol[x][y] == 1:
            return False
        sol[x][y] = 1

        if maze_sol(arr, x + 1, y, sol, move+"D") == True:
            if maze_sol(arr, x, y + 1, sol, move+"R") == True:
                sol[x][y] = 0
                return True
            sol[x][y] = 0
            return True

        if maze_sol(arr, x, y + 1, sol, move+"R") == True:
            sol[x][y] = 0
            return True

        if maze_sol(arr, x - 1, y, sol, move+"U") == True:
            sol[x][y] = 0
            return True

        if maze_sol(arr, x, y - 1, sol, move+"L") == True:
            sol[x][y] = 0
            return True
        sol[x][y] = 0
        return False
print("Enter number of rows: ")
row = int(input())
print("Enter number of columns: ")
col = int(input())
print("Enter desired configuration of maze: ")
arr=[]
for _ in range(row):
        rows = list(map(int, input().split()))
        arr.append(rows)
print("All possible moves to reach (row-1,col-1): ") 
solve(arr)
