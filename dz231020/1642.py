class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        for i in range(n-1):
            h = heights[i+1]-heights[i]
            if h>0:
                heappush(heap,h)
                if len(heap)>ladders:
                    m_bricks = heappop(heap)
                    bricks-=m_bricks
                if bricks<0:
                    return i
        return n-1
