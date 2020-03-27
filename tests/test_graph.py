import pytest

from core.graph.graph import Graph, InvalidNodeError, LoopError


def test_from_adj_matrix():
    graph = Graph.from_adjacency_matrix([[None, 2, 3], [4, None, 6], [7, None, None]])

    assert graph.get_number_of_nodes() == 3
    assert len(list(graph.get_edges())) == 5


def test_from_matrix_not_square():
    with pytest.raises(ValueError):
        graph = Graph.from_adjacency_matrix([[None, 2, 3], [4, None, 6]])


def test_no_loops_allowed():
    graph = Graph()
    node = graph.add_node("node")
    with pytest.raises(LoopError):
        graph.add_edge(node, node)


def test_invalid_node():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)

    other_graph = Graph()
    with pytest.raises(InvalidNodeError):
        other_graph.add_edge(node1, node2)
