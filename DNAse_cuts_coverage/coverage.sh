#!/bin/sh
python /oak/stanford/groups/akundaje/marinovg/code/makewigglefromBAM-NH.py ==== rep1+rep2_copy.bam /oak/stanford/groups/akundaje/marinovg/genomes/hg20/hg38.chrom.sizes GM12878-DNAse_coverage_new.wig -notitle -uniqueBAM -RPM
echo "Finished generating coverage track"

