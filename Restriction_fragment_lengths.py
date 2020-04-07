dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
EcoR1 = dna.find("GAATTC")
print("The start position of the restriction cut site is " + str(EcoR1) + ", which is inclusive")
#This provides the start residue for the restriction fragment
fragment1 = dna[0:int(EcoR1) + 1 ]
#The end position is exclusive, so an extra base must be added (+1)
print("Fragment 1 is " + fragment1)
fragment1_length = len(fragment1)
print(str(fragment1_length))
#fragment1 = len(EcoR1)
#print(fragment1)
total_length = len(dna)
print(total_length)
print((int(total_length) - int(fragment1_length)))
fragment2 = dna[22:]
print("Fragment 2 is " + fragment2)
