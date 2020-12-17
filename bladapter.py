spec_list = open('species.txt').read().split('\n')

class Contigs:
      
    # init method or constructor    
    def __init__(self, tigstr):
        self.tigstr  = tigstr
        self.name = tigstr.split('\n')[0]
#         self.species = '' if tigstr[1:4] == 'tig' else tigstr[1:].split('tig')[0].split('tg')[0].split('seq')[0]
        self.species = has_species(self.name, spec_list)
        self.length = int(tigstr[tigstr.find('Length=')+7:].split('\n')[0])
#         self.tester = tigstr[tigstr.find('\n\n')+2:].split('\n\n\n')[:-1]
        self.hits = [Hits(hit) for hit in ['Score' + elem for elem in tigstr.split('Score')[1:]]]
        
    def __repr__(self):
        
        no_hit_dict = {}
        
        display = '-- Contig Class -- \n'
        display += str({key:self.__dict__[key] for key in self.__dict__ if not key == 'hits'})
        return display
    
    def fasta_hits(self, path, option='a'):
        f = open(path, option)
        for name, hit in zip([self.name+str(num) for num in range(1, 1+len(self.hits))], self.hits):
            f.write('>' + name + '\n' + hit.sbjct + '\n')
            f.close()
        return True
    
    def pos60(self):
        return bool(sum([sum([1 if pos==60 else 0 for pos in hit.qpos]) for hit in self.hits]))

class Hits:
      
    # init method or constructor    
    def __init__(self, hitstr):
#         print(hitstr)
        self.hitstr = hitstr
        if not hitstr.find('Expect = ') == -1:
            self.expect = float(hitstr[hitstr.find('Expect = ')+ 9:].split(',')[0])
        elif not hitstr.find('Expect(2) = ') == -1:
            self.expect = float(hitstr[hitstr.find('Expect(2) = ')+ 12:].split(',')[0])
        else:
            self.expect = 0
        self.query, self.qpos, self.sbjct, self.spos = self.make_seqs() 
        self.identities_number = int(hitstr[hitstr.find('Identities')+13:].split('/')[0])
        self.identities = int(hitstr[hitstr.find('Identities')+13:].split('/')[0])*100/len(self.query)
#          = [int(hitstr[hitstr.find('Query')+7:].split(' ')[0]), int(hitstr[hitstr.find('Query')+7:].split('\n')[0].split(' ')[-1])]
        self.compare = '' #need to have a lil think
#          = [int(hitstr[hitstr.find('Sbjct')+7:].split(' ')[0]), int(hitstr[hitstr.find('Sbjct')+7:].split('\n')[0].split(' ')[-1])]
        return None
        
    def __repr__(self):
        display = '-- Hits Class -- \n'
        display += str({key:self.__dict__[key] for key in self.__dict__ if not key == 'hitstr'})
        return display
    
    def fasta_save(self, path, option='a', name=None, seq=None):
        if not name:
            name = id(self)
        if not seq:
            seq = self.sbjct
        f = open(path, option)
        f.write('>' + name + '\n' + seq + '\n')
        f.close()
        return True
    
    def get_len(self):
        pass
    
    def make_seqs(self):
        query = ''
        sbjct = ''

        qpos1 = int(self.hitstr[self.hitstr.find('Query')+7:].split(' ')[0])
        spos1 = int(self.hitstr[self.hitstr.find('Sbjct')+7:].split(' ')[0])

        for section in ['Query' + elem for elem in self.hitstr.split('Query')[1:]]:
            qpos2 = int(section[section.find('Query')+7:].split('\n')[0].split(' ')[-1])
            spos2 = int(section[section.find('Sbjct')+7:].split('\n')[0].split(' ')[-1])
            query += [elem for elem in section[section.find('Query')+7:].split(' ')[1:-1] if elem][0]
            sbjct += [elem for elem in section[section.find('Sbjct')+7:].split(' ')[1:-1] if elem][0]
        return query, [qpos1, qpos2], sbjct, [spos1, spos2]

def load_contigs(input_path):
    readed = open(input_path, "r").read()
    return [Contigs(contig) for contig in readed.split('\n\n\n\n')[2].split('>')[1:]]

def has_species(namestr, spec_list):
    for spec in spec_list:
        if not namestr.find(spec) == -1:
            return spec
    return ''


header_text = 'TBLASTN 2.11.0+\n\n\nReference: Stephen F. Altschul, Thomas L. Madden, Alejandro A.\nSchaffer, Jinghui Zhang, Zheng Zhang, Webb Miller, and David J.\nLipman (1997), "Gapped BLAST and PSI-BLAST: a new generation of\nprotein database search programs", Nucleic Acids Res. 25:3389-3402.\n\n\n\nDatabase: top_contig_hits\n\n\n\nQuery= top_contigs\n\nLength=60Sequence info not for search\n\n\n'