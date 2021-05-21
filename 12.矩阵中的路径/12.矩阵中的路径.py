#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix char字符型二维数组 
# @param word string字符串 
# @return bool布尔型
#
class Solution:
    def hasPath(self , matrix , word ):
        # write code here
        if len(matrix) == 0 or len(matrix[0]) == 0 or len(word) == 0:
            return False
        self.res = False
        def dfs(start,visit,row,col):
            if start == len(word):
                self.res = True  #如果start能走到和查询字符串一样的长度，则res为真
                #  只要有一条路径能走通，res 就会一直是 True
                return 
            if not (col>=0 and col < len(matrix[0]) and row>=0 and row <len(matrix)):
                # 这其中的任何一个条件不满足，直接返回
                return 
            matrix[row][col]
            word[start]
            visit[row][col]
            if matrix[row][col] != word[start] or visit[row][col]==True:
                # 如果矩阵中当前元素的值不等于查询字符串中的值 或 visit 中已经对应为True
                return 
            visit[row][col] = True   # 如果上述情况都没有发生
            # 那就标记这个点，说明这个点已经被 用 过了
            dfs(start+1,visit[:],row-1,col) #向下
            dfs(start+1,visit[:],row+1,col) #向上
            dfs(start+1,visit[:],row,col-1) #向左
            dfs(start+1,visit[:],row,col+1) #向右
            visit[row][col] = False   #这一步一定要记得！ 复原当前步骤用过的标记
            # 因为复原当前节点的标记，不会再影响走当前路径的结果。
            # 但是如果不复原，其他路径有可能会用到当前节点，但当前节点被标记为 True(已使用)，从而影响结果。
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visit = [[False for m in range(len(matrix[0]))] for n in range(len(matrix))]
                dfs(0,visit,i,j)  # 不知道哪个点是 word 字符串的起点，遍历之
        return self.res