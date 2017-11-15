
# coding: utf-8

# In[5]:

import numpy as np
import pyximport
pyximport.install(pyimport = True)
from processing import process_function
import os
import json
path=os.getcwd()


# In[23]:

def create_labels_from_regions_and_labels(processed_file_name):
	f=open(processed_file_name,'r')
	data=[int(line.strip('\n').split('\t')[-1]) for line in f]
	data=np.array(data).reshape((len(data),1))
	labels_file_name=processed_file_name.strip('.bed')
    
	np.save(labels_file_name, data)
	print("Created labels file at %s "%(labels_file_name))

def create_filtered_intervals_file(CpG_offend_list,filename,new_file_name):
	try:
		os.system('bedtools intersect -v -a %s -b %s > %s'%(filename,CpG_offend_list,'./temp_intervals.bed'))
		os.system('shuf %s > %s'%('./temp_intervals.bed',new_file_name))
		os.system('rm %s'%('./temp_intervals.bed'))
		print("Created shuffled and filtered intervals file at %s" %new_file_name)
	except Exception as e:
		print(e)
		




# In[29]:

def read_json_regions_labels_file(json_file):
    with open(json_file,'r') as f:
        json_dict=json.load(f)
        regions=json_dict['K562']['regions'].encode('utf-8')
        labels=json_dict['K562']['labels'].encode('utf-8')
        # import IPython
        # IPython.embed()
        # try:
        #     regions=json_dict['K562']['regions'].encode('utf-8')
        #     labels=json_dict['K562']['labels'].encode('utf-8')
        # except:
        #     regions=json_dict['K562']['regions']
        #     labels=json_dict['K562']['labels']
    return regions,labels




# In[7]:

##Provide the complete path to the regions and labels file
def create_json_file_regions_labels(regions,labels):
    path=os.getcwd()
    task_name=regions.split('/')[-1].split('_')[0]
    dict_return={}
    dict_return["K562"]={"regions":regions,"labels":labels}
    dict_return["task_names"]=[task_name]
    json_file_name='%s'%(regions.strip('.bed')+'.json')
    with open(json_file_name,'wb') as f:
        json.dump(dict_return,f)
    print("Created JSON file for regions, labels at %s" %(json_file_name))
    
    


# In[30]:

def run_filtering_pipeline(regions_json_file,CpG_offend_list):
    path=os.getcwd()
    regions,labels=read_json_regions_labels_file(regions_json_file)
    print(type(regions))
    TF_name_id='_'.join(regions.split('/')[-1].split('_')[0:2])
    print("Processing the TF: %s \n"%(TF_name_id))
    TF_name=TF_name_id.split('_')[0]
    unfiltered_file_name='%s/%s'%(path,'temp_regions_labels.bed')
    process_function(regions,labels,unfiltered_file_name)
    filtered_shuf_file='%s/%s_filter_shuf_regions_labels.bed'%(path,TF_name_id)
    ##Create filtered and shuffled intervals file
    create_filtered_intervals_file(CpG_offend_list, unfiltered_file_name, filtered_shuf_file)
    os.system('rm %s'%(unfiltered_file_name))
    ##Create np labels file from it
    create_labels_from_regions_and_labels(filtered_shuf_file)
    ##Create JSON file with shuffled regions and labels
    create_json_file_regions_labels(filtered_shuf_file,filtered_shuf_file.strip('.bed')+'.npy')
    
    
      


# In[31]:

if __name__=='__main__':
    import glob
    CpG_offend_list='./offending_CpGs_10reads.bed'
    for file_ in glob.glob('/srv/scratch/manyu/NIPS_workshop_tests/train_models/label_regions/*stride200.json'):
        path_to_json=file_
        run_filtering_pipeline(path_to_json,CpG_offend_list)
        
        


# In[32]:



# In[ ]:



