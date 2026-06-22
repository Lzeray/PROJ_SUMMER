from typing import List

class GraphAnalyzer:
    def __init__(self, app):
        self.app = app
        self.graph = app.get_graph()
        
        self.nodes = self._get_nodes()
        self.edges, self.entry_points = self._get_edges()

    def _get_nodes(self):
        nodes = set()
        for node in self.graph.nodes:
            if not node.startswith('__'):
                nodes.add(node)
        return nodes
    
    def _get_edges(self):
        entry_points = []
        edges = {}
        for node in self.nodes:
            edges[node] = []
        
        for edge in self.graph.edges:
            if edge.source in edges and not edge.target.startswith('__'):
                edges[edge.source].append(edge.target)

            if edge.source == '__start__' and edge.target in edges:
                entry_points.append(edge.target)
                
        return edges, entry_points
    
    def get_paths(self, max_depth: int = 10) -> List[List[str]]:
        all_paths = []

        def dfs(current: str, path: List[str], depth: int):
            new_path = path + [current]
            if depth >= max_depth:
                all_paths.append(new_path)
                return
            
            children = self.edges.get(current, [])
            
            if not children:
                all_paths.append(new_path)
                return
            
            for child in children:
                dfs(child, new_path, depth + 1)

        for start in self.entry_points:
            dfs(start, [], 0)

        return all_paths