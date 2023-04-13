#List up all species that have selected gene
#Run this like "Listup.py geneName"
import sys

gbff_ = open('plastid.1.genomic.gbff', 'r')


gene_name = sys.argv[1]
file_name = './gene_list/' + gene_name + '.txt'

gbff = gbff_.readlines()

index = 0
translation_flag = 0
amino_acid_array = []
locus = ""
source = ""
count = 0
for line in gbff:
    if "SOURCE" in line:
        source = line[12:-1]
    if "LOCUS" in line:
        locus = line[12:21]
    if ('/gene=\"' + gene_name + '\"') in line:
        gene_position_ = gbff[index-1][21:-1]
        forward_count = gene_position_.count('(')
        back_count = gene_position_.count(')')
        back = 1
        while forward_count != back_count:
            gene_position_ = gbff[index-1-back][21:-1] + gene_position_
            forward_count = gene_position_.count('(')
            back_count = gene_position_.count(')')
            back += 1

        index2 = index + 1
        translation_flag = 0
        amino_acid = ""
        while not "CDS" in gbff[index2] and not "misc_feature" in gbff[index2] and not "gene" in gbff[index2]:
            if translation_flag:
                amino_acid += gbff[index2][21:-1]
            if "/translation" in gbff[index2]:
                translation_flag = 1
                amino_acid = gbff[index2][35:-1]
            index2 += 1
        if translation_flag:
            amino_acid_array.append([locus, source, amino_acid[:-1], gene_position_])
    index += 1

with open(file_name, 'a') as f:
    for i in amino_acid_array:
        f.write("LOCUS:" + i[0] + "\n")
        f.write("   SOURCE:" + i[1] + "\n")
        f.write("   Position:" + i[3] + "\n")
        f.write("   Amino acid:" + i[2] + "\n")    