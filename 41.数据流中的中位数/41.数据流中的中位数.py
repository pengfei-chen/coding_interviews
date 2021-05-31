# -*- coding:utf-8 -*-
class Heap:
    def __init__(self,cmp_f):   #cmp_f 堆排序方式
        self.cmp = cmp_f
        self.heap = []
    def siftDown(self,i):
        target= i
        left = 2*i + 1
        right = 2*i + 2
        if left < self.size() and self.cmp(self.heap[left],self.heap[target]):  
            # 假设这里现在是最大堆，左子节点大于当前节点，当前节点下沉到左子节点
            target = left
        if right < self.size() and self.cmp(self.heap[right],self.heap[target]):
            target = right
        if target != i:
            self.heap[target],self.heap[i] = self.heap[i],self.heap[target]  # 父子节点互换
            self.siftDown(target)   # 递归调用，直到都满足堆约束
    def size(self,):
        return len(self.heap)
    def pop(self,):
        if self.size() ==0:
            return None
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]  # 堆的最后一个元素和堆顶元素互换位置
        elem = self.heap.pop()  # 取出堆顶元素
        self.siftDown(0)   # 通过下沉方法，恢复堆顺序
        return elem
    def insert(self,num):
        self.heap.append(num)
        i = self.size() - 1   # 新加入堆的元素
        parent = (i-1)>>1   # 新加入元素的父节点
        while(i>0 and self.cmp(self.heap[i],self.heap[parent])):   # 假设self.cmp这里是取最大值，那么这里用的是 上浮 的方法；当前节点比其父节点值更大，上浮。
            self.heap[parent],self.heap[i] = self.heap[i],self.heap[parent]  # 父子节点互换位置
            i = parent
            parent = (i-1)>>1   #这两部索引更新
        
    def top(self,):
        return self.heap[0]
        
        
class Solution:
    def __init__(self,):
        self.maxHeap = Heap(lambda x,y:x>y)   #最大堆
        self.minHeap = Heap(lambda x,y:x<y)   #最小堆
    def Insert(self, num):
        # write code here
        if self.maxHeap.size() == self.minHeap.size():
                self.minHeap.insert(num)
                self.maxHeap.insert(self.minHeap.pop())   # 排序后的 前半部分数据，都在maxHeap里面
        else:
                self.maxHeap.insert(num)
                self.minHeap.insert(self.maxHeap.pop())   # 排序后的 后半部分数据，都在minHeap里面
    def GetMedian(self,n=None):
        # write code here
        if self.maxHeap.size() == self.minHeap.size():
            return (self.maxHeap.top()+self.minHeap.top())/2.0
        else:
            return self.maxHeap.top()*1.0 