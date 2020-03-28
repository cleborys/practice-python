from .graph import Graph
from core.heap.arrayheap import ArrayHeap

from typing import Dict, Optional, List

Node = Graph.Node
Edge = Graph.Edge


class BoundaryEdge:
    __slots__ = ["_edge", "_distance"]

    def __init__(self, edge: Edge, distance_to_source: float):
        self._edge = edge
        self._distance = distance_to_source + edge._weight

    def __lt__(self, other: "BoundaryEdge") -> bool:
        return self._distance < other._distance

    @property
    def node(self):
        return self._edge._target

    @property
    def edge(self):
        return self._edge


class Dijkstra:
    @staticmethod
    def compute_path_tree(graph: Graph, start: Node) -> Dict[Node, Optional[Node]]:
        heap = ArrayHeap()
        paths: Dict[Node, Optional[Node]] = {start: None}
        distances = {start: 0}

        boundary = {}

        for edge in graph.get_outgoing_edges(start):
            new_boundary_edge = BoundaryEdge(edge, 0)
            new_item = heap.push(new_boundary_edge)
            boundary[new_boundary_edge.node] = new_item

        while boundary:
            add_to_path = heap.pop()
            del boundary[add_to_path.node]
            paths[add_to_path.node] = add_to_path.edge
            distances[add_to_path.node] = (
                distances[add_to_path.edge._source] + add_to_path.edge._weight
            )

            for edge in graph.get_outgoing_edges(add_to_path.node):
                target = edge._target
                # if done, skip
                if target in paths:
                    continue

                boundary_edge = BoundaryEdge(edge, distances[add_to_path.node])
                # if not in boundary, add to heap
                if target not in boundary:
                    new_item = heap.push(boundary_edge)
                    boundary[target] = new_item
                    continue

                # if improvement, update
                if boundary_edge < boundary[target].value:
                    heap.update(boundary[target], boundary_edge)

        return paths

    @staticmethod
    def path_to(node: Node, paths: Dict[Node, Optional[Edge]]) -> List[Edge]:
        if node not in paths:
            raise KeyError

        reverse_path: List[Edge] = []
        current_node = node
        while paths[current_node] is not None:
            reverse_path.append(paths[current_node])
            current_node = reverse_path[-1]._source

        reverse_path.reverse()
        return reverse_path

    @classmethod
    def distance_to(cls, node: Node, paths: Dict[Node, Optional[Edge]]) -> int:
        path = cls.path_to(node, paths)
        return sum(edge._weight for edge in path)
