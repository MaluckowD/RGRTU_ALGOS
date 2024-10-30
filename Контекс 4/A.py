class MaxHeap:
  def __init__(self):
    self.heap = [0]
    self.size = 0
  
  def shiftUp(self, i):
    while (i // 2 > 0) and self.heap[i] < self.heap[i // 2]:
      self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
      i = i // 2
  
  def insert(self, x):
    self.heap.append(x)
    self.size += 1
    self.shiftUp(self.size)
  
  def shiftDown(self, i):
    while i * 2 <= self.size:
      j = self.intMaxChild(i)
      if self.heap[i] > self.heap[j]:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
      i = j
  
  def intMaxChild(self, i):
    if i * 2 + 1 > self.size:
      return i * 2
    if self.heap[i * 2] > self.heap[i * 2 + 1]:
      return i * 2
    
    return i * 2 + 1
  
  def delMax(self):
    if self.size == 0:
      return None
    removed = self.heap[1]
    self.heap[1] = self.heap[self.size]
    self.size -= 1
    self.heap.pop()
    self.shiftDown(1)
    return removed

heap = MaxHeap()
N = int(input())
for i in range(N):
  lst = list(map(int, input().split()))
  if lst[0] == 0:
    heap.insert(lst[1])
  else:
    print(heap.delMax())
    
      
    