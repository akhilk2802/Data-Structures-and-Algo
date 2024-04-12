class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices_with_no_incoming_edges = set(range(n))
    
        for _, to_vertex in edges:
            vertices_with_no_incoming_edges.discard(to_vertex)
        
        return list(vertices_with_no_incoming_edges) 