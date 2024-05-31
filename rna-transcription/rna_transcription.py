def to_rna(dna_strand):
    str=''
    for i in range(len(dna_strand)):
        if dna_strand[i]=='G':
            str+='C'
        elif dna_strand[i]=='C':
            str+= 'G'
        elif dna_strand[i]=='T':
            str+= 'A'
        elif dna_strand[i]=='A':
            str+= 'U'
    return str
    pass
