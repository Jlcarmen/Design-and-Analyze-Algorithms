import heapq

heap = []

heapq.heappush(heap, 20)
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)

print(heapq.heappop(heap))
print(heapq.heappop(heap))

print("Heap after popping:", heap)