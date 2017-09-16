import glob
import os
import gzip
from analyse_chip_seq_data import *
import re

if __name__=='__main__':
	path ='/srv/scratch/manyu/data/hg38/K562/'    #Path to all the data in K562
	data_list=[]
	for entry in glob.glob(path+'ENC*'):
    		data_list.append(entry)
    


   
	for entry in data_list:
		try:
			entry_name=entry.split('/')[-1]
			path_to_write='/srv/scratch/manyu/NIPS_workshop_tests/data_enrichment_analysis/%s'%(entry_name)
			if os.path.isfile(path_to_write):
				print("file %s exists . Continuing \n"%(entry_name))
				continue
			else:
				print "Trying %s"%(entry_name)
				
				for filename,sub,files in os.walk(entry):
					for file_ in files:
						file_=filename+'/'+file_   #Complete path of all files is captured this way
						if re.search('optimal',file_):
							ChipSeq_file_methylation(file_, path_to_write).write_to_file()
							print "Wrote \t %s to file \n" %(entry_name)


					
					
					
		except Exception as e:
			print e

				

    			

