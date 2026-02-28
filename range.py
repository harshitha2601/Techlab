class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            self.build(nums, 2*node+1, start, mid)
            self.build(nums, 2*node+2, mid+1, end)
            self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def update(self, index, value, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1

        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self.update(index, value, 2*node+1, start, mid)
            else:
                self.update(index, value, 2*node+2, mid+1, end)

            self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def queryMax(self, L, R, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1

        if R < start or L > end:
            return float('-inf')

        if L <= start and end <= R:
            return self.tree[node]

        mid = (start + end) // 2
        left = self.queryMax(L, R, 2*node+1, start, mid)
        right = self.queryMax(L, R, 2*node+2, mid+1, end)

        return max(left, right)