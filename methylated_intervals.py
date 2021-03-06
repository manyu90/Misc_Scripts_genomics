from methylation_percentage import*
from collections import defaultdict

chip_seq_file='/mnt/lab_data/kundaje/manyu/ChipSeq/CEBPB_narrowPeak_peaks_mainChrom.bed'
with open(chip_seq_file,'r') as f:
    data=[tuple(line.strip().split('\t')) for line in f]

print(len(data))    

methylation_interval_dict=defaultdict(float)
for interval in data:
    #print(str(interval)+"done\n")
    region,start,end =interval[0],int(interval[1]),int(interval[2])
    methylation_interval_dict[interval]=methylation_percentage(region,start,end)

# import IPython
# IPython.embed()

#f=open('methylation_intervals_CEBPB.bed','w')
write_path='/srv/scratch/manyu/NIPS_workshop_tests/CEBPB_methylation_sorted'
f=open(write_path,'wb')
for key in methylation_interval_dict.keys():
	f.write(key[0]+'\t'+str(key[1])+'\t'+str(key[2])+'\t'+str(methylation_interval_dict[key][0]) \
		+'\t'+str(methylation_interval_dict[key][1])+'\t'+str(methylation_interval_dict[key][2])+'\n')

f.close()

#Then do this on the shell to sort based on the methylation levels
#sort -k 5 -r -t $'\t' methylation_intervals_NFATC3.bed >methylation_intervals_NFATC3_sorted.bed    