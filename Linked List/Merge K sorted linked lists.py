import heapq

class Solution:
    def mergeKLists(self, arr):
        heap = []
        for i in range(len(arr)):
            if arr[i]:
                heapq.heappush(heap, (arr[i].data, i, arr[i]))

        dummy = Node(0)
        tail = dummy

        while heap:
            val, idx, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.data, idx, node.next))

        return dummy.next
