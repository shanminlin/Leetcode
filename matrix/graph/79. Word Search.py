#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.<br>
# 
# Example:<br>
# board =<br>
# [<br>
#   ['A','B','C','E'],<br>
#   ['S','F','C','S'],<br>
#   ['A','D','E','E']<br>
# ]
# 
# Given word = "ABCCED", return true.<br>
# Given word = "SEE", return true.<br>
# Given word = "ABCB", return false.<br>
#  
# 
# Constraints:
# - board and word consists only of lowercase and uppercase English letters.
# - 1 <= board.length <= 200
# - 1 <= board[i].length <= 200
# - 1 <= word.length <= 10^3

# In[ ]:


def exist(board, word):
    seen = set()
    nrow = len(board)
    ncol = len(board[0])

    for row in range(nrow):
        for col in range(ncol):
            if board[row][col] == word[0]:
                dfs(board, word, row, col)

def dfs(board, word, row, col):

    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or not word:
        return False

    if board[row][col] == word[0]:
        dfs(board, word[1:], row-1, col)
        dfs(board, word[1:], row+1, col)
        dfs(board, word[1:], row, col+1)
        dfs(board, word[1:], row, col-1)

