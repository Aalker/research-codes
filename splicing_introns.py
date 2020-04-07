genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = genomic_dna[0:63]
print("Exon 1: " + exon1)
exon2 = genomic_dna[90:]
print("Exon 2: " + exon2)
combined_exons = exon1 + exon2
print(combined_exons)
#Splice out the intron by knowing exactly what positions the exons are located
length_combined_exons = len(combined_exons)
print("The coding sequence length is " + str(length_combined_exons))
total_length = (len(genomic_dna))
percent_coding = length_combined_exons /total_length * 100
print("The percentage of the sequence that is coding is " + str(percent_coding))
##Print out the original DNA sequence with coding bases uppercase and non-coding bases in lowercase
intron = genomic_dna[63:90]
print(intron)
lower_intron = intron.lower()
print(lower_intron)
upper_lower_gdna = genomic_dna.replace(intron, lower_intron)
print(upper_lower_gdna)
#The example also showed this being done as a concatenation of the 3 different variables (E1, Int, E2).

