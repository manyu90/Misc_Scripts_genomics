'''
Parses a TF-dragonn metrics file 
'''



import os
import re

class parse_metrics(object):
    def __init__(self,metrics_file):
        assert os.path.exists(metrics_file)
        self.filename = metrics_file
        with open(self.filename,'r') as f:
            self.file = f.readlines()
        self.total_pos_and_neg()    
        self.metrics_dict = {}  
        n=1
        while(self.extract_metrics_of_epoch(n)):
            print("Parsing Epoch: {}".format(n))
            self.metrics_dict[n] = self.parse_metrics_of_epoch(n)
            n+=1
        self.best_epoch = self.extract_best_epoch()    
            
    
    def extract_best_epoch(self):
        last_line  = self.file[-1]
        match = re.search('from epoch [0-9]+',last_line)
        if match:
            match = match.group()
        else:
            return("Model has not finished training/trained")
        best_epoch = int(match.lstrip('from epoch'))
        return best_epoch
    
    def extract_metrics_of_epoch(self,n):
        for i,line in enumerate(self.file):
            match = re.search('Epoch {}:'.format(str(n)),line)
            if match:
                break
        if i==(len(self.file)-1):   #Went to the end of the file with no matches found
            print("No match found for Epoch: {} \n".format(n))
            return
        else:
            return self.file[i:i+4]     
             
    def parse_metrics_of_epoch(self,n):
        metrics_dict = {}
        if n in self.metrics_dict:
            return self.metrics_dict[n]
        
        
        metrics = self.extract_metrics_of_epoch(n)
        if metrics:
            metrics_dict['Epoch'] = n
            line3 = metrics[2]
            metrics_dict['auroc'] = float(line3.split('\t')[1].lstrip('auROC:'))
            metrics_dict['auprc'] = float(line3.split('\t')[2].strip().lstrip('auPRC:'))
            line4 = metrics[3]
            match = re.search('FDR: [0-9.% | ]+',line4).group()
            match = match.lstrip('FDR:').split('|')
            recall_vals = [float(_.strip().rstrip('%')) for _ in match]
            metrics_dict['recall_5'] = recall_vals[0]
            metrics_dict['recall_10'] = recall_vals[1]
            metrics_dict['recall_25'] = recall_vals[2]
            metrics_dict['recall_50'] = recall_vals[3]
            return metrics_dict
            
        
        return 
    
    def total_pos_and_neg(self):
        metrics = self.extract_metrics_of_epoch(1)
        pos,neg = re.search('Num Positives: [0-9]+',metrics[-1]).group(),        re.search('Num Negatives: [0-9]+',metrics[-1]).group()
        pos = int(pos.split(':')[-1])
        neg = int(neg.split(':')[-1])
        self.pos = pos
        self.neg = neg
        

