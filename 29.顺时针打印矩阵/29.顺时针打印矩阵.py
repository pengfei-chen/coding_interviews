# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        col_start = 0
        col_end = len(matrix[0]) - 1
        row_start = 0
        row_end = len(matrix) - 1
        ans = []
        while(col_start < col_end and row_start < row_end):
            for i in range(col_start,col_end):   # 当前行的最后一个元素，没有取！
                ans.append(matrix[row_start][i])
            for i in range(row_start,row_end):   # 当前列的最后一个元素，没有取！
                ans.append(matrix[i][col_end])
            for i in reversed(range(col_start+1,col_end+1)):  # 这里的写法要注意！ 取了当前行最后一个元素，到当前行第二个元素
                ans.append(matrix[row_end][i])
            for i in reversed(range(row_start+1,row_end+1)):  # 取了当前列最后一个元素，到当前列第二个元素
                ans.append(matrix[i][col_start])
            col_start += 1
            col_end -= 1
            row_start += 1
            row_end -= 1
        if col_start == col_end:   # 此时只有一行数据
            for i in range(row_start,row_end+1):
                ans.append(matrix[i][col_start])
        elif row_start == row_end: # 此时只有一列数据
            for i in range(col_start,col_end+1):
                ans.append(matrix[row_start][i])
        return ans