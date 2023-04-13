#To find the synonymous mutations of Serine!
#Run this like "Smuta.py fileName speiceID1 speiceID2"
#This code is messed up.I'm sorry for that.
import sys
import subprocess

id = [sys.argv[1],sys.argv[2]]
# gene_list = gene_list = ['rps12', 'trnH-GTG', 'psbA', 'matK', 'rps16', 'trnQ-TTG', 'trnN-GTT', 'psbK', 'psbI', 'trnS-GCT', 'trnR-TCT', 'atpA', 'atpF', 'atpH', 'atpI', 'rps2', 'rpoC2', 'rpoC1', 'rpoB', 'trnC-GCA', 'petN', 'psbM', 'trnD-GTC', 'trnY-GTA', 'trnE-TTC', 'trnT-GGT', 'psbD', 'psbC', 'trnS-TGA', 'psbZ', 'trnG-GCC', 'trnfM-CAT', 'rps14', 'psaB', 'psaA', 'ycf3', 'trnS-GGA', 'rps4', 'trnT-TGT', 'trnF-GAA', 'ndhJ', 'ndhK', 'ndhC', 'trnM-CAT', 'atpE', 'atpB', 'rbcL', 'accD', 'psaI', 'ycf4', 'cemA', 'petA', 'psbJ', 'psbL', 'psbF', 'psbE', 'petL', 'petG', 'trnW-CCA', 'trnP-TGG', 'psaJ', 'rpl33', 'rps18', 'rpl20', 'clpP', 'psbB', 'psbT', 'psbN', 'psbH', 'petB', 'petD', 'rpoA', 'rps11', 'rpl36', 'infA', 'rps8', 'rpl14', 'rpl16', 'rps3', 'rpl22', 'rps19', 'rpl23', 'trnI-CAT', 'ycf2', 'ycf15', 'trnL-CAA', 'ndhB', 'rps7', 'trnV-GAC', 'rrn16S', 'rrn23S', 'rrn4.5S', 'rrn5S', 'trnR-ACG', 'ndhF', 'rpl32', 'trnL-TAG', 'ccsA', 'ndhD', 'psaC', 'ndhE', 'ndhG', 'ndhI', 'ndhA', 'ndhH', 'rps15', 'ycf1', 'trnH-GUG', 'trnK-UUU', 'trnQ-UUG', 'trnS-GCU', 'trnG-UCC', 'trnR-UCU', 'trnD-GUC', 'trnY-GUA', 'trnE-UUC', 'trnT-GGU', 'trnS-UGA', 'trnfM-CAU', 'trnT-UGU', 'trnL-UAA', 'trnV-UAC', 'trnM-CAU', 'trnP-UGG', 'trnI-CAU', 'rrn16', 'trnI-GAU', 'trnA-UGC', 'rrn23', 'rrn4.5', 'rrn5', 'trnN-GUU', 'trnL-UAG', 'lhbA', 'psbG', 'trnQ_UUG', 'trnS_GCU', 'trnG_UCC', 'trnR_UCU', 'trnC_GCA', 'trnD_GUC', 'trnY_GUA', 'trnE_UUC', 'trnT_GGU', 'trnS_UGA', 'trnG_GCC', 'trnfM_CAU', 'trnS_GGA', 'trnT_UGU', 'trnL_UAA', 'trnF_GAA', 'trnV_UAC', 'trnM_CAU', 'trnW_CCA', 'trnP_UGG', 'trnH_GUG', 'trnI_CAU', 'trnL_CAA', 'trnV_GAC', 'trnI_GAU']
# gene_list =['rpl23', 'trnI-CAT', 'ycf2', 'ycf15', 'trnL-CAA', 'ndhB', 'rps7', 'trnV-GAC', 'rrn16S', 'rrn23S', 'rrn4.5S', 'rrn5S', 'trnR-ACG', 'ndhF', 'rpl32', 'trnL-TAG', 'ccsA', 'ndhD', 'psaC', 'ndhE', 'ndhG', 'ndhI', 'ndhA', 'ndhH', 'rps15', 'ycf1', 'trnH-GUG', 'trnK-UUU', 'trnQ-UUG', 'trnS-GCU', 'trnG-UCC', 'trnR-UCU', 'trnD-GUC', 'trnY-GUA', 'trnE-UUC', 'trnT-GGU', 'trnS-UGA', 'trnfM-CAU', 'trnT-UGU', 'trnL-UAA', 'trnV-UAC', 'trnM-CAU', 'trnP-UGG', 'trnI-CAU', 'rrn16', 'trnI-GAU', 'trnA-UGC', 'rrn23', 'rrn4.5', 'rrn5', 'trnN-GUU', 'trnL-UAG', 'lhbA', 'psbG', 'trnQ_UUG', 'trnS_GCU', 'trnG_UCC', 'trnR_UCU', 'trnC_GCA', 'trnD_GUC', 'trnY_GUA', 'trnE_UUC', 'trnT_GGU', 'trnS_UGA', 'trnG_GCC', 'trnfM_CAU', 'trnS_GGA', 'trnT_UGU', 'trnL_UAA', 'trnF_GAA', 'trnV_UAC', 'trnM_CAU', 'trnW_CCA', 'trnP_UGG', 'trnH_GUG', 'trnI_CAU', 'trnL_CAA', 'trnV_GAC', 'trnI_GAU']
# gene_list = ["accD", 'atpB', 'atpE', 'psal', 'rbcL']
gene_list = ["ycf1"]

