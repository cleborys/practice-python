import pytest

from core.tree.bst.avl import AVLTree, AVLTreeMap

from typing import List
import random
from core.timing import Timer
import matplotlib
import matplotlib.pyplot as plt
import math


def test_rotate():
    tree = AVLTree()
    tree.insert(2, 2)
    tree.insert(3, 3)
    tree.insert(1, 1)

    assert [x.value for x in tree.postorder_traversal()] == [1, 3, 2]

    tree._rotate_child_up(tree.get_root(), True)
    assert [x.value for x in tree.postorder_traversal()] == [1, 2, 3]

    root = tree.get_root()
    assert root.value == 3
    assert root._right is None

    left = root._left
    assert left.value == 2
    assert left._right is None

    leftleft = left._left
    assert leftleft.value == 1
    assert leftleft._has_children() is False


def test_avl_tree_map():
    random.seed("test avl tree map")
    to_add = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(100)]

    tree_map = AVLTreeMap()
    compare_dict = {}

    for key, value in to_add:
        tree_map[key] = value
        compare_dict[key] = value

    assert len(tree_map) == len(compare_dict)
    for key, value in compare_dict.items():
        assert tree_map[key] == value

    with pytest.raises(KeyError):
        tree_map[-1]


def rand_list_distinct(length: int) -> List[int]:
    return_list = list(range(length))
    random.shuffle(return_list)
    return return_list


def profile_avl_tree_map(length: int, values: List[int]) -> float:
    random.seed("profile avl tree map")

    tree_map = AVLTreeMap()
    keys = values[:length]
    timer = Timer()
    with timer:
        for i in keys:
            tree_map[i] = i

        for i in keys:
            tree_map[i]

    return timer.elapsed


if __name__ == "__main__":
    fig, ax = plt.subplots()
    max_items = 150_000
    values = rand_list_distinct(max_items)
    item_nbrs = (math.floor(pow(1.5, x)) for x in range(100))
    x_val = []
    y_val = []
    for item_nbr in item_nbrs:
        if item_nbr > max_items:
            break
        runtime = profile_avl_tree_map(item_nbr, values)
        print(f"Handled {item_nbr} items in {runtime} seconds")
        x_val.append(item_nbr)
        y_val.append(runtime / item_nbr)

    ax.set_xscale("log")
    plt.plot(x_val, y_val)
    plt.show()
