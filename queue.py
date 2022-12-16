from collections import deque 

queue = deque([1,2,3,4,5])

print('Present Data: ',queue)

queue.append(6)
print('received data: ',6)
print('present data: ',queue)

queue.append(7)
print('received data: ',7)
print('present data: ',queue)

out = queue.popleft()
print('reduce data: ',out)
print('in data: ',queue)