from collections import deque

def openLock(deadends, target):
    deadends = set(deadends)
    visited = set()
    queue = deque([('0000', 0)])
    while queue:
        current, depth = queue.popleft()
        
        if current == target:
            return depth
        
        if current in deadends or current in visited:
            continue
        
        visited.add(current)
        
        for i in range(4):
            digit = int(current[i])
            up_digit = (digit + 1) % 10
            new_state = current[:i] + str(up_digit) + current[i+1:]            
            if new_state not in visited:
                queue.append((new_state, depth + 1))
            down_digit = (digit - 1) % 10
            new_state = current[:i] + str(down_digit) + current[i+1:]
            if new_state not in visited:
                queue.append((new_state, depth + 1))
    return -1
