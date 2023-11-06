class SeatManager:

    def __init__(self, n: int):
        self.next = 1
        self.priority = []

    def reserve(self) -> int:
        if self.priority:
            return heapq.heappop(self.priority)
        seat = self.next
        self.next += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.priority, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)