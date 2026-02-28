from collections import deque

def streaming_max(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove out-of-window elements
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result