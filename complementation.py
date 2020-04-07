dna_nt = "ATGCAACAACAAGAACAGGAGCAAGCTCCTACCTTTCAAAGTTATCCCACGCGCACTGCGTTATCAGTGA"
A_replaced = dna_nt.replace("A", "t")
#convert to the lower case version to ensure that the "T"s dont get converted back to As by the next replacement.
T_replaced = A_replaced.replace("T", "a")
C_replaced = T_replaced.replace("C", "g")
G_replaced = C_replaced.replace("G", "c")
print(G_replaced)
complement = G_replaced.upper()
#convert the string from lower case to upper case to return the string to its original form
print(complement)
