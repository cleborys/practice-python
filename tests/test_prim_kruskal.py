import pytest

from core.graph.graph import Graph
from core.graph.mst import PrimMST, KruskalMST


@pytest.fixture
def graph():
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

    return graph


@pytest.fixture
def small_graph():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")

    graph.add_edge_undirected(a, b, 1)
    graph.add_edge_undirected(a, c, 2)
    graph.add_edge_undirected(b, c, 3)

    return graph


def test_prim_small(small_graph):
    mst = PrimMST.run(small_graph)
    assert sum(edge._weight for edge in mst) == 3


def test_prim(graph):
    mst = PrimMST.run(graph)
    assert sum(edge._weight for edge in mst) == 4456


def test_kruskal_small(small_graph):
    mst = KruskalMST.run(small_graph)
    assert sum(edge._weight for edge in mst) == 3


def test_kruskal(graph):
    mst = KruskalMST.run(graph)
    assert sum(edge._weight for edge in mst) == 4456
