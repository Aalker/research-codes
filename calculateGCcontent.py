dna_nt = "ATGCAACAACAAGAACAGGAGCAAGCTCCTACCTTTCAAAGTTATCCCACGCGCACTGCGTTATCAGTGA"
#figure out how to not hardcode this sequence in the future. Read in function?
dna_length = len(dna_nt)
total_dna = (int(dna_length))
#Use the int() function to make total_dna a number that can be operated on with equations
print(total_dna)
#determine the total number of nucleotides in the protein sequence.
g_content = dna_nt.count("G")
print(g_content)
#Determine the number of Gs in the nucleotide sequence
c_content = dna_nt.count("C")
print(c_content)
#Determine the number of Cs in the nucleotide sequence
gc_content = (int(g_content) + int(c_content)) / total_dna
print(gc_content)
percent_gc_content = gc_content * 100
print(percent_gc_content)
print("The percent gc content is: " + str(percent_gc_content) + "%")
