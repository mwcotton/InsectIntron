import bladapter as bl
import sys

_, pathin, pathout = sys.argv

print('Loading contigs from {}'.format(pathin))

contigs = bl.load_contigs(pathin)

temp_list = bl.spec_list.copy()
top_contig = {}
for contig in contigs:
    if contig.species in temp_list:
        temp_list.remove(contig.species)
        top_contig[contig.species] = contig
        if not top_contig:
            break
        
top_contig, 

if temp_list:
    print('/n/nWarning: no contig matches for:', *temp_list)
    
print('Saving top_contigs to {}'.format(pathout))

f = open(pathout, 'a')
f.write(bl.header_text)
for key in top_contig:
    contig = top_contig[key]
    f.write('>' + contig.tigstr)
    for hit in contig.hits:
        f.write(hit.hitstr)
f.close()

print('Done')