# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "[]"

        queue = deque([root]) # deque([]) Need "[]"
        results = []
        while queue:
            # NO level order
            node = queue.popleft()
            if node:
                results.append(node.val)
            else:
                results.append(None)
                continue
            
            #if node.left:
            queue.append(node.left)
    
            #if node.right:
            queue.append(node.right)

        while results[-1] == None:
            del results[-1]
        
        return str(results)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # data.strip("\n")
        if data == "[]":
            return None
        
        data = data[1:-1] # remove "[]"
        results = data.split(", ") # string to list, KEY: ", "
        root = TreeNode(int(results[0]))
        queue_nodes = [root] # use a list to record the nodes pass by
        index = 0
        isLeftChild = True

        for val in results[1:]:
            if val != "None":
                node = TreeNode(int(val))
                if isLeftChild:
                    queue_nodes[index].left = node
                else:
                    queue_nodes[index].right = node
                queue_nodes.append(node)
            
            if not isLeftChild: # move to next node, every two times
                index += 1
            isLeftChild = not isLeftChild

        return root


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
"""
You may serialize the following tree:
    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""