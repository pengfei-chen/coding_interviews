# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        ss = sorted(list(ss))
        used = [False] * len(ss)
        self.ans = []
        def dfs(temp,used):
            # 走完所有可能，记录排列
            if len(temp) == len(ss):
                self.ans.append("".join(temp))  #所有字母全都在temp里面了，结束当前方法
                return   # 返回上一步
            # 遍历整个序列，尝试每一种可能。
            for i in range(len(ss)):
                # 是否走过  used[i]  等于 True,则表示已经走过
                if (i>0 and ss[i] == ss[i-1] and used[i-1]==False) or used[i]:   # 这里第一个括号里面的条件，很难想明白。
                    continue
                temp.append(ss[i])
                used[i] = True
                dfs(temp,used)   # 在这一个DFS里面，i 一直是used的状态。
                temp.pop()   # 当前节点遍历完了，返回到上一节点。   # append, pop  这里用到了栈
                # 走完最后一步，后退一步
                used[i] = False
        dfs([],used)
        return self.ans