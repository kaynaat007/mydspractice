class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ""
        s = str(root.val)
        left = self.serialize(root.left)
        if left:
            s += '#' + str(left)
        right = self.serialize(root.right)
        if right:
            s += '#' + str(right)
        return s

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = extract(data)
        # print('vector found: ', arr)
        return util(arr, 0, len(arr)-1, len(arr))


def util(s, i, j, n):

    if i > j:
        return

    v = s[i]
    root = TreeNode(v)
    val = root.val

    k = i + 1
    while k <= j < n:
        v = s[k]
        if v >= val:
            break
        k += 1

    root.left = util(s, i+1, k-1, n) #
    root.right = util(s, k , j, n)

    return root

def printTree(root):


    if root is not None:
        printTree(root.left)
        print(root.val)
        printTree(root.right)


def extract(data):

    elements = []
    e = ""
    for ch in data:
        if ch.isdigit():
            e += ch
        if ch == '#':
            elements.append(int(e))
            e = ""
    if e:
        elements.append(int(e))
    return elements


code = Codec()

s = '516'
s = '876'
# s = '20#10#40'
# s = '5#1#6'
# s = '14#18#251'

# root = TreeNode(14)
# root.right = TreeNode(18)
# root.right.right = TreeNode(251)

# root = TreeNode(14)

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.left.left = TreeNode(1)


# root = TreeNode(5)
# root.left = TreeNode(3)
# root.left.right = TreeNode(4)

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(6)

# root = TreeNode(10)
# root.left = TreeNode(10)
# root.left.left = TreeNode(10)

s = code.serialize(root)
# print(s)

# s = '10#10#10'
# s = '3#1#6'
root = code.deserialize(s)

print('------ Tree start ------')
printTree(root)
print('------ Tree end------')