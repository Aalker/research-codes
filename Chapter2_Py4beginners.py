##printing outputs
print("Hello world")
#print(Hello World)
#Demonstrates example where quotations are used incorrectly
#prin("Hello World")
#Demonstrates example where name/function is used incorrectly
print("Hello\nworld")
# \n Demonstrates example where printed output can get split onto a separate line
# \t printed output will contain a tab
# \r printed output will make the carriage return character go to the front of the line (good for rewriting output)
my_dna = "ATCGCTA"
#Assign a variable with the equals sign
print(my_dna)
#print the string using the variable

##Manipulating strings
my_dna = "AATT" + "GGCC"
#concatenate two strings with +
print(my_dna)
upstream = "AAA"
downstream = "GGG"
my_dna = upstream + "ATGC" + downstream
print(my_dna)
#Can combine strings with variables. Order remains the same.
print("Hello" + " " + "world")

len("ATGC")
#Determine the length of the string. Output does not return number. Must be stored in a variable)
dna_length = len("AGTC")
print(dna_length)
my_dna = "ATGCGAGT"
dna_length = len(my_dna)
print("The length of the DNA sequence is " + str(dna_length))
#str() is a function which takes one argument (whose type is number), and returns a value (whose type is a string) representing that number.
number = 3 + int("4")
print(number)
#int() turns a string into a number

##method-- changing case new syntax
my_dna = "ATGC"
print(my_dna.lower())
#print my_dna in lower case
my_dna = "ATGC"
print("before: " + my_dna)
lowercase_dna = my_dna.lower()
print("after: " + my_dna)
#upper() performs the same function but makes uppercase

##replacement
protein = "vlspadktnv"
print(protein.replace("v", "y"))
#replace valine with tyrosine. First argument is "to be replaced, second is "replaced with".
print(protein.replace("vls", "ymt"))
#Can replace more than one character
print(protein)
#does not change the original, but should be utilized by making a new variable with replacement.

##Extracting a substring
protein = "vlspadktnv"
print(protein[3:5])
#print positions 3-5. Positions are inclusive at the start and exclusive at the stop (does not include positive 5 here).
print(protein[0:6])
#positions start at zero, not one
print(protein [2:])
#by not adding a number at the end,  it will go until the end of the string.

##counting and finding substrings
protein = "vlspadktnv"
valine_count = protein.count("v")
lsp_count = protein.count("lsp")
tryptophan_count = protein.count("w")
#count the amino acid residues
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))
#print the amino acid residues
print(str(protein.find("p")))
print(str(protein.find("kt")))
print(str(protein.find("w")))
#pay attention to the layering of the functions here. Start with the question: what are you looking for? (find(), where? use find as a method for the variable. Because its a number, make it a string. Then print
#If it does not exsist, the number will be -1 because 0 is position 1
#you can only search EXACT substrings






