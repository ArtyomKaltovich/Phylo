#if (!requireNamespace("BiocManager", quietly = TRUE))
#    install.packages("BiocManager")
#
#BiocManager::install("ggtree")
library(ggtree)
library(xml2)

DATA_URL = "https://www.jasondavies.com/tree-of-life/life.txt"

data <- download_html(DATA_URL)
tree1 <- read.tree(data)
png("plot/tree1_ggtree.png", width = 2000, height = 2000)
plot(tree1)
dev.off()
