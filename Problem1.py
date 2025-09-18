# Problem 1
# Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)

# Method1: Using BFS
# Time Complexity : O(N) -- going through all the nodes
# Space Complexity : O(N) -- O(N/2) -- max size of the queue would be at the leaf nodes when it is a complete BST
# Did this code successfully run on GFG : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Used BFS or level order traversal to print nodes values level by level. We used queue because we wanted to explore all the children
# of a node at a level and queue helps us to achieve that because of its FIFO property.

from collections import deque
# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if(not root):
            return []
        que = deque([root])
        levelTrav = []
        while(que):
            size = len(que)
            currLevel = []
            for i in range(size):
                # we need FIFO
                currEle = que.popleft()
                currLevel.append(currEle.val)
                # add children of currNode
                if(currEle.left):
                    que.append(currEle.left)

                if(currEle.right):
                    que.append(currEle.right)

            levelTrav.append(currLevel)
        
        return levelTrav
    
root = Node(10)

node6 = Node(6)
root.left = node6
node15 = Node(15)
root.right = node15
node4 = Node(4)
node6.left = node4
node8 = Node(8)
node6.right = node8
node13 = Node(13)
node15.left = node13
node18 = Node(18)
node15.right = node18
node2 = Node(2)
node4.left = node2
node5 = Node(5)
node4.right = node5
node9 = Node(9)
node8.right = node9
node12 = Node(12)
node13.left = node12
node20 = Node(20)
node18.right = node20

print("Method1: Using BFS")
sol = Solution()
print(sol.levelOrder(root))
print(sol.levelOrder(None))

# Method2: Using DFS
# Time Complexity : O(N) -- going through all the nodes
# Space Complexity : O(N) -- hashmap + O(h) -- recursion stack
# Did this code successfully run on GFG : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Here we pass level as parameter of recursion. For the given level as key of the hashmap we keep list of node values

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.levelMap = {}
        self.maxLevel = 0

    def helper(self, root, currLevel):
        # base case
        if(not root):
            return

        if(currLevel > self.maxLevel):
            self.maxLevel = currLevel

        if(currLevel in self.levelMap):
            self.levelMap[currLevel].append(root.val)
        else:
            self.levelMap[currLevel] = [root.val]

        self.helper(root.left, currLevel + 1)
        self.helper(root.right, currLevel + 1)


    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if(not root):
            return []
        self.helper(root, 0)
        levelTrav = []
        for level in range(self.maxLevel + 1):
            levelTrav.append(self.levelMap[level])

        return levelTrav
        
print("Method2: Using DFS")
sol = Solution()
print(sol.levelOrder(root))
print(sol.levelOrder(None))


# Method3: Using DFS with result list
# Time Complexity : O(N) -- going through all the nodes
# Space Complexity : O(h) -- recursion stack
# Did this code successfully run on GFG : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# The algo is same as above. Just instead of hash map for keys we use the final result indices as keys.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = []

    def helper(self, root, currLevel):
        # base case
        if(not root):
            return

        if(currLevel == len(self.result)):
            # it means for the currLevel we do not have a list in our result
            # so create it
            self.result.append([root.val])
        else:
            # list for this level already exists in the result
            # just append the element to the list for this level
            self.result[currLevel].append(root.val)

        self.helper(root.left, currLevel + 1)
        self.helper(root.right, currLevel + 1)


    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if(not root):
            return []
        self.helper(root, 0)

        return self.result

print("Method3: Using DFS with result list")
sol = Solution()
print(sol.levelOrder(root))
print(sol.levelOrder(None))