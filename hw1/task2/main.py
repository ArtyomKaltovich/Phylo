import sys

import matplotlib.pyplot as plt
from Bio import Phylo

from utils import save_data_to_file

INPUT_FILE_NAME = "data/data.txt"
OUT_FILE_NAME = "data/data.phyloxml"


if __name__ == '__main__':
    sys.path.append(".")
    # save data as file, coz Phylo doesn't accept strings
    # tempfile is also doesn't work and always empty
    save_data_to_file(INPUT_FILE_NAME)
    data = Phylo.parse(INPUT_FILE_NAME, "newick")
    fig = plt.figure(figsize=(25, 30))
    axes = fig.add_subplot(1, 1, 1)
    for tree in data:
        tree.ladderize()
        Phylo.draw_ascii(tree)
        Phylo.draw(tree, do_show=False, axes=axes)
        fig.savefig("plot/tree.svg")
        fig.savefig("plot/tree.png")
    Phylo.convert(INPUT_FILE_NAME, "newick", OUT_FILE_NAME, "phyloxml")
