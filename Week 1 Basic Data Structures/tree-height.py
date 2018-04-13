# python3

import sys
import threading

def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    queue = []

    tree = {}
    
    #check if tree is empty
    if n == 0:
        return max_height

    else:
        
        #create dict 
        for i in range(n):
            tree[i] = []
        
        #create tree     
        for i in range(n):
            if parents[i] == -1:
                pass
            else:
                tree[parents[i]] += [i]

        #insert root into queue
        queue.append(parents.index(-1))

        #loop forever until break
        while True:
            node_count = len(queue)
            
            if len(queue) == 0:
                return max_height

            max_height += 1
            
            while node_count > 0:
                node = queue[0]
                queue.pop(0)
                node_count -= 1
                
                if tree[node]:
                    for child in tree[node]:
                        queue.append(child)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()