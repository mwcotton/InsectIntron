#!/bin/bash

# tblastn -query enenbeetle.fasta -db longer_contigs/longer_contigs -out longer_hits.txt

# makeblastdb -in more_contigs.fasta -dbtype nucl -out longer_contigs/longer_contigs

#initial search

#get top hits

#research top hits

#filter top hits

#identify if intro


 #add all species to a single fasta file

cat *.fasta >  all_species.fasta

#initial engrailed search

makeblastdb -in all_species.fasta -dbtype nucl -out first_blastdb

tblastn -query engrailed.fasta -db first_blastdb -out prelim_blast.txt

#save top hit for each species

python3 top_contigs.py prelim_blast.txt prelim_top.txt

#search the full contig for top hits

python3 quick_seqs.py prelim_top.txt prelim_contigs.fasta

makeblastdb -in prelim_contigs.fasta -dbtype nucl -out contigs_blastdb

tblastn -query engrailed.fasta -db contigs_blastdb -out contig_blast.txt

#manual search, stitching and reciprocal blast currently required at this point