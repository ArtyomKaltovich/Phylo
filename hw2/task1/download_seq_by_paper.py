from Bio import Entrez

ID = 12890024
OUTPUT = "result/seq_from_paper.fasta"
Entrez.email = "Your.Name.Here@example.org"


def download_seq(paper_id, *, output_file, rettype="fasta", retmax=10):
    with Entrez.elink(dbfrom="pubmed", db="nucleotide", id=paper_id,
                      linkname="pubmed_nuccore", retmax=retmax) as handle,\
            open(output_file, "w") as output:
        record = Entrez.read(handle)
        ids = []
        for v in record[0]["LinkSetDb"][0]["Link"]:
            ids.extend(v.values())
        with Entrez.efetch(db="nucleotide", id=ids, rettype=rettype, retmode="text", retmax=retmax) as handle:
            output.write(handle.read())


if __name__ == '__main__':
    download_seq(ID, output_file=OUTPUT)
