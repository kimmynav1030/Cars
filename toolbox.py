rna_seq = "AUGGGCGGAUACCCCUUAUUG" 
    #defining the seqence we want to analyze
len(rna_seq) #to test the value of the length
print(rna_seq)
def another_rna_to_aa(rna):     #defining the function - def function():
                                #don't have to have an input
    codons = {'Phe': ['UUU', 'UUC'],
                                #defining the meaning of the codons within curly
                                #brackets -- each comma after last row of []
                                #bracketis a definition in the dictionary


              'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'Ile': ['AUU', 'AUC', 'AUA'],
              'Met': ['AUG'],
              'Val': ['GUU', 'GUC', 'GUA', 'GUG'],
              'Ser': ['UCU', 'UCC', 'UCA', 'UCG'],
              'Pro': ['CCU', 'CCC', 'CCA', 'CCG'],
              'Thr': ['ACU', 'ACC', 'ACA', 'ACG'],
              'Ala': ['GCU', 'GCC', 'GCA', 'GCG'],
              'Tyr': ['UAU', 'UAC'],
              'Stop': ['UAA', 'UAG', 'UGA'],
              'His': ['CAU', 'CAC'],
              'Gln': ['CAA', 'CAG'],
              'Asn': ['AAU', 'AAC'],
              'Lys': ['AAA', 'AAG'],
              'Asp': ['GAU', 'GAC'],
              'Glu': ['GAA', 'GAG'],
              'Cys': ['UGU', 'UGC'],
              'Trp': ['UGG'],
              'Arg': ['CGU', 'CGC', 'CGA', 'CGG'],
              'Ser': ['AGU', 'AGC'],
              'Arg': ['AGA', 'AGG'],
              'Gly': ['GGU', 'GGC', 'GGA', 'GGG']}
    codon_list = [rna[index:index + 3] for index in range(0, len(rna), 3)]
    aa_seq = ''
    for codon in codon_list: #filtering through list 2
      for key in codons.keys(): #filtering through list 1
        if codon in codons[key]: #conditional statement to add string into vaule
          aa_seq += key + ' ' # aa_seq = aa=seq + key + ' ' -- formatting
    return aa_seq.rstrip()    #returning string values by slicing the genes

translated_aa = another_rna_to_aa(rna_seq) #defining new string value, using
  #the function above, the input "rna_seq" is filtered through to produce the
  #needed string
print(translated_aa)
  #telling python to print the ones we want