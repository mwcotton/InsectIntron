import bladapter as bl
import sys

_, pathin, pathout = sys.argv

database = open(pathin).read()[open(pathin).read().find('Database: ')+10:].split('\n')[0]
print('Using database located at {}'.format(database))
print('Loading top conntigs from {}'.format(database))

contigs = bl.load_contigs(pathin)

current_write = ''

for contig in contigs:

    loc = -1
    
    with open(database, 'r') as full_db:
        for num, line in enumerate(full_db):
            if contig.name in line:
                loc = num
                print('Contig found:', contig.name)
                break
        for num, line in enumerate(full_db):
            if loc == -1:
                print('Contig not located:', contig.name)
                break
            elif num == loc+1:
                print('Sequence found:', contig.name)
                current_write += line
                break

    f = open(pathout, 'a')
    f.write(current_write)
    f.close()