for geneL in gene_list:
    gene_file_name = geneL + '.txt'
    print(geneL)

    fasta_name = [gene_file_name[:-4] + '_' + id[0] + '.fa', gene_file_name[:-4] + '_' + id[1] + '.fa']
    output_maf_name = gene_file_name[:-4] + '_' + id[0] + '_' + id[1] + '.maf'
    # print(output_maf_name)

    fasta_ = open('plastid.genomic.fna', 'r')
    gene_file_ = open('./gene_list/' + gene_file_name, 'r')

    fasta = fasta_.readlines()
    gene_file = gene_file_.readlines()

    position_ = ["",""]
    amino_acid = ["",""]
    index = 0
    for line in gene_file:
        for i in range(2):
            if id[i] in line:
                position_[i] = gene_file[index+2][12:-1]
                amino_acid[i] = gene_file[index+3][14:-1]
        index += 1
    if position_[0] == "" or position_[1] == "":
        continue
    base_array = ["",""]
    complement_join = [[],[]]
    position = [[],[]]
    for i in range(2):
        skip = 0
        start_num = 0
        end_num = 0
        start_end_flag = 0
        comp_stop_signal = 0
        if not '(' in position_[i]:
            # print(position_[i].split('.'))
            startP = position_[i].split('.')[0]
            endP = position_[i].split('.')[2]
            position[i].append([int(startP), int(endP), 0])
        else:
            # print(position_[i])
            for chara in position_[i]:
                # print(complement_join)
                if skip > 0:
                    skip -= 1
                    continue
                if chara == 'c':
                    complement_join[i].append(0)
                    skip += 10
                if chara == 'j':
                    complement_join[i].append(1)
                    skip += 4
                if chara == ',':
                    if comp_stop_signal:
                        comp_stop_signal = 0
                    else:
                        start_end_flag = 0
                        if not 0 in complement_join[i]:#complement外の時
                            position[i].append([start_num, end_num, 0])
                            # print('A')
                        else:#complement内の時
                            position[i].append([start_num, end_num, 1])
                            # print('B')
                        start_num = 0
                        end_num = 0
                if chara == ')':
                    if not complement_join[i][-1]:#complementの動作
                        complement_join[i].pop()
                        start_end_flag = 0
                        position[i].append([start_num, end_num, 1])
                        start_num = 0
                        end_num = 0
                        comp_stop_signal = 1
                        tmp = []
                        j = len(position[i])-1
                        k = 0
                        # print(position[i][j][2])
                        # print(position)
                        while position[i][j][2]:
                            tmp.append([position[i][j][1], position[i][j][0]])
                            if j == 0:
                                break
                            j -= 1
                        while j < len(position[i]):
                            # print(k)
                            position[i][j][0] = tmp[k][0]
                            position[i][j][1] = tmp[k][1]
                            position[i][j][2] = 0
                            k += 1
                            j += 1
                    else:
                        start_end_flag = 0
                        if not 0 in complement_join[i]:#complement外の時
                            position[i].append([start_num, end_num, 0])
                            # print('A')
                        else:#complement内の時
                            position[i].append([start_num, end_num, 1])
                            # print('B')
                        start_num = 0
                        end_num = 0
                        complement_join[i].pop()
                if chara.isdigit():
                    if not start_end_flag:
                        start_num *= 10
                        start_num += int(chara)
                    else:
                        end_num *= 10
                        end_num += int(chara)
                if chara == '.':
                    start_end_flag = 1

    # print(position)
    index2 = 0
    checked = [1,1]
    for line in fasta:
        for i in range(2):
            if id[i] in line:
                if checked[i]:
                    checked[i] = 0
                    for base_range in position[i]:
                        # print(base_range)
                        if base_range[0] < base_range[1]:#forward
                            base_line_s = ((base_range[0]-1) // 80) + index2 + 1
                            base_line_e = ((base_range[1]-1) // 80) + index2 + 1
                            if base_line_s == base_line_e:
                                if base_range[1] % 80 != 0:
                                    base_array[i] += fasta[base_line_s][(base_range[0]-1)%80:(base_range[1])%80]
                                    # print(base_array)
                                else:
                                    base_array[i] += fasta[base_line_s][(base_range[0]-1)%80:-1]
                                    # print(base_array)
                            else:
                                base_array[i] += fasta[base_line_s][(base_range[0]-1)%80:-1]
                                # print(base_array)
                                base_line_s += 1
                                while base_line_s < base_line_e:
                                    base_array[i] += fasta[base_line_s][:-1]
                                    # print(base_array)
                                    base_line_s += 1
                                if base_range[1] % 80 != 0: 
                                    base_array[i] += fasta[base_line_s][:base_range[1]%80]
                                    # print(base_array)
                                else:
                                    base_array[i] += fasta[base_line_s][-1]
                                    # print(base_array)
                        else:#backward
                            base_line_s = ((base_range[0]-1) // 80) + index2 + 1
                            base_line_e = ((base_range[1]-1) // 80) + index2 + 1
                            if base_line_s == base_line_e:
                                if (base_range[1]-1) % 80 != 0:
                                    base_array[i] += fasta[base_line_s][(base_range[0]-1)%80:(base_range[1]-2)%80:-1].translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))
                                else:
                                    base_array[i] += fasta[base_line_s][(base_range[0]-1)%80::-1].translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))
                            else:
                                base_array[i] += fasta[base_line_s][(base_range[0]-1)%80::-1].translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))
                                # print(base_array)
                                base_line_s -= 1
                                while base_line_s > base_line_e:
                                    base_array[i] += fasta[base_line_s][-2::-1].translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))
                                    base_line_s -= 1
                                    # print(base_array)
                                if (base_range[1]-1) % 80 != 0:
                                    base_array[i] += fasta[base_line_s][-2:(base_range[1]-2)%80:-1].translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))
                                    # print(base_array)
                                else:
                                    base_array[i] += fasta[base_line_s][-2::-1].translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))
                                    # print(base_array)                       
        index2 += 1

    for i in range(2):
        with open(fasta_name[i], 'a') as f:
            f.write('>' + id[i] + '\n')
            f.write(base_array[i])

    subprocess.run('lastdb humdb ' + fasta_name[0], shell = True)
    subprocess.run('lastal humdb ' + fasta_name[1] +  ' > ' + output_maf_name, shell = True)
    subprocess.run('rm ' + fasta_name[0], shell = True)
    subprocess.run('rm ' + fasta_name[1], shell = True)

    maf_file_ = open(output_maf_name, 'r')
    maf_file = maf_file_.readlines()

    #subprocess.run('rm ' + output_maf_name, shell = True)

    Genetic_Code = ["TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG","TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG","TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG","FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"]

    index3 = 0
    for line in maf_file:
        if 'score' in line:
            line1 = maf_file[index3+1].split(' ')[-1]
            line2 = maf_file[index3+2].split(' ')[-1]
            index4 = 0
            while line1[index4] != '\n':
                # print(line1[index4])
                # print(line1[index4+1])
                # print(line1[index4+2])
                if line1[index4+1] == '\n':
                    break
                if line1[index4+2] == '\n':
                    break
                if line1[index4] == '-' or line1[index4+1] == '-' or line1[index4+2] == '-':
                    index4 += 3
                    continue
                index5 = Genetic_Code[0].index(line1[index4].upper())
                # print(index5)
                index5 = index5 + Genetic_Code[1][index5:index5+16].index(line1[index4+1].upper())
                # print(index5)
                index5 = index5 + Genetic_Code[2][index5:index5+4].index(line1[index4+2].upper())
                # print(index5)
                the_amino_acid = Genetic_Code[3][index5]

                if the_amino_acid == 'S':
                    if line2[index4] == '-' or line2[index4+1] == '-' or line2[index4+2] == '-':
                        index4 += 3
                        continue
                    index6 = Genetic_Code[0].index(line2[index4].upper())
                    index6 = index6 + Genetic_Code[1][index6:index6+16].index(line2[index4+1].upper())
                    index6 = index6 + Genetic_Code[2][index6:index6+4].index(line2[index4+2].upper())
                    the_amino_acid2 = Genetic_Code[3][index6]
                    if the_amino_acid2 == 'S':
                        # print("S match!!!")
                        if line1[index4].upper() != line2[index4].upper():
                            print(line1[index4])
                            print(line1[index4+1])
                            print(line1[index4+2])
                            print(line2[index4])
                            print(line2[index4+1])
                            print(line2[index4+2])
                            print("synonymous mutations in position1")
                        if line1[index4+1].upper() != line2[index4+1].upper():
                            print("synonymous mutations in position2")
                        # if line1[index4+2].upper() != line2[index4+2].upper():
                        #     print("synonymous mutations in position3")

                # print(the_amino_acid)
                index4 += 3
        index3 += 1


