import pandas as pd
from Bio import Entrez

GENE = "ABO"
ORGANISM = "horse"
OUTPUT = "result/summary.csv"
Entrez.email = "Your.Name.Here@example.org"


def summary(gene, organism, *, output_file, retmax=10):
    with Entrez.esearch(db="nucleotide", retmax=retmax, term=f"({gene}[Gene Name]) AND {organism}[Organism])",
                        idtype="acc") as handle:
        record = Entrez.read(handle)
        ids = ",".join(record["IdList"])
        with Entrez.esummary(db="nucleotide", id=ids, retmode="xml") as handle:
            record = Entrez.parse(handle)
            result = {"UID": [], "Accesion Number": [], "Length": []}
            for r in record:
                for key, field in zip(result, ["Id", "Caption", "Length"]):
                    value = r[field]
                    if isinstance(value, int):  # for IntegerObject
                        value = int(value)
                    result[key].append(value)
        pd.DataFrame(result).to_csv(output_file)


if __name__ == '__main__':
    summary(GENE, ORGANISM, output_file=OUTPUT)
