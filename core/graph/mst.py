from .graph import Graph
from core.heap.arrayheap import ArrayHeap
from core.union_find import UnionFind

from typing import List

Edge = Graph.Edge


class WeightedEdge:
    __slots__ = ["_edge"]

    def __init__(self, edge: Edge):
        self._edge = edge

    def __lt__(self, other: "WeightedEdge") -> bool:
        return self._edge._weight < other._edge._weight

    @property
    def source(self):
        return self._edge._source

    @property
    def target(self):
        return self._edge._target


class PrimMST:
    @staticmethod
    def run(graph: Graph) -> List[Edge]:
        start_node = next(iter(graph.get_nodes()))

        mst = []
        boundary = {}
        done = {start_node}
        heap = ArrayHeap()

        for edge in graph.get_outgoing_edges(start_node):
            new_item = heap.push(WeightedEdge(edge))
            boundary[edge._target] = new_item

        while len(boundary) != 0:
            new_w_edge = heap.pop()
            new_edge = new_w_edge._edge
            mst.append(new_edge)

            new_node = new_edge._target
            del boundary[new_node]
            done.add(new_node)

            for edge in graph.get_outgoing_edges(new_node):
                if edge._target in done:
                    continue

                # if not in boundary
                # then add to heap
                if edge._target not in boundary:
                    new_item = heap.push(WeightedEdge(edge))
                    boundary[edge._target] = new_item
                    continue

                # if already in boundary
                # and edge is better
                # then update heap
                new_container = WeightedEdge(edge)
                if new_container < boundary[edge._target].value:
                    heap.update(boundary[edge._target], new_container)

        return mst


class KruskalMST:
    @staticmethod
    def run(graph: Graph) -> List[Edge]:
        """
        Returns a minimum spanning forest on each component.
        """
        edges = sorted(WeightedEdge(edge) for edge in graph.get_edges())
        partitions = UnionFind()
        mst = []

        for edge in edges:
            added = partitions.union(edge.source, edge.target)
            if added:
                mst.append(edge._edge)

            if len(mst) == graph.get_number_of_nodes() - 1:
                break

        return mst
