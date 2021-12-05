'''
To be used for faster queries like:
   find sum of elements between array indices [l, r]
   find minimum of elements between array indices [l, r]
   find maximum of elements between  array indices [l, r]
   find frequency of element x in between given range[l, r]
'''

class SegmentTree:

    def __init__(self, arr):
        n = len(arr)
        self.arr = arr
        self.segment_tree = [{}] * (2 * n + 5)

    def build(self, current_index, start, end):
        '''
        construct in post order fashion.
        process children nodes before processing current node
        size of segment tree: 2 * n +  2
        Each call caries a range (l, r) which tells that the node called current_index
         in segment tree will store values from
        arr[l] + arr[l+1] + .... + arr[r-1] + arr[r]
        '''
        if start == end:
            # print(current_index, len(self.segment_tree))
            self.segment_tree[current_index] = {
                self.arr[start]: 1
            }
            return
        if start > end or start < 0:
            return
        mid = start + (end - start)//2
        self.build(current_index * 2 + 1, start, mid)
        self.build(current_index * 2 + 2, mid+1, end)
        self.segment_tree[current_index] = merge(self.segment_tree[2 * current_index + 1], self.segment_tree[2 * current_index + 2])

    def query(self, node_range_left, node_range_right, query_left, query_right, target,  current_node_index):
        '''
        current nodes range is defined by [q, r]. q and r are indices which represent that nodes range
        root nodes range is from 0 to len(arr) - 1.
        query range is defined by [l, r]
        current node index is current nodes index in the segment Tree
        if node's range is within query range, return node's value
        if node's range is completely outside the query range, return 0
        if overlap happens, process left and right child of current node and then return the sum
        '''
        if query_left <= node_range_left <= node_range_right <= query_right:
            return self.segment_tree[current_node_index].get(target, 0)
        elif query_left > node_range_right or query_right < node_range_left:
            # [ .segment..] [.query...] or [ query....] [..segment]
            return 0
        else:
            mid = node_range_left + (node_range_right - node_range_left) // 2
            left = self.query(node_range_left, mid, query_left, query_right, target,  current_node_index * 2 + 1)
            right = self.query(mid + 1, node_range_right, query_left, query_right, target, current_node_index * 2 + 2)
            return left + right

    def update(self, idx, new_value):
        pass

    def print(self):
        print("segment tree: ", self.segment_tree)


def merge(dict1, dict2):
    dict3 = dict2.copy()
    for key, val in dict1.items():
        if key not in dict3:
            dict3[key] = val
        else:
            dict3[key] += val
    return dict3


arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]
q_l = 0
q_r = 11
target = 33


# arr = [5, 8, 9, 5, 8, 10, 1, 1, 3]
# q_l = 6
# q_r = 8
# target = 1

arr = [10, 1, 1, 3, 5, 7, 8, 9, 1, 2, 4, 6, 3, 1, 7, 7, 7]
q_l = 12
q_r = 16
target = 7


client = SegmentTree(arr)
client.build(0,  0, len(arr)-1)
print(client.query(0, len(arr)-1, q_l, q_r, target, 0))
# client.print()



