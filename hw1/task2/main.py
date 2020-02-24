import requests
import matplotlib.pyplot as plt
from Bio import Phylo

DATA_URL = r"https://www.jasondavies.com/tree-of-life/life.txt"
INPUT_FILE_NAME = "data/data.txt"
OUT_FILE_NAME = "data/data.phyloxml"


def save_data_to_file(data_url, file_name):
    data = requests.get(data_url)
    data = data.text
    with open(file_name, "w") as file:
        file.write(data)


if __name__ == '__main__':
    # save data as file, coz Phylo doesn't accept strings
    # tempfile is also doesn't work and always empty
    save_data_to_file(DATA_URL, INPUT_FILE_NAME)
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
