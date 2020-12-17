#!/bin/bash

tblastn -query enenbeetle.fasta -db longer_contigs/longer_contigs -out longer_hits.txt

makeblastdb -in more_contigs.fasta -dbtype nucl -out longer_contigs/longer_contigs

#initial search

#get top hits

#research top hits

#filter top hits

#identify if intro