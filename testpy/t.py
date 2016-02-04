# from collections import deque
# def search(lines,pattern,history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)
# if __name__ == '__main__':
#     with open('E:\\Desktop\\testpy\\somefile.txt') as f:
#         for line,prevlines in search(f,'python',5):
#             for pline in prevlines:
#                 print(pline,end="")
#             print(line,end="")
#             print('-'*20)

import heapq
class Priority:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)
class Item(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
