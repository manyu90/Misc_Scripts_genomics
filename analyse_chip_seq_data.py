#from methylation_percentage import*
from collections import defaultdict
import re
import gzip
import numpy as np
import pybedtools
from pysam import FastaFile
import pyBigWig
from genomedatalayer.util import nan_to_zero



##This class needs a chip seq file path as an input. and a write to path
##Calculates the methylation of GC dinucleotides within every chromosome and aggregates these statistics
##Generates a file where intervals have been sorted based on Methylation levels


class ChipSeq_file_methylation(object):
	def __init__(self,path,write_path):
		self.write_path=write_path
		self.path=path
		self.methylation_interval_dict=defaultdict(float)
		self.fasta_file=FastaFile('/mnt/data/annotations/by_organism/human/hg20.GRCh38/GRCh38.genome.fa')
		self.bw_filtered=pyBigWig.open('/mnt/lab_data/kundaje/manyu/Methylation_data/K562_wgbs_filtered.bigWig')

		try:
			if re.search('bed.gz', self.path):
				with gzip.open(path,'rb') as f:
					self.data_lines=[tuple(line.strip().split('\t')) for line in f]
			else:
				with open(path,'rb') as f:
					self.data_lines=[tuple(line.strip().split('\t')) for line in f]
		except Exception as e:
			print(e)
			self.data_lines=None

	#Looks at the sequence at tells you if there is a CpG dinucleotide at sequence[count]
	def find_CpG(self,sequence,count):
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

	#Calculates total CpG sites, and methylation percentage in the region specified
#CpG,Total Methylation/#CpG,Total Methylation/Total Sites  is returned

	def methylation_percentage(self,region,start,end):
	    fasta_file=self.fasta_file
	    bw_filtered=self.bw_filtered
	    sequence=fasta_file.fetch(region,start,end+1).lower()
	    #print(sequence)
	    count_gc=0.0
	    sum_gc=0.0
	    for count in xrange(len(sequence)):
	        if self.find_CpG(sequence,count):
	            count_gc+=1
	    data_methylation=bw_filtered.values(region,start,end+1,numpy=True)
	    nan_to_zero(data_methylation)
	    sum_gc=np.sum(data_methylation)
	    if count_gc>0:
	        # print("Returning total CpG,Fraction of methylated Cpg,Fraction of Methylated sites \n")
	        # print("#CpG,Total Methylation/#CpG,Total Methylation/Total Sites \n")
	        return count_gc,sum_gc/count_gc,sum_gc/len(sequence)
	    
	    else:
	        return 0,0.0,0.0


	

	def calculate_methylation(self):
		for interval in self.data_lines:
			region,start,end =interval[0],int(interval[1]),int(interval[2])
			self.methylation_interval_dict[interval]=self.methylation_percentage(region,start,end)
			#print "interval \t %s"%(str(interval))



					
	def write_to_file(self):
		self.calculate_methylation()  #Calculating meylation, populating the dictionary
		methylation_data_list=[]  #List version of the methylation_dict
		#print len(methylation_data_list)
		for key in self.methylation_interval_dict:
			data_=tuple(list(key)+list(self.methylation_interval_dict[key]))
			methylation_data_list.append(data_)
		methylation_data_list=sorted(methylation_data_list,key=lambda x: -1*x[4])
		with open(self.write_path,'wb') as f:
			for line in methylation_data_list:
				line_='\t'.join([str(elem) for elem in line])
				f.write(line_+'\n')
		f.close()
		print("Wrote to file %s \n"%(self.write_path) )


	


if __name__=='__main__':
	path='/srv/scratch/manyu/NIPS_workshop_tests/test.bed'
	#path='/mnt/lab_data/kundaje/manyu/ChipSeq/CEBPB_narrowPeak_peaks_mainChrom.bed'
	path_to_write='/srv/scratch/manyu/NIPS_workshop_tests/CEBPB_methylation_sorted_test'
	ChipSeq_file_methylation(path, path_to_write).write_to_file()
	



					
