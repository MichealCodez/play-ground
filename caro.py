inputfile= input("Write the file name to analize: ")

Aminoacids = {
        'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
        'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
        'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
        'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
        'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
        'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
        'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
        'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
        'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
        'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
        'TAA': '-',     'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
        'TAG': '-',     'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
        'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
        'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
        'TGA': '-',     'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
        'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
    }

sequences = []
descr = None
# here is the path of multifalsta file
with open(inputfile) as file:
    line = file.readline()[:-1]  # always trim newline
    while line:
        if line[0] == '>':
            if descr:  # any sequence found yet?
                sequences.append((descr, seq))
            descr = str(line[1:].split('>'))
            seq = ''  # start a new sequence
        else:
            seq += line
        line = file.readline()[:-1]
    sequences.append((descr, seq))
    #print(sequences)
listOfOrf = list()
for index, value in enumerate(sequences):  # looping over the fragments extracted
    frames = [] # storing the six frame translation that it zould be extacted from the fragments
    dna = value[1]  # extract the fragment
    description = value[0] #extact the desciption even were not use it, just for learning purpose
    reverseCdna = [] # storing the reverse compliments
    # create the positive frames
    # split the frames into codons for better performance
    frames.append([dna[i:i + 3] for i in range(0, len(dna), 3)])
    frames.append([dna[i:i + 3] for i in range(1, len(dna), 3)])
    frames.append([dna[i:i + 3] for i in range(2, len(dna), 3)])
    # reverse compliment of the fragment
    reverse = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for i in range(len(dna)):
        reverseCdna.append(reverse[dna[-i - 1]]) if dna[-i - 1] in reverse.keys() else reverseCdna.append(dna[-i - 1])  # if any contamination found we keep it for further more check
    reverseCdna = ''.join(reverseCdna) # joining
    # create the negative frames
    frames.append([reverseCdna[i:i + 3] for i in range(0, len(reverseCdna), 3)])
    frames.append([reverseCdna[i:i + 3] for i in range(1, len(reverseCdna), 3)])
    frames.append([reverseCdna[i:i + 3] for i in range(2, len(reverseCdna), 3)])
    #print(frames)

    for i in range(0,len(frames),1): #looping all the frames
        start=0
        while start <len(frames[i]): #looping each frame for start and stop codons
            if frames[i][start]=="ATG":
#            if frames[i][start]=="ATG" or frames[i][start]=="TTG" or frames[i][start]=="CTG" or frames[i][start]=="GTG":
                for stop in range(start+1,len(frames[i]),1):
                             if frames[i][stop]=="TAA" or  frames[i][stop]=="TAG" or  frames[i][stop]=="TGA" :
                                    listOfOrf.append(frames[i][start:stop]) # retrieve the orf
                                    start=stop+1 # avoiding multiple start codons
                                    #DNA = listOfOrf[1]
                                    #longest= sorted(listOfOrf,key=len)
                                    print(listOfOrf)
                                    result = []
                                    for m in listOfOrf:
                                         temp = []
                                         temp1 = []
                                         for j in m:
                                             if j in Aminoacids:
                                                 temp1.append(Aminoacids[j])
                                         temp.append(''.join(temp1))
                                         result.append(temp)
                                    print(f'Result = {result}')
                                    length1 = []
                                    for n in result:
                                        length1.append(len(n))
                                    ma = max(length1)
                                    ind1 = length1.index(ma)
                                    print(result[ind1][0])
                                    #print("open reading frames find in", description, "are :", listOfOrf)
            start+=1

# dictionary = {
#     'GTC': 'k',
#     'KTC': 'J',
#     'AAA': 'L'
# }
#
# list1 = [['GTC', 'AAA'], ['KTC'], ['AAA', 'KTC', 'GTC']]
# list2 = [['GTC', 'AAA'], ['KTC'], ['AAA', 'KTC', 'GTC']]
# list3 = [['GTC', 'AAA'], ['KTC'], ['AAA', 'KTC', 'GTC']]
#
#
# def solution(dictionary, *listoflist):
#     final_result = []
#     for k in listoflist:
#         result = []
#         for i in k:
#             temp = []
#             temp1 = []
#             for j in i:
#                 if j in dictionary:
#                     temp1.append(dictionary[j])
#             temp.append(''.join(temp1))
#             result.append(temp)
#         final_result.append(result)
#     return final_result
#
#
# all_lists = solution(dictionary, list1, list2, list3)
#
# for i in all_lists:
#     print(i)
