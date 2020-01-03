#!/usr/bin/python3

'''
dnautil module contains a few useful function for dna sequence
'''

def gc(dna):
    'This function compute the gc percentage of a dna sequence'
    nbases = dna.count('n') + dna.count('N')
    gcpercent = (dna.count('g') + dna.count('G') + dna.count('c') + dna.count('C')) * 100 / (len(dna) - nbases)
    return gcpercent

def has_stop_codon(dna,frame):
    'This function check if given dna sequence has in frame stop codon'
    stop_codon_found = False
    stop_codon = ['tga', 'tag', 'taa']
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3].lower()
        if codon in stop_codon:
            stop_codon_found = True
            break
    return stop_codon_found

