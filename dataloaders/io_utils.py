from profilehooks import profile
from itertools import cycle,izip
import numpy as np


def batch_iterator(iterable,batch_size=128):
    it=iter(iterable)
    try:
        while True:
            batch=[]
            for i in xrange(batch_size):
                batch.append(next(it))
            yield batch
    except StopIteration:
        yield batch
        

def infinite_batch_iter(iterable, batch_size=128):
    '''iterates in batches indefinitely.
    '''
    return batch_iterator(cycle(iterable),
                      batch_size)

        




def generate_from_intervals(intervals, data_extractors_dict, batch_size=128, indefinitely=True):
    """
    Generates signals extracted on interval batches.
    Parameters
    ----------
    intervals : Intervals BedTool (pybedtools list of intervals)
    data_extractor_dict : dict of data source, and corresponding Genomelake Array Extractor
    batch_size : int, optional
    indefinitely : bool, default: True
    """
    shapes_dict={
    "data/genome_data_dir":(batch_size,1000,4),
    "data/dnase_data_dir":(batch_size,1000,1),
    "data/methylation_data_dir":(batch_size,1000,1)}
    
    if indefinitely:
        batch_iterator_generator = infinite_batch_iter(intervals, batch_size)
    else:
        batch_iterator_generator = batch_iterator(intervals, batch_size)
    
    
    
    
    ##Pre allocate memory for the data dictionary
    data_dict={}
    for key in data_extractors_dict:
        assert key in shapes_dict.keys()
        data_dict[key]=np.zeros(shapes_dict[key])
        
        
            
    for batch in batch_iterator_generator:
        try:
            for key in data_extractors_dict:
                data_dict[key][:]=data_extractors_dict[key](batch).reshape(shapes_dict[key])
            yield data_dict    
                
            
        except ValueError:
            for key in data_extractors_dict:
                # import  IPython
                # IPython.embed()
                data=data_extractors_dict[key](batch)
                #print (key,data.shape)

                data_dict[key] = data_extractors_dict[key](batch).reshape((data.shape[0],shapes_dict[key][1],shapes_dict[key][2]))
            yield data_dict    




def test_extractor_in_generator(intervals, extractor_dict, batch_size=128):
    """
    Extracts data in bulk, then in streaming batches and checks its the same data.
    """
    from keras.utils.generic_utils import Progbar

    X_in_memory = extractor_dict['data/genome_data_dir'](intervals)
    Y_in_memory = extractor_dict['data/dnase_data_dir'](intervals).reshape((len(intervals),1000,1))
    samples_per_epoch = len(intervals)
    batches_per_epoch = int(samples_per_epoch / batch_size) + 1
    
    batch_generator = generate_from_intervals(
        intervals, extractor_dict, batch_size=batch_size, indefinitely=False)
    progbar = Progbar(target=samples_per_epoch)
    for batch_indx in xrange(1, batches_per_epoch + 1):
        next_batch = next(batch_generator)
        x_next_batch=next_batch['data/genome_data_dir']
        y_next_batch=next_batch['data/dnase_data_dir']
        print (x_next_batch.shape,y_next_batch.shape)
        start = (batch_indx - 1) * batch_size
        stop = batch_indx * batch_size
        if stop > samples_per_epoch:
            stop = samples_per_epoch
        # assert streamed sequences and labels match data in memory
        assert (X_in_memory[start:stop] - x_next_batch).sum() == 0
        assert (Y_in_memory[start:stop] - y_next_batch).sum()==0
        progbar.update(stop)



def generate_from_array(array, batch_size=128, indefinitely=True):
    """
    Generates the array in batches.
    """
    if indefinitely:
        batch_iterator_generator = infinite_batch_iter(array, batch_size)
    else:
        batch_iterator_generator = batch_iterator(array, batch_size)
    for array_batch in batch_iterator_generator:
        yield np.stack(array_batch, axis=0)





def get_fixed_number_of_intervals(intervals_bedtool,num_batches,batch_procesing_size):
    
    total_processed_batches=0
    return_list=[]
    
    for batch in batch_iterator(intervals_bedtool,batch_procesing_size):
        return_list.append(copy.deepcopy(batch))
        total_processed_batches+=1
        if total_processed_batches==num_batches:
            break
    return return_list        
    
    #Vstack all the elements of the list
    features_tensor=np.vstack(features_list)
    np.save(file=save_file_path,arr=features_tensor)
    print("Saved features file to %s \n"%(save_file_path))



def generate_from_intervals_and_labels(intervals,labels,data_extractors_dict, batch_size=128, indefinitely=True):
    """
    intervals: BedTool list of a set of genomic intervals 
    labels: np.array
    data_extractors_dict: dict of data type to genomelake extractor object for that kind of data 
    for example: {'data/genome_data_dir':ArrayExtractor(genome_path)}

    Generates batches of (inputs, labels) where inputs is a list of numpy arrays based on provided extractors.
    """
    batch_generator = izip(generate_from_intervals(intervals,data_extractors_dict,
                                                  batch_size=batch_size,
                                                  indefinitely=indefinitely),
                          generate_from_array(labels, batch_size=batch_size, indefinitely=indefinitely))
    for batch in batch_generator:
        yield batch    
