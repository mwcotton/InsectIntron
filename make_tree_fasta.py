import bladapter as bl
import sys

_, pathin, pathout = sys.argv

contigs = bl.load_contigs(pathin)

for contig in contigs:
    write_val = '>' + contig.name + '\n' + contig.hits[0].sbjct + '\n'
    f = open(pathin, 'a')
    f.write(write_val)
    f.close()