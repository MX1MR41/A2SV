from heapq import heapify, heappop, heappush


for _ in range(int(input())):
    n = int(input())
    parent = list(map(int,input().split()))
    
    graph = [[] for i in range(n)]
    for i in range(n -1):
        graph[parent[i] - 1].append(i + 1)
    
    graph.sort(key = lambda x : len(x),reverse=True)
    

    arr = []

    for i in graph:
        if len(i) != 0:
            arr.append(len(i))
    
    arr.append(1)
    
    for i in range(len(arr)):
        arr[i] += i
        
    if max(arr) == arr[-1]:
        print(arr[-1])
        
    else:
        
        cur_ans = arr[-1]
        for i in range(len(arr)):
            arr[i] = -arr[i]
            
        heapify(arr)
        
        while cur_ans < -arr[0]:
            cur = heappop(arr)
            heappush(arr,cur + 1)
            cur_ans += 1
            
        print(cur_ans) 