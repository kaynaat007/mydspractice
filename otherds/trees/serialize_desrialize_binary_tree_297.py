from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printTree(root):


    if root is not None:
        printTree(root.left)
        print(root.val)
        printTree(root.right)


class Construct:

    def __init__(self):
        self.k = 0

    def util(self, i, j, preorder, inorder):

        if i > j:
            return

        val, idx = preorder[self.k]
        self.k +=1
        for x in range(i, j+1):
            if inorder[x][0] == val and inorder[x][1] == idx:
                break
        root_index = x
        root = TreeNode(val)
        root.left = self.util(i, root_index-1,  preorder, inorder)
        root.right = self.util(root_index + 1, j, preorder, inorder)
        return root


    def buildTree(self, preorder: List[int], inorder_list: List[int]) -> TreeNode:
        """

        """
        if not preorder:
            return None
        return self.util(0, len(inorder_list)-1, preorder, inorder_list)



def construct_binary_tree_from_inorder_preorder_traversal(inorder_list, preorder_list):

    construct = Construct()
    return construct.buildTree(preorder_list, inorder_list)



class Efficient:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """

        def dfs(root):
            if root:
                vals.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            else:
                vals.append('#')

        vals = []
        dfs(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """
        nodes = iter(data.split())

        def dfs():
            if not nodes:
                return
            val = next(nodes)
            if val == '#':
                return
            root = TreeNode(val)
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()




class Codec:

    def preorder(self, root, k):

        if root is None:
            return ""

        s = str(root.val) + ':' + str(k)

        left = self.preorder(root.left, k+1)
        if left:
            s += '#' + str(left)
        right = self.preorder(root.right, k+2)
        if right:
            s += '#' + str(right)
        return s

    def inorder(self, root, k):

        if root is None:
            return ""

        ins = ""
        left = self.inorder(root.left, k+1)
        if left:
            ins += left

        ins += '#' + str(root.val) + ':' + str(k)

        right = self.inorder(root.right, k+2)
        if right:
            ins += right

        return ins

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ins = self.inorder(root, 0)
        print('inorder: ', ins)
        pre = self.preorder(root, 0)
        print('preorder: ', pre)
        ins = ins[1:]
        summation = ins + '#$' + pre
        return summation


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        inorder_list, preorder_list = extract(data)
        print('inorder list', inorder_list)
        print('preorder list', preorder_list)
        return construct_binary_tree_from_inorder_preorder_traversal(inorder_list, preorder_list)


def get_index(data, i):
    n = len(data)
    ch = ""
    i += 1
    while i < n and data[i].isdigit():
        ch += data[i]
        i +=1
        if i < n and data[i] == '#':
            break
    return ch, i


def extract(data):

    inorder_list = []
    preorder_list = []
    e = ""
    elements = inorder_list
    i = 0
    n = len(data)
    while i < n:

        ch = data[i]

        if ch == '-':
            e += '-'
        elif ch == ':':
            idx, i = get_index(data, i)
            elements.append((int(e), idx))
            if i < n and data[i] == '#':
                e = ""
        elif ch.isdigit():
            e += ch
        elif ch == '$':
            inorder_list = elements.copy()
            elements.clear()
            elements = preorder_list

        i = i+1

    return inorder_list, preorder_list


# code = Codec()
code = Efficient()

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(6)

#
# root = TreeNode(14)
# root.right = TreeNode(18)
# root.right.right = TreeNode(251)

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.left.right = TreeNode(4)


#
# root = TreeNode(15)
# root.left = TreeNode(10)
# root.left.left = TreeNode(3)


# root = TreeNode(10)

# root = TreeNode(1)
# root.left = TreeNode(-2)
# root.right = TreeNode(-2)

# [3,2,4,3]

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(3)


# root = None
s = code.serialize(root)
print(s)
root = code.deserialize(s)
printTree(root)

