import pytest

from core.graph.graph import Graph
from core.graph.shortest_path import Dijkstra


@pytest.fixture
def large_graph():
    graph = Graph()
    bos = graph.add_node("bos")
    pvd = graph.add_node("pvd")
    jfk = graph.add_node("jfk")
    bwi = graph.add_node("bwi")
    ordd = graph.add_node("ordd")
    mia = graph.add_node("mia")
    dfw = graph.add_node("dfw")
    sfo = graph.add_node("sfo")
    lax = graph.add_node("lax")

    graph.add_edge_undirected(bos, sfo, 2704)
    graph.add_edge_undirected(bos, ordd, 867)
    graph.add_edge_undirected(bos, jfk, 187)
    graph.add_edge_undirected(bos, mia, 1258)
    graph.add_edge_undirected(pvd, jfk, 144)
    graph.add_edge_undirected(pvd, ordd, 849)
    graph.add_edge_undirected(jfk, ordd, 740)
    graph.add_edge_undirected(jfk, dfw, 1391)
    graph.add_edge_undirected(jfk, bwi, 184)
    graph.add_edge_undirected(jfk, mia, 1090)
    graph.add_edge_undirected(bwi, ordd, 621)
    graph.add_edge_undirected(bwi, mia, 946)
    graph.add_edge_undirected(ordd, dfw, 802)
    graph.add_edge_undirected(ordd, sfo, 1846)
    graph.add_edge_undirected(mia, dfw, 1121)
    graph.add_edge_undirected(mia, lax, 2342)
    graph.add_edge_undirected(dfw, sfo, 1464)
    graph.add_edge_undirected(dfw, lax, 1235)
    graph.add_edge_undirected(sfo, lax, 337)

    return graph, bos, lax


@pytest.fixture
def small_graph():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")

    graph.add_edge_undirected(a, b, 1)
    graph.add_edge_undirected(a, c, 2)
    graph.add_edge_undirected(b, c, 3)

    return (graph, a, b, c)


def test_dijkstra_small(small_graph):
    graph, a, b, c = small_graph
    path_tree = Dijkstra.compute_path_tree(graph, a)

    assert Dijkstra.distance_to(a, path_tree) == 0
    assert Dijkstra.distance_to(b, path_tree) == 1
    assert Dijkstra.distance_to(c, path_tree) == 2


def test_dijkstra(large_graph):
    graph, bos, lax = large_graph
    path_tree = Dijkstra.compute_path_tree(graph, bos)

    path_to_lax = Dijkstra.path_to(lax, path_tree)

    assert Dijkstra.distance_to(lax, path_tree) == 2813
    assert path_to_lax[0]._source._value == "bos"
    assert path_to_lax[0]._target._value == "jfk"
    assert path_to_lax[1]._target._value == "dfw"
    assert path_to_lax[2]._target._value == "lax"


def test_dijkstra_missing(small_graph):
    graph, a, b, c = small_graph
    path_tree = Dijkstra.compute_path_tree(graph, a)
    with pytest.raises(KeyError):
        Dijkstra.path_to("bogus", path_tree)
