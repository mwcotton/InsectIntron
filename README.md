# InsectIntron

A small collection of short scripts used to analyse intron stability in insects.

Based on innsect data taken from the [Darwin Tree of Life Project](https://www.darwintreeoflife.org).

Data Availability: [DToL Respository](https://github.com/darwintreeoflife/darwintreeoflife.data)

| File               | Description                                                            |
| ------------------ | ---------------------------------------------------------------------- |
| bladapter.py       | Library to handle standard blast output.                               |
| get_sequences.py   | Save full contig identified from a blast.                              |
| quick_seqs.py      | Quickly save full contiq identified from a blast.                      |
| make_tree_fasta.py | Saves contig and sbjct sequence information ready for tree generation. |
| top_contigs.py     | Saves the top hit for each species.                                    |
| filter_contigs.py  | Remove bad hits based on identities and expect value.                  |
