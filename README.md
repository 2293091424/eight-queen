# eight-queen
回溯算法解决8皇后问题
1. Introduction
The 8 Queens Problem is a classic combinatorial optimization challenge that involves
placing 8 queens on an 8×8 chessboard so that no two queens threaten each other. This
means no two queens can share the same row, column, or diagonal. The queen, being the
most powerful chess piece, can move in any direction, making this a fundamental problem
in algorithm design and artificial intelligence.
2. Algorithm
2.1 Backtracking Algorithm
One common method for solving the 8 Queens Problem is the backtracking algorithm.
Backtracking is a trial-and-error method that explores all possible options to find a
solution. The specific steps are as follows:
1. Start from the first row and place the first queen in one of the columns.
2. Recursively place the next queen in the next row, ensuring that it does not conflict
with previously placed queens.
3. If the current placement is not valid, backtrack to the previous queen's position and
try the next column.
4. Repeat this process until all 8 queens are successfully placed.
2.2 State Checking
To ensure that queens do not threaten each other, we need to maintain three sets:
1. Column Set: Records whether a column already has a queen placed.
2. Main Diagonal Set: Records the status of the main diagonals (from top-left to
bottom-right).
3. Secondary Diagonal Set: Records the status of the secondary diagonals (from topright to bottom-left).
