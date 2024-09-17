import matplotlib.pyplot as plt
import numpy as np
import os

    # 检查该列是否有皇后
    # 遍历当前行之前的所有行（for i in range(row)）。
    # 检查是否有皇后在同一列（board[i] == col）。
    # 检查是否有皇后在同一斜线（abs(board[i] - col) == abs(i - row)）。
    # 如果发现冲突，返回 False，否则返回 True。
def is_safe(board, row, col):
    for i in range(row):                                                       
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


    # 该函数使用递归的方法解决 N 皇后问题。
    # 输入: board（棋盘状态）、row（当前行）、solutions（存储所有解决方案的列表）。
    # 当 row 等于棋盘的长度时，表示所有皇后都已成功放置，此时将当前棋盘的状态添加到 solutions 列表中。
def solve_n_queens_util(board, row, solutions):
    if row == len(board):
        solutions.append(board.copy())
        return  
    # 遍历当前行的每一列（for col in range(len(board))）。
    # 使用 is_safe 函数检查在 (row, col) 位置放置皇后是否安全。
    # 如果安全，将当前列索引放置到 board 的当前行（board[row] = col）。
    # 递归调用 solve_n_queens_util 尝试在下一行放置皇后（row + 1）。
    # 回溯：如果放置皇后后没有找到有效的解决方案，将当前位置重置为 -1 （board[row] = -1），以便尝试其他列。
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col  # 放置皇后
            solve_n_queens_util(board, row + 1, solutions)  # 递归放置下一个皇后
            board[row] = -1  # 回溯，移除皇后



def solve_n_queens(n):
    board = [-1] * n  # 初始化棋盘，每行无皇后
    solutions = []
    solve_n_queens_util(board, 0, solutions)
    return solutions



def draw_solution(solution, index):
    n = len(solution)
    board = np.zeros((n, n))
    for row in range(n):
        board[row][solution[row]] = 1  # 将皇后位置标记为 1

    plt.imshow(board, cmap='binary')
    plt.xticks(range(n))
    plt.yticks(range(n))
    plt.gca().invert_yaxis()
    plt.grid(False)
    
    # 保存图像到本地
    filename = f"solution_{index + 1}.png"
    plt.savefig(filename)
    plt.close()  # 关闭当前图像，以释放内存
    print(f"Saved: {filename}")

# 解决8皇后问题并绘制所有解
solutions = solve_n_queens(8)
print(f"Total solutions: {len(solutions)}")  # 打印解决方案的数量
for index, solution in enumerate(solutions):
    draw_solution(solution, index)