import numpy as np


def extract_motif_from_text(text):
    vals = []
    for line in text:
        arr=[]
        line_split = line.strip().split()
        for elem in line_split:
            arr.append(float(elem.strip()))
        vals.append(arr)
    return np.array(vals)

def parse_MEME(meme):
    with open(meme,'r') as f:
        data = f.readlines()
    
    motifs_dict = {}
    count_tf = 0
    for i,line in enumerate(data):
        if line.startswith('MOTIF'):
            line_split = line.split()
            TF = line_split[-1]
            count_tf+=1

            length_motif = int(data[i+2].split()[5])

            motif_info = data[i+3:i+3+length_motif]
            motif_array = extract_motif_from_text(motif_info)
            motifs_dict[TF] = motif_array
            print(TF,motif_array)
    return motifs_dict
           

