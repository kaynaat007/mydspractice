"""
Rotations:

T1, T2 and T3 are subtrees of the tree
rooted with y (on the left side) or x (on
the right side)

     y                               x
    / \     Right Rotation          /  \
   x   T3   - - - - - - - >        T1   y
  / \       < - - - - - - -            / \
 T1  T2     Left Rotation            T2  T3
Keys in both of the above trees follow the
following order
 keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
So BST property is not violated anywhere.


AVL tree insert & delete

1. Perform normal BST insertion
2. Let the newly inserted node be w.
3. Starting from w travel up and find the first unbalanced node.
4. Let z be the first unbalanced node.
5. y be the child of z that comes on path from w to z.
6. x be the grandchild of z that comes to path from w to z.
7. Perform rotation on subtree rooted at z.
    7.1   y is left child of z and x is left child of y.  ( Left Left )
    7.2   y is left child of z and x is right child of y ( Left right )
    7.3   y is right child of z and x is right child of y ( Right Right )
    7.4   y is right child of z and x is left child of y.  ( Right Left )


Left Left case

T1, T2, T3 and T4 are subtrees.
         z                                      y
        / \                                   /   \
       y   T4      Right Rotate (z)          x      z
      / \          - - - - - - - - ->      /  \    /  \
     x   T3                               T1  T2  T3  T4
    / \
  T1   T2


Left Right case


    z                               z                           x
    / \                            /   \                        /  \
   y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
  / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
T1   x                          y    T3                    T1  T2 T3  T4
    / \                        / \
  T2   T3                    T1   T2


Right Right case

 z                                y
 /  \                            /   \
T1   y     Left Rotate(z)       z      x
    /  \   - - - - - - - ->    / \    / \
   T2   x                     T1  T2 T3  T4
       / \
     T3  T4


Right left case

   z                            z                            x
  / \                          / \                          /  \
T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
    / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
   x   T4                      T2   y                  T1  T2  T3  T4
  / \                              /  \
T2   T3                           T3   T4


1. perform normal BST insert
2. while making bottom up, update the height of the current node.
3. Get the balance factor of this node.  ( left subtree - right subtree ) height
4. if balance factor > 1 , then current node is unbalanced and node must have been inserted in left subtree of
current node. it is either LEFT LEFT case or LEFT RIGHT case.
5. to check which one, compare newly inserted node with current node's left subtree root value.
6. if balance factor  < -1, then current node is unbalanced and node must have been inserted in right subtree of
current node. it is either RIGHT RIGHT case or RIGHT LEFT case. To find out check the newly inserted value with
current node's right node value.

"""


class Node:
    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right
        self.height = 0
        self.parent = None

    def __str__(self):
        return 'val={}, height={}'.format(self.val, self.height)


class AVL:

    def __init__(self):

        self.root = None
        self.output = []

    def _get_height(self, x):
        if not x:
            return -1
        return x.height


    def _left_rotate(self, x):
        """
        left rotates on subtree rooted at node x

             y                               x
            / \     Right Rotation          / \
           x   T3   - - - - - - - >        T1  y
          / \       < - - - - - - -            / \
         T1  T2     Left Rotation            T2  T3

        """
        print('doing left rotation of node: {}'.format(x))

        if x is None:
            return
        if x.left is None and x.right is None:
            return

        y = x.right  # define y in left rotate
        x.right = y.left  # y's left subtree becomes x's right subtree.

        if y.left:  # y's left subtree parent now becomes x.
            y.left.parent = x

        # original parent of x becomes new parent of y
        y.parent = x.parent

        # if x.parent is None, we have a new root
        if x.parent is None:
            self.root = y
            self.root.parent = None
        elif x.parent.left and x.val == x.parent.left.val: #
            # if x is left child of it's parent, then y will becomes left child
            x.parent.left = y
        else:
            x.parent.right = y # else y becomes right child of x's parent.

        y.left = x  # set x as y's left
        x.parent = y  # set x's parent as y.

        # fix heights
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

    def balance_factor(self, x):

        if x is None:
            return 0
        return self._get_height(x.left) - self._get_height(x.right)

    def self_balance(self, w):
        """
        w is the node inserted newly.
        we wish to balance this tree due to insertion by following parent pointers till root
        """

        current = w.parent
        while current is not None:

            current.height = 1 + max(self._get_height(current.left), self._get_height(current.right))

            f = self.balance_factor(current)

            if f > 1:
                z = current
                # this means node w was inserted somewhere to left of this parent
                y = current.left

                if w.val > y.val:
                    # LEFT RIGHT case
                    print('Left Right case..')
                    self._left_rotate(y)
                    self._right_rotate(z)
                    break
                else:
                    # LEFT LEFT case
                    print('Left Left case..')
                    self._right_rotate(z)
                    break

            elif f < -1:

                z = current
                y = z.right
                if w.val > y.val:
                    # RIGHT RIGHT case
                    print('Right Right case..')
                    self._left_rotate(z)
                    break
                else:
                    # RIGHT LEFT case
                    print('Right Left case..')
                    self._right_rotate(y)
                    self._left_rotate(z)
                    break

            else:
                current = current.parent

    def _right_rotate(self, y):
        """
        right rotates a subtree rooted at node y

             y                               x
            / \     Right Rotation          /  \
           x   T3   - - - - - - - >        T1   y
          / \       < - - - - - - -            / \
         T1  T2     Left Rotation            T2  T3

        """
        print('doing right rotation of node: {}'.format(y))

        if y is None:
            return
        if y.left is None and y.right is None:
            return

        x = y.left  # define x in right rotate
        y.left = x.right  # x's right subtree becomes y's left subtree.

        if x.right:  # x's right subtree parent now becomes y.
            x.right.parent = y

        # original parent of y becomes new parent of x
        x.parent = y.parent

        # if y.parent is None, we have a new root
        if y.parent is None:
            self.root = x
            self.root.parent = None
        elif y.parent.left and y.val == y.parent.left.val:  #
            # if x is left child of it's parent, then y will becomes left child
            y.parent.left = x
        else:
            y.parent.right = x  # else y becomes right child of x's parent.

        x.right = y  # set y as x's right
        y.parent = x  # set y's parent as x.

        # fix heights
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

    def insert(self, val):
        """
        standard BST insertion
        """
        current = self.root
        parent = None

        while current is not None:

            parent = current
            if val < current.val:
                current = current.left
            else:
                current = current.right

        current = Node(val,)
        current.parent = parent

        if parent:
            if current.val < parent.val:
                parent.left = current
            else:
                parent.right = current
        else:
            self.root = current

        # balance the tree
        self.self_balance(current)
        print('inserted: {}'.format(current))

    def inorder(self):

        print('doing inorder...')
        if self.root:
            current = self.root
            self.inorder_util(current)

    def inorder_util(self, current):

        if current:
            self.inorder_util(current.left)
            self.output.append(current)
            self.inorder_util(current.right)

    def check(self, input):

        input = list(input)
        return list(sorted(input)) == [key.val for key in self.output]



import random

x = set()
t = AVL()

for i in range(100000):
    x.add(random.randint(1, 10 * 10 * 10 * 10 * 10))

print('unique numbers: {}'.format(len(x)))
for e in x:
    t.insert(e)

t.inorder()

print(t.check(x))



















