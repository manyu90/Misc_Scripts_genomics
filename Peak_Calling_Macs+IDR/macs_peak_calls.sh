#!/bin/sh
#p=.01 is a relaxed threshold for peak calling for DNAse. We do this and keep top 300K peaks based on p value. 
#use the py27 environment to calls peaks with MACS2

echo "Calling peaks on rep1"
macs2 callpeak -t ENCFF308HYA_sort.bam -f BAM -n macs.ENCFF308HYA.rep1 -g hs -p 0.01 --nomodel --shift -75 --extsize 150 -B --SPMR --keep-dup all --call-summits
echo "Calling peaks on rep2"
macs2 callpeak -t ENCFF603PGI_sort.bam -f BAM -n macs.ENCFF603PGI.rep2 -g hs -p 0.01 --nomodel --shift -75 --extsize 150 -B --SPMR --keep-dup all --call-summits


