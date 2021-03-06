import os
import random
import sys

from ete3 import Tree, TreeStyle, TextFace
from utils import save_data_to_file

INPUT_DATA_FILE = r"data/data.txt"

NUMBER = 30


def read_prunned_data():
    if not os.path.exists(INPUT_DATA_FILE):
        save_data_to_file(INPUT_DATA_FILE)
    t = Tree(INPUT_DATA_FILE, format=1)
    descendants = random.choices(t.get_descendants(), k=NUMBER)
    # filter empty and int nodes
    descendants = [d.name for d in descendants if d.name and not d.name.isdecimal()]
    t.prune(descendants)
    return t


def remove_blue_dots(node):
    node.img_style["size"] = 0


def create_tree_style():
    ts = TreeStyle()
    ts.title.add_face(TextFace("Randomly pruned data", fsize=20), column=0)
    ts.layout_fn = remove_blue_dots
    ts.mode = "c"
    ts.show_leaf_name = True
    ts.show_branch_length = True
    ts.show_branch_support = True
    return ts


if __name__ == '__main__':
    sys.path.append(".")
    t = read_prunned_data()
    t.render("plot/tree.pdf", tree_style=create_tree_style())
    t.show(tree_style=create_tree_style())
