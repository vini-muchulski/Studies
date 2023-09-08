def proteins(strand):
    rna = strand

    dicionario = {
        "AUG" : "Methionine",

        "UUU":	"Phenylalanine",
        "UUC" :	"Phenylalanine",


        "UUA": "Leucine",
        "UUG"	: "Leucine",


        "UCU":	"Serine", 
        "UCC" :	"Serine", 
        "UCA":	"Serine",
        "UCG":	"Serine",


        "UAU" : "Tyrosine",
        "UAC":"Tyrosine",

        "UGU" :	"Cysteine",
        "UGC" :	"Cysteine",

        "UGG":"Tryptophan",

        "UAA":"STOP",
        "UAG":"STOP",
        "UGA":"STOP",

    }

    lista_de_proteinas = []

    for i in range(0,len(rna),3):
        codon = rna[i:i+3]
        #print(codon + "\n")

        protein = dicionario[codon]

        if(protein == "STOP"):
            break

        else:
            lista_de_proteinas.append(protein)


    return lista_de_proteinas




proteins("AUGUUUUCU")


    
