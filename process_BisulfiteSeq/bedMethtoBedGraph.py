import glob
import subprocess
import sys
import os
import glob
import re
#Converts a .bedMethyl file to a bedgraph and bigwig. 
#Expects as input a .bedMethyl format file
class bedMeth_bigWig(object):
    def __init__(self,BedMeth_filename):
        self.bedMeth=BedMeth_filename
        name=self.bedMeth.split('.')[0]
        self.bedgraph=name+'.bedGraph'
        self.bigwig=name+'.bigWig'
        #print(name,self.bedgraph)

    def bedMeth_to_bedGraph(self):
        if os.path.isfile(self.bedgraph):
            print('%s exists'%self.bedgraph)
            return
        g=open(self.bedgraph,'w')
        with open(self.bedMeth,'r') as f:
            for line in f:
                line=line.split('\t')
                g.write('\t'.join(line[0:3])+'\t'+line[-1])
        g.close()
        print('Wrote to %s'%self.bedgraph) 

    
    def bedGraph_to_bigWig(self):
        # with open('./shell_script.sh','w') as f:
        #     #os.system('module load ucsc_tools/3.0.9 ')
        #     os.system('bedGraphToBigWig %s /mnt/data/annotations/by_organism/human/hg20.GRCh38/hg38.chrom.sizes %s \n'%(self.bedgraph,self.bigwig))

        print("Created shell script \n")
        # os.system('. ./shell_script.sh')
        # #subprocess.call(['bash', 'shell_script.sh'])
        print("Wrote to %s"%(self.bigwig))  






if __name__=='__main__':
    # a=bedMeth_bigWig('/mnt/lab_data/kundaje/manyu/Methylation_data/K562_wgbs_filtered.bedMethyl')
    # a.bedGraph_to_bigWig()
    for filename,sub,files in os.walk('/srv/scratch/manyu/Methylation_data'):
        for file_ in files:
            if re.search('.bedMethyl$',file_):
                file_=filename+'/'+file_
                print("Trying %s \n"%file_)
                bedMeth_bigWig(file_).bedMeth_to_bedGraph()








            















