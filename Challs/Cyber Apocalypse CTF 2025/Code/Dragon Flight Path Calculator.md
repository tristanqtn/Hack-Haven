```python
import sys

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = (arr[start], arr[start], arr[start], arr[start])
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = self.merge(self.tree[left_child], self.tree[right_child])
    
    def merge(self, left, right):
        total_sum = left[0] + right[0]
        max_prefix = max(left[1], left[0] + right[1])
        max_suffix = max(right[2], right[0] + left[2])
        max_subarray = max(left[3], right[3], left[2] + right[1])
        return (total_sum, max_prefix, max_suffix, max_subarray)
    
    def update(self, idx, value, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = (value, value, value, value)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if idx <= mid:
                self.update(idx, value, left_child, start, mid)
            else:
                self.update(idx, value, right_child, mid + 1, end)
            self.tree[node] = self.merge(self.tree[left_child], self.tree[right_child])
    
    def query(self, l, r, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if r < start or l > end:
            return (0, float('-inf'), float('-inf'), float('-inf'))
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = self.query(l, r, 2 * node + 1, start, mid)
        right_child = self.query(l, r, 2 * node + 2, mid + 1, end)
        return self.merge(left_child, right_child)

# Read input
n, q = map(int, input().split())
arr = list(map(int, input().split()))
segment_tree = SegmentTree(arr)

# Process queries
for _ in range(q):
    command = input().split()
    if command[0] == 'U':
        i, x = int(command[1]) - 1, int(command[2])
        segment_tree.update(i, x)
    elif command[0] == 'Q':
        l, r = int(command[1]) - 1, int(command[2]) - 1
        print(segment_tree.query(l, r)[3])

```

`HTB{DR4G0N_FL1GHT_5TR33_5560529c4b321dcb5415c022dc5dc8a2}`