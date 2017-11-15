import numpy as np
cimport numpy as np

def process_function(str intervals_file,str labels_file,str processed_file_name):
	cdef np.ndarray[np.int_t, ndim=2] labels=np.load(labels_file)
	cdef int length=labels.shape[0]
	cdef np.ndarray[np.int_t,ndim=1] labels_reshape=np.reshape(labels,(length,))
	cdef int ctr=0
	g=open(processed_file_name,'w')
	with open(intervals_file,'r') as f:
		for line in f:
			g.write('\t'.join(line.split('\t')[:3])+'\t'+str(labels_reshape[ctr])+'\n')
			ctr+=1

	g.close()
