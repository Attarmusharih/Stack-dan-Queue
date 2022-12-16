stack = [1,2,3,4,5,6]
print('present data: ',stack)

stack.append(7)
print('received data: ',7)
print('present data: ',stack)
stack.append(8)
print('received data: ',8)
print('received data: ',stack)

out = stack.pop()
print('reduce data: ',out)
print('present data: ',stack)