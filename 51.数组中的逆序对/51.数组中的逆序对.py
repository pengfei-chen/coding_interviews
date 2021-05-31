# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        length = len(data)
        if length <= 1:
            return 0
        copy = data[:]  # 占位   # 靠，原来是这里被坑了！  这里才不是占位！
        count = self.InversePairsCore(data,copy,0,length-1)
        return count % 1000000007
    
    def InversePairsCore(self,data,copy,start,end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) / 2 
        left = self.InversePairsCore(copy,data,start,start+length)   #copy中有一部分已经排好序了，成为新的data
        right = self.InversePairsCore(copy,data,start+length+1,end)   # data 还是原来的样子，成为新的用来辅助的copy
        i = start + length  #从右往左比
        j = end
        indexcopy = end
        count = 0
        while (i>=start and j >= start+length+1):
            if(data[i] > data[j]):
                copy[indexcopy] = data[i]
                indexcopy -=1
                i -=1
                count = count + j - (start+length)
            else:   #右边大于左边，这一次比较没有逆序对
                copy[indexcopy] = data[j]
                indexcopy -=1
                j -= 1
        # 同时满足上面两者的已经走完了，可能还余下左边数组，或者余下右边数组
        while i >= start:
            copy[indexcopy] = data[i]
            indexcopy -= 1
            i -= 1
        while j >= start + length +1:
            copy[indexcopy] = data[j]   # 现在 copy 已经成为部分排序后的data了
            indexcopy -= 1
            j -= 1
        return  left + right + count


# 通过答案
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        temp = [i for i in data]
        return self.mergeSort(temp, data, 0, len(data)-1) % 1000000007
       
    def mergeSort(self, temp, data, low, high):
        if low >= high:
            temp[low] = data[low]
            return 0
        mid = (low + high) / 2
        left = self.mergeSort(data, temp, low, mid)
        right = self.mergeSort(data, temp, mid+1, high)
           
        count = 0
        i = low
        j = mid+1
        index = low
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:   # i 已经逆序了，后面比i大的也全都逆序了，一直到mid
                temp[index] = data[j]
                count += mid-i+1   # 这一步很关键
                j += 1
            index += 1
        while i <= mid:
            temp[index] = data[i]
            i += 1
            index += 1
        while j <= high:
            temp[index] = data[j]
            j += 1
            index += 1
        return count + left + right
    