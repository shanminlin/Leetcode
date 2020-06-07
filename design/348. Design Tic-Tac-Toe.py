#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Design a Tic-tac-toe game that is played between two players on a n x n grid.
# 
# You may assume the following rules:
# 
# A move is guaranteed to be valid and is placed on an empty block.<br>
# Once a winning condition is reached, no more moves is allowed.<br>
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

# # Brainstorms
# 
# We need to keep track of variables that describe the status of the board:
# - number of marks each player places in each row, column and diagonal.
