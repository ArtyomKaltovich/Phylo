library(ape)
library(phangorn)
library(seqinr)

draw_tree <- function(path, fitJC) {
  png(path, width=1000, height=800)
  plotBS(midpoint(fitJC$tree), bs, p=0, type="p")
  add.scale.bar()
  dev.off()
}

read_data <- function() {
  data <- read.dna("hw3/data/SUP35_aln.best.fas", format="fasta")
  data <- phyDat(data, type="DNA", levels=NULL)
  return(data)
}

bootsrap <-function(tree, data) {
  fit <- pml(tree, data)
  fitJC <- optim.pml(fit, model="JC", rearrangement="stochastic")
  logLik(fitJC)
  bs <- bootstrap.pml(fitJC, bs=100, optNni=TRUE, multicore=TRUE, control=pml.control(trace=0))
  return(fitJC)
}

data <- read_data()
#mt <- modelTest(data)
dna_dist <- dist.ml(data, model="JC")
upgma_tree <- upgma(dna_dist)
nj_tree  <- NJ(dna_dist)

draw_tree("hw3/plot/upgma.png", bootsrap(upgma_tree, data))
draw_tree("hw3/plot/nj.png", bootsrap(nj_tree, data))
