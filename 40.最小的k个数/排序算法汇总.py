# 冒泡排序
from random import randint


def bubbleSort(alist):
    n = len(alist)
    for i in range(n-1, 0, -1):   # 不用取到第一个元素
        for j in range(0,i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

"""
但是，由于冒泡排序要遍历整个未排好的 部分，它可以做一些大多数排序方法做不到的事。
尤其是如果在整个排序过程中没有交换，我们就可断定列表已经排好。
因此可改良冒泡排序，使其在已知列表排好的情况下提前结束。
这就是说，如果一个列表只需要几次遍历就可排好，冒泡排序就占有优势：它可以在发现列表已排好时立刻结束。
"""
# 冒泡排序优化
def bubbleSort_optimize(alist):
    n = len(alist)
    for i in range(n-1,0,-1):
        exchange = False
        for j in range(0,i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                exchange = True   # 一直没有到这一步，说明一直没有发生交换，前面的已经是有序的了。
        if not exchange:
            break
    return alist

# 选择排序
def selectionSort(alist):
    n = len(alist)
    for i in range(n-1):
        # 寻找[i,n]区间里的最小值
        min_index = i
        for j in range(i+1,n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index],alist[i]
    return alist

#插入排序
def insertionSort(alist):
    for i in range(1,len(alist)):
        currentvalue = alist[i]
        position = i
        while alist[position-1] > currentvalue and position > 0:
            alist[position] = alist[position-1]  # 这个比较大的值，往后挪一位
            position  = position - 1   # 索引往前走一位
        alist[position] = currentvalue   # 把当前值，插入到合适的位置
    return alist

"""
希尔排序
有时又叫做 “缩小间隔排序”，它以插入排序为基础，将原来要排序的列表划分为一些子列表，再对每一个子列表执行插入排序，
从而实现对插入排序性能的改进。划分子列的特定方法是希尔排序的关键。
我们并不是将原始列表分成含有连续元素的子列，而是确定一个划分列表的增量 “i”，这个i更准确地说，
是划分的间隔。然后把每间隔为i的所有元素选出来组成子列表，然后对每个子序列进行插入排序，
最后当 i=1 时，对整体进行一次直接插入排序。
"""
# 希尔排序
def shellSort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap):
            gapInsetionSort(alist,i,gap)
        gap = gap // 2
    return alist

def gapInsetionSort(alist,startpos,gap):
    # 希尔排序的辅助函数
    for i in range(startpos+gap, len(alist), gap):
        position = i
        currentvalue = alist[i]

        while position > startpos and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap] # position - gap 位置的值往后推 gap 个位置
            position = position - gap
        alist[position] = currentvalue   # 小的值往前推 gap 位

"""
希尔排序这么做，有意义嘛？
"""

"""
归并排序是一种递归算法，它持续地将一个列表分成两半。
如果列表是空的或者 只有一个元素，那么根据定义，它就被排序好了（最基本的情况）。
如果列表里的元素超过一个，我们就把列表拆分，然后分别对两个部分调用递归排序。
一旦这两个部分被排序好了，然后就可以对这两部分数列进行归并了。
归并是这样一个过程：把两个排序好了的列表结合在一起组合成一个单一的有序的新列表。
有自顶向下（递归法）和自底向上的两种实现方法。
"""
# 归并排序：自顶向下（递归法）方法实现
def mergeSort(alist):
    n = len(alist)
    __mergeSort(alist, 0 ,n-1)
    return alist
# 对arr[l......r]的范围进行排序
def __mergeSort(alist,start, end):
    # 当数列的大小比较小的时候，数列近乎有序的概率较大
    if(end-start <= 15):
        insertionSortHelp(alist,start,end)
        return
    if start > end:
        return
    # 存在风险，start + end 可能越界
    mid = (start + end ) // 2
    __mergeSort(alist,start,mid)
    __mergeSort(alist,mid+1,end)
    # 优化
    if alist[mid] > alist[mid+1]:   # 为什么是这里要这样？  判断当前alist 是否有序？ 若无序，则归并
        merge(alist,start,mid,end)

def merge(alist,start,mid,end):   # merge这里写得并不好
    # 复制一份
    blist = alist[start:end+1]
    l = start   # 这里写得不容易理解  l 表示左半边元素
    r = mid +1  # r 表示右半边元素
    pos = start  # 当前位置索引

    while pos <= end:   # 从start 到 end 遍历新的blist   # z注意这里的  -start
        if(l > mid):   #左边用尽，取右半边的元素
            alist[pos] = blist[l-start]
            r += 1
        elif(r>end):  #右边用尽，取左半边的元素
            alist[pos] = blist[l-start]
            l += 1
        elif blist[l-start] <= blist[r-start]:  #左半边当前元素小于右半边当前元素，取左半边
            alist[pos] = blist[l-start]
            l += 1
        else:
            alist[pos] = blist[r-start]   #右半边当前元素小于左半边当前元素，取右半边
            r += 1
        pos += 1
# 插入排序，帮助获取排序好的数组
def insertionSortHelp(alist,l,r):
    for i in range(l+1, r+1):
        currentvalue = alist[i]
        position = i
        while alist[position-1] > currentvalue and position>l:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue
    return alist

# 自底向上（非递归法）方法
def mergeBU(alist):
     n = len(alist)
     # 归并规模从 1 开始
     size = 1
     while size <= n:
         for i in range(0,n-size,size+size):
             merge(alist, i, i+size-1,min(i+size+size-1, n-1))   #这里要理解，记住。
         size += size
     return alist


"""
快速排序由 C. A. R. Hoare 在1962年提出。
它的基本思想是：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
"""

def quickSort(alist,l,r):
    if l>r:
        return
    p = partition(alist,l,r)
    quickSort(alist,l,p-1)
    quickSort(alist,p+1,r)
    return alist

# 在alist[l...r]中寻找j,使得alist[l...j] <= alist[l], alist[j+1...r] >alist[l]
def partition(alist,l,r):
    pos = randint(l,r)
    alist[pos],alist[l] = alist[l],alist[pos]
    v = alist[l]
    j = l
    i = l + 1
    while i <= r:
        if alist[i] <= v:
            alist[j+1],alist[i] = alist[i],alist[j+1]   # 只要值小于 v，往 j+1 放
            j += 1
        i += 1
    alist[l],alist[j] = alist[j],alist[l]   # 因为经过上面的形式后，列表成为 5,2,3,4,1,6,7,9,8  这样的形式，现在l=0，j=4
    return j


if __name__ == '__main__':
    alist = [2,9,5,8,3,4,6,1,7]
    # ans = bubbleSort(alist)
    # ans = bubbleSort_optimize(alist)
    # ans = selectionSort(alist)
    # ans = insertionSort(alist)
    # ans = shellSort(alist)
    # ans = mergeSort(alist)
    # ans = mergeBU(alist)
    ans = quickSort(alist,0,8)
    print(ans)

