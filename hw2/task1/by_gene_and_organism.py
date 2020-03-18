from Bio import Entrez

GENE = "ABO"
ORGANISM = "horse"
OUTPUT = "result/by_gene_and_organism.xml"
Entrez.email = "Your.Name.Here@example.org"


def by_gene_and_organism(gene, organism, *, output_file, retmax=10):
    with Entrez.esearch(db="nucleotide", retmax=retmax, term=f"({gene}[Gene Name]) AND {organism}[Organism])",
                        idtype="acc") as handle, \
            open(output_file, "w") as output:
        output.write(handle.read())


if __name__ == '__main__':
    by_gene_and_organism(GENE, ORGANISM, output_file=OUTPUT)
