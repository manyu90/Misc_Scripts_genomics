

import gzip
import os
import sys
import glob
import re


#Takes a bed methyl file as an input and filters out positions with read coverage >10 reads
def process_data_10_reads(inputfile,outfile):
    # if os.path.isfile(outfile):
    #     print("File %s exists"%outfile)
    g=open(outfile,'w')
    
    if re.search('.gz', inputfile):
        f=gzip.open(inputfile,'rb')
        
        for line in f:
            line=line.decode("utf-8") 
        # print (type(line))
            line=line.split('\t')
            if (int(line[9]))>=10:
                g.write('\t'.join(line))
        g.close()

    else:
        f=open(inputfile,'r')  
        for line in f:
        # print (type(line))
            line=line.split('\t')
            if (int(line[9]))>=10:
                g.write('\t'.join(line))
        g.close()  

    
    
    #g.close()
    f.close()
    print("Wrote to file %s"%(outfile))
    return




if __name__=='__main__':
    input_file='/srv/scratch/manyu/Methylation_data/K562/MethCpG_rep1.bedMethyl.gz'
    output_file='/srv/scratch/manyu/Methylation_data/K562/MethCpG_rep1_filtered.bedMethyl'
    process_data_10_reads(input_file,output_file)
    inputfile='/srv/scratch/manyu/Methylation_data/K562/MethCpG_rep2.bedMethyl.gz'
    output_file='/srv/scratch/manyu/Methylation_data/K562/MethCpG_rep2_filtered.bedMethyl'
    process_data_10_reads(input_file,output_file)
    input_file='/srv/scratch/manyu/Methylation_data/GM12878/MethCpG_rep1.bedMethyl.gz'
    output_file='/srv/scratch/manyu/Methylation_data/GM12878/MethCpG_rep1_filtered.bedMethyl'
    process_data_10_reads(input_file,output_file)
    inputfile='/srv/scratch/manyu/Methylation_data/GM12878/MethCpG_rep2.bedMethyl.gz'
    output_file='/srv/scratch/manyu/Methylation_data/GM12878/MethCpG_rep2_filtered.bedMethyl'
    process_data_10_reads(input_file,output_file)
    input_file='/srv/scratch/manyu/Methylation_data/H1-hESC/MethCpG_rep1.bedMethyl.gz'
    output_file='/srv/scratch/manyu/Methylation_data/H1-hESC/MethCpG_rep1_filtered.bedMethyl'
    process_data_10_reads(input_file,output_file)
    inputfile='/srv/scratch/manyu/Methylation_data/H1-hESC/MethCpG_rep2.bedMethyl.gz'
    output_file='/srv/scratch/manyu/Methylation_data/H1-hESC/MethCpG_rep2_filtered.bedMethyl'
    process_data_10_reads(input_file,output_file)
    






    
