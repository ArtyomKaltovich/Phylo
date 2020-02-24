library(xml2)
# might need root preveligies
#for (package in c("ape", "ggtree"))
#    if (!package %in% installed.packages()) install.packages(package)
library(ape)
library(ggtree)

DATA_URL = "https://www.jasondavies.com/tree-of-life/life.txt"

data <- download_html(DATA_URL)
tree1 <- read.tree(data)
png("plot/tree.png", width = 2000, height = 3000)
plot(tree1, type = "radial")
dev.off()
svg("plot/tree.svg", width = 3000, height = 3000)
plot(tree1, type = "unrooted", lab4ut="axial", use.edge.length=FALSE,
    font=1, align.tip.label=TRUE)
dev.off()

tree2 <- read.tree(text="(((A, B), (C, D)), E);")
print(tree2)
png("plot/tree2.png", width = 900, height = 900)
plot.phylo(tree2, type = "radial", use.edge.length=FALSE, no.margin=TRUE)
dev.off()
svg("plot/tree2.svg", width = 900, height = 900)
plot.phylo(tree2, type = "unrooted", lab4ut="axial", use.edge.length=FALSE, no.margin=TRUE)
dev.off()
