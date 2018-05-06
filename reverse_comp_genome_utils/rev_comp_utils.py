#Creates a reverse complemented version of the genome. 
#Reads the bcolz file for the mapped genome and reverse complements it


from genomelake.backend import load_directory, _array_writer
import numpy as np
import os
import json


def create_rev_com_genome(source_genome_path,write_dir):
    source_genome_path=source_genome_path.rstrip('/')
    genome_name=source_genome_path.split('/')[-1]
    write_dir=os.path.join(write_dir,genome_name)
    if not os.path.exists(write_dir):
        os.mkdir(write_dir)
    source_genome_dict=load_directory(source_genome_path,in_memory=True)
    file_shapes={}    
    for key in source_genome_dict.keys():
        data_arr=source_genome_dict[key].__dict__['_arr'][:].transpose()
        ##Reverse complement by taking base pair complements as well as reversing

        rev_comp_data_arr=data_arr[::-1,::-1]   #Reverse complement the entrire chromosome
        _array_writer['bcolz'](rev_comp_data_arr.astype(np.float32), os.path.join(write_dir,key))
        file_shapes[key]=rev_comp_data_arr.shape
        print("Created chromosome %s \n"%(key))
        
    
    
    ##Write the metadata.json file::

    print("Writing metadata file \n")
    with open(os.path.join(write_dir,'metadata.json'), 'w') as fp:
        json.dump({'file_shapes': file_shapes,
                   'type': 'array_{}'.format('bcolz'),
                   'source': source_genome_path}, fp)

    

def create_complemented_genome(source_genome_path,write_dir):
    """
        Does not reverse. Only takes complements

    """
    source_genome_path=source_genome_path.rstrip('/')
    source_genome_dict=load_directory(source_genome_path,in_memory=True)
    genome_name=source_genome_path.split('/')[-1]
    write_dir=os.path.join(write_dir,genome_name)
    if not os.path.exists(write_dir):
        os.mkdir(write_dir)
    
    file_shapes={}    
    for key in source_genome_dict.keys():
        data_arr=source_genome_dict[key].__dict__['_arr'][:].transpose()

        ##Take the complement by just flipping bases
        ##The shape is now (4,N)
        rev_comp_data_arr=data_arr[::-1]   
        _array_writer['bcolz'](rev_comp_data_arr.astype(np.float32), os.path.join(write_dir,key))
        file_shapes[key]=rev_comp_data_arr.shape
        print("Created chromosome %s \n"%(key))
        
    
    print("Writing metadata file \n")
    ##Write the metadata.json file::
    with open(os.path.join(write_dir,'metadata.json'), 'w') as fp:
        json.dump({'file_shapes': file_shapes,
                   'type': 'array_{}'.format('bcolz'),
                   'source': source_genome_path}, fp)




if __name__=='__main__':
	write_path='/srv/scratch/manyu/memmap_bcolz/BP_complemented_genomes'
	source_genome_path='/srv/scratch/manyu/memmap_bcolz/GRCh38.genome.fa'
	create_complemented_genome(source_genome_path,write_path)



  
