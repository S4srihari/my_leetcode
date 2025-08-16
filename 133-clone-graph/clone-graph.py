"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        my_hash = {}

        def dfs(node):
            if node in my_hash : return my_hash[node]
            copy = Node(node.val)
            my_hash[node] = copy
            for adj_node in node.neighbors:
                copy.neighbors.append(dfs(adj_node))
            return copy

        return dfs(node) if node else None