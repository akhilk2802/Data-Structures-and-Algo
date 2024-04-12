"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['node']) -> Optional['node']:

        if not node:
            return None
        node_map = {}
        queue = deque([node])
        cloned_node = Node(node.val)
        node_map[node] = cloned_node
        
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in node_map:
                    queue.append(neighbor)
                    cloned_neighbor = Node(neighbor.val)
                    node_map[neighbor] = cloned_neighbor
                node_map[curr_node].neighbors.append(node_map[neighbor])
        
        return cloned_node