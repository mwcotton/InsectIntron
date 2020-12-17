# InsectIntron

A small collection of short scripts used to analyse intron stability in insects.

Based on innsect data taken from the [Darwin Tree of Life Project](https://www.darwintreeoflife.org).

Data Availability: [DToL Respository](https://github.com/darwintreeoflife/darwintreeoflife.data)

## Repository Contents

| File               | Description                                                            |
| ------------------ | ---------------------------------------------------------------------- |
| bladapter.py       | Library to handle standard blast output.                               |
| get_sequences.py   | Save full contig identified from a blast.                              |
| quick_seqs.py      | Quickly save full contiq identified from a blast.                      |
| make_tree_fasta.py | Saves contig and sbjct sequence information ready for tree generation. |
| top_contigs.py     | Saves the top hit for each species.                                    |
| filter_contigs.py  | Remove bad hits based on identities and expect value.                  |

## Pipeline

An example pipeline may look as follows.

```bash
 #add all species to a single fasta file

cat *.fasta >  all_species.fasta

#initial engrailed search

makeblastdb -in all_species.fasta -dbtype nucl -out first_blastdb

tblastn -query engrailed.fasta -db first_blastdb -out prelim_blast.txt

#save top hit for each species

python3 top_contigs.py prelim_blast.txt prelim_top.txt

#search the full contig for top hits

python3 quick_seqs.py prelim_top.txt prelim_contigs.fasta





```
