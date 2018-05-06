#!/bin/sh
samtools merge -f rep1+rep2.bam ENCFF308HYA_sort.bam ENCFF603PGI_sort.bam
echo "finished merging bam files"
samtools index rep1+rep2.bam
echo "finished indexing bam file"
python /oak/stanford/groups/akundaje/marinovg/code/make5primeWigglefromBAM-NH.py ==== rep1+rep2.bam /oak/stanford/groups/akundaje/marinovg/genomes/hg20/hg38.chrom.sizes GM12878-DNAse_cuts.wig -notitle -uniqueBAM -RPM
echo "Finished processsing BAM to get cuts"

