""" 
1. 对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替。
2. 对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树。
 """

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        if not root:
            return '#'
        # 先序遍历
        return str(root.val) + ',' + self.Serialize(root.left)+ ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        root, index = self.deserialize(s.split(","), 0)
        return root
    def deserialize(self,s,index):
        if s[index]=='#':
            return None,index+1
        root=TreeNode(int(s[index]))
        index += 1
        root.left, index = self.deserialize(s, index) # 递归 + 先序
        root.right, index = self.deserialize(s, index)
        return root, index