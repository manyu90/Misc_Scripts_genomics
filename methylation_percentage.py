import numpy as np
import numpy as np
import pybedtools
from pysam import FastaFile
import pyBigWig
from genomedatalayer.util import nan_to_zero

#Looks at the sequence at tells you if there is a CpG dinucleotide at sequence[count]
def find_CpG(sequence,count):
    letter=sequence[count]
    if (count>0 and letter=='c' and count< len(sequence)-1):
        if sequence[count-1]=='g' or sequence[count+1]=='g':
            return True
        else:
            return False
    elif (count==0 and letter=='c' and sequence[count+1]=='g'):
        return True
    elif (count ==len(sequence)-1 and letter=='c' and sequence[count-1]=='g'):
        return True
    return False


#print (find_CpG('cttcgc',5))        
    
    
#Calculates total CpG sites, and methylation percentage in the region specified
#CpG,Total Methylation/#CpG,Total Methylation/Total Sites  is returned

def methylation_percentage(region,start,end):
    fasta_file=FastaFile('/mnt/data/annotations/by_organism/human/hg20.GRCh38/GRCh38.genome.fa')
    bw_filtered=pyBigWig.open('/mnt/lab_data/kundaje/manyu/Methylation_data/K562_wgbs_filtered.bigWig')
    sequence=fasta_file.fetch(region,start,end+1).lower()
    #print(sequence)
    count_gc=0.0
    sum_gc=0.0
    for count in xrange(len(sequence)):
        if find_CpG(sequence,count):
            count_gc+=1
    data_methylation=bw_filtered.values(region,start,end+1,numpy=True)
    nan_to_zero(data_methylation)
    sum_gc=np.sum(data_methylation)
    if count_gc>0:
        print("Returning total CpG,Fraction of methylated Cpg,Fraction of Methylated sites \n")
        print("#CpG,Total Methylation/#CpG,Total Methylation/Total Sites \n")
        return count_gc,sum_gc/count_gc,sum_gc/len(sequence)
    
    else:
        print("No CpG found")


# upper=200000
# lower=10000
# #print(fasta_file.fetch('chr7',lower,upper).lower())
# #data=bw_filtered.values('chr7',lower,upper,numpy=True)
# #nan_to_zero(data)
# #print(data)
# print(methylation_percentage('chr7',lower,upper))        
