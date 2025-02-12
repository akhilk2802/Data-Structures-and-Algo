# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_list = defaultdict(list)
        
        def buildGraph(node, parent=None):
            if not node:
                return
            if parent:
                adj_list[node.val].append(parent.val)
                adj_list[parent.val].append(node.val)
            buildGraph(node.left, node)
            buildGraph(node.right, node)

        buildGraph(root)
        
        queue = deque([(target.val, 0)])
        visited = set()
        visited.add(target.val)
        
        while queue:
            if queue[0][1] == k:
                return [node for node, dist in queue]

            for _ in range(len(queue)):
                node, dist = queue.popleft()
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return []
        