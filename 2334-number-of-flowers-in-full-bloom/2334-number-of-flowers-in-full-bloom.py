class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p, i) for i, p in enumerate(people)]
        res = [0] * len(people)
        count = 0

        flowers.sort()
        # using one min heap
        end = []

        # m people, n flowers
        # mlogm (sorting people) + nlogn (pop every flower)

        j = 0
        for p, i in sorted(people):
            # flower came into bloom
            while j < len(flowers) and flowers[j][0] <= p:
                heapq.heappush(end, flowers[j][1])
                j += 1

            while end and end[0] < p:
                heapq.heappop(end)

            res[i] = len(end)

        return res

        
        # people = [(p, i) for i, p in enumerate(people)]
        # res = [0] * len(people)
        # count = 0
        # start = [f[0] for f in flowers]
        # end = [f[1] for f in flowers]
        # # make 2 min heaps - O(n) operation
        # heapq.heapify(start)
        # heapq.heapify(end)

        # # m people, n flowers
        # # mlogm (sorting people) + nlogn (pop every flower)

        # for p, i in sorted(people):
        #     # flower came into bloom
        #     while start and start[0] <= p:
        #         heapq.heappop(start)
        #         count += 1

        #     # flower withered
        #     while end and end[0] < p:
        #         heapq.heappop(end)
        #         count -= 1
        #     res[i] = count

        # return res