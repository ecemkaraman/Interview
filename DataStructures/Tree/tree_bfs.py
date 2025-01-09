from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

def bfs_level_order(root):
    result = []
    if not root:
        return result
    queue = deque([root])

    while queue: 
        level_size= len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    return result

if __name__ == "__main__":
    # Constructing a simple binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(bfs_level_order(root)) # Output: [[1], [2, 3], [4, 5]]

def bfs_level_order_bottom(root):
    result = []
    if not root:
        return result
    queue = deque([root])
    while queue:
        current_level=[]
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.insert(0, current_level)
    return result 

#Zigzag traversal

#Diffrent views of tree:
#Left view:
#Recursive

#Iterative

#Right view:
# #Recursive

#Iterative