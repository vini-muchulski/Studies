



def to_rna(dna_strand):
    rna = dna_strand

    rna_transcriptado = ""

    for base in range(0,len(rna)):
        if( rna[base] == "G"):
            rna_transcriptado += "C"

        if( rna[base].upper() == "C"):
            rna_transcriptado += "G"

        if( rna[base].upper() == "T"):
            rna_transcriptado += "A"
        
        if( rna[base].upper() == "A"):
            rna_transcriptado += "U"

    return rna_transcriptado
    
print(to_rna("ACGTGGTCTTAA"))