from Bio import Entrez

GENE = "ABO"
ORGANISM = "horse"
OUTPUT = "result/seq.fasta"
Entrez.email = "Your.Name.Here@example.org"


def download_seq(gene, organism, *, output_file, rettype="fasta", retmax=10):
    with Entrez.esearch(db="nucleotide", retmax=retmax, term=f"({gene}[Gene Name]) AND {organism}[Organism])",
                        idtype="acc") as handle,\
            open(output_file, "w") as output:
        record = Entrez.read(handle)
        ids = ",".join(record["IdList"])
        with Entrez.efetch(db="nucleotide", id=ids, rettype=rettype, retmode="text") as handle:
            output.write(handle.read())


if __name__ == '__main__':
    download_seq(GENE, ORGANISM, output_file=OUTPUT)
