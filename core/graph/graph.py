from typing import Any, List, Optional

ValueType = Any
WeightType = int


class GraphError(Exception):
    pass


class InvalidNodeError(GraphError):
    pass


class LoopError(GraphError):
    pass


class Graph:
    """
    In adjacency map representation.
    """

    class Node:
        __slots__ = ["_value"]

        def __init__(self, value: ValueType):
            self._value = value

        def __hash__(self):  # pragma: no cover
            return hash(id(self))

        def __repr__(self) -> str:  # pragma: no cover
            return f"<{self._value}>"

    class Edge:
        __slots__ = ["_source", "_target", "_weight"]

        def __init__(self, source: "Node", target: "Node", weight: WeightType):
            self._source = source
            self._target = target
            self._weight = weight

        def __hash__(self):  # pragma: no cover
            return hash((self._source, self._target))

        def __repr__(self) -> str:  # pragma: no cover
            return f"({self._source}-{self._target})"

    def __init__(self):
        self._out_edges = {}
        self._in_edges = {}

    def add_node(self, value: ValueType) -> Node:
        new_node = self.Node(value)
        self._out_edges[new_node] = {}
        self._in_edges[new_node] = {}
        return new_node

    def add_edge(self, source: Node, target: Node, weight: WeightType = 1):
        self._add_edge_directed(source, target, weight)

    def add_edge_undirected(self, source: Node, target: Node, weight: WeightType = 1):
        self._add_edge_directed(source, target, weight)
        self._add_edge_directed(target, source, weight)

    def _add_edge_directed(self, source: Node, target: Node, weight: WeightType):
        self._verify_node(source)
        self._verify_node(target)
        if source is target:
            raise LoopError

        new_edge = self.Edge(source, target, weight)
        self._out_edges[source][target] = new_edge
        self._in_edges[target][source] = new_edge

    def _verify_node(self, node: Node):
        if node not in self._out_edges:
            raise InvalidNodeError

    def get_edges(self):
        yield from (
            edge
            for out_edges in self._out_edges.values()
            for edge in out_edges.values()
        )

    def get_number_of_nodes(self) -> int:
        return len(self._out_edges)

    def get_nodes(self):
        yield from self._out_edges.keys()

    def get_outgoing_edges(self, node: Node):
        self._verify_node(node)
        yield from self._out_edges[node].values()

    @classmethod
    def from_adjacency_matrix(cls, matrix: List[List[Optional[int]]]):
        dimensions = len(matrix)
        for row in matrix:
            if len(row) != dimensions:
                raise ValueError("Matrix must be square.")

        graph = cls()
        nodes = []
        for index in range(dimensions):
            nodes.append(graph.add_node(str(index)))

        for source, row in zip(nodes, matrix):
            for target, value in zip(nodes, row):
                if value is None:
                    continue

                graph.add_edge(source, target, value)

        return graph
