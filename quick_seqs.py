import sys
import glob
import bladapter as bl

_, pathin, pathout = sys.argv

top_contigs = bl.load_contigs(pathin)

names = {contig.species:contig.name for contig in top_contigs}
files = {spec:glob.glob('../wgot/fastas/*{}*'.format(spec))[0] for spec in bl.spec_list}


for contig in top_contigs:
    whole_file = open(files[contig.species]).read()
    tig_loc = whole_file.find(contig.name.split(contig.species)[1])
    
    contig_seq = ''

    for elem in whole_file[tig_loc:].split('>')[0].split('\n')[1:]:
        contig_seq += elem

    print('Writing sequence for :{}'.format(contig.name))
    f = open(pathout, 'a')
    f.write('>' + contig.name + '\n' + contig_seq + '\n')
    f.close()