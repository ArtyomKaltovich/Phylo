# Comparision of different multiply alignment utilities

## Part 1

### Materials and Methods

10 coding sequences of Sup35 protein of yeasts. They was aligned by 4 different tools
and than the alignment was checked with gblocks.

### Tools

* trying to use clustalw
> https://www.ebi.ac.uk/Tools/msa/clustalw2/
>
>The ClustalW2 services have been retired. To access similar services, please visit the Multiple Sequence Alignment tools page. For protein alignments we recommend Clustal Omega. For DNA alignments we recommend trying MUSCLE or MAFFT. If you have any questions/concerns please contact us via the feedback link above.

| Tool        | Gblocks result | Execution Time | Description |
| ----------- | -------------- | -------------- | ----------- |
| MUSCLE 3.8.31 | 1753  (77% of the original 2275 positions) | 10s       | [results](https://www.ebi.ac.uk/Tools/services/web_muscle/toolresult.ebi?jobId=muscle-E20200318-162231-0045-12801604-p2m) |
| MAFFT 7.42    | 1786  (78% of the original 2286 positions) | 7s        | [results](https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=mafft-I20200318-165939-0743-7720800-p2m)|
| KALIGH 2.04   | 1377  (55% of the original 2500 positions) | 3s        | [results](https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=kalign-I20200318-175017-0237-3550769-p2m)|
| T-COFFEE 11.00.8cbe486 | 1722  (77% of the original 2210 positions) | 39s        | [results](https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=tcoffee-I20200318-175231-0863-95195112-p2m)|

T-COFFEE has the longest run time, but also produce shortest alignment.
I suggest using T-COFFEE, because it produce good alignment, and MAFFT or MUSCLE for long data.

## Part 2

### Materials and Methods

10 coding sequences from part 1 were translated to proteins. Then the same pipeline was used.

### Tools

| Tool        | Gblocks result | Execution Time | Description |
| ----------- | -------------- | -------------- | ----------- |
| MUSCLE 3.8.31 | 553  (74% of the original 743 positions) | 2s       | [results](https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=muscle-I20200319-110812-0071-6227165-p2m) |
| MAFFT 7.42    | 542  (71% of the original 754 positions) | 9s        | [results](https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=mafft-I20200319-110531-0899-55658629-p2m)|
| KALIGH 2.04   | 480  (60% of the original 793 positions) | 3s        | [results](https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=kalign-I20200319-102630-0853-78843857-p2m)|
| T-COFFEE 11.00.8cbe486 | 558  (74% of the original 752 positions) | 8s        | [results](https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=tcoffee-I20200319-111109-0495-51696271-p2m)|

MUSCLE is the fastest and produce the best alignment.

## SUP35_10seqs_strange_aln.fa

One of the sequences (SUP35_Spar_A12_Liti) doesn't start with start codon and doesn't stop with stop codon. 
