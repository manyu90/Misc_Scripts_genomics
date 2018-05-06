#!/bin/sh
zcat ABI3VP1_tnt.AT5G60130_col_a/SRR2926075_1.fastq.gz|python /oak/stanford/groups/akundaje/marinovg/code/trimfastq.py - 50 -stdout | /oak/stanford/groups/akundaje/marinovg/programs/bowtie-1.0.1+hamrhein_nh_patch/bowtie /oak/stanford/groups/akundaje/marinovg/genomes/TAIR10/bowtie-indexes/TAIR10 -p 8 -v 2 --k 2 -m 1 -t --best --strata -q --sam-nh --sam - | /oak/stanford/groups/akundaje/marinovg/programs/samtools-0.1.18/samtools view -bT /oak/stanford/groups/akundaje/marinovg/genomes/TAIR10/bowtie-indexes/TAIR10.fa - | /oak/stanford/groups/akundaje/marinovg/programs/samtools-0.1.18/samtools sort - ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.with_organelles
echo "Finished mapping ABI3VP1_tnt.AT5G60130_col_a"

samtools index ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.with_organelles.bam
echo "Finished indexing"

samtools view ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.with_organelles.bam | egrep -v 'chloroplast|chrM' | /oak/stanford/groups/akundaje/marinovg/programs/samtools-0.1.18/samtools view -bT /oak/stanford/groups/akundaje/marinovg/genomes/TAIR10/bowtie-indexes/TAIR10.fa - | /oak/stanford/groups/akundaje/marinovg/programs/samtools-0.1.18/samtools sort - ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique

echo "Finished removing organelles"

samtools index ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.bam

echo "Finished re-indexing"
echo "Running  SPP"
Rscript /oak/stanford/groups/akundaje/marinovg/code/spp/spp_package/run_spp.R -c=ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.bam -p=8 -savp -rf -s=-0:2:400 -out=ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.QC

echo "Finished running SPP"

echo "Make coverage tracks"
python /oak/stanford/groups/akundaje/marinovg/code/makewigglefromBAM-NH.py ==== ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.bam /oak/stanford/groups/akundaje/marinovg/genomes/TAIR10/TAIR10.chrom.sizes ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.wig -notitle -uniqueBAM -RPM
echo "Finished making coverage tracks"

echo "making stranded coverage tracks"

python /oak/stanford/groups/akundaje/marinovg/code/makewigglefromBAM-NH.py ==== ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.bam /oak/stanford/groups/akundaje/marinovg/genomes/TAIR10/TAIR10.chrom.sizes ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.minus.wig -notitle -uniqueBAM -RPM -stranded -

python /oak/stanford/groups/akundaje/marinovg/code/makewigglefromBAM-NH.py ==== ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.bam /oak/stanford/groups/akundaje/marinovg/genomes/TAIR10/TAIR10.chrom.sizes ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.plus.wig -notitle -uniqueBAM -RPM -stranded +

echo "Finished producing stranded coverage tracks"

echo "Step6: Make pseudoreps"
python /oak/stanford/groups/akundaje/marinovg/code/BAMPseudoReps.py   ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.bam
echo "Made pseudoreps"

echo "Step 7: SPP peak calling step"
mkdir ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique-SPP-300K
mkdir ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.pseudoRep1-SPP-300K
mkdir ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.pseudoRep2-SPP-300K 

Rscript /oak/stanford/groups/akundaje/marinovg/code/spp/spp_package/run_spp.R -c=ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.bam -i=control_none.beads_col_v3a-GSM1924998.50mers.TAIR10.unique.removed_organelles.bam  -odir=ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique-SPP-300K -p=8 -npeak=300000 -savr -savn -rf 

Rscript /oak/stanford/groups/akundaje/marinovg/code/spp/spp_package/run_spp.R -c=ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.pseudoRep1.bam -i=control_none.beads_col_v3a-GSM1924998.50mers.TAIR10.unique.removed_organelles.pseudoRep1.bam  -odir=ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.pseudoRep1-SPP-300K -p=8 -npeak=300000 -savr -savn -rf 

Rscript /oak/stanford/groups/akundaje/marinovg/code/spp/spp_package/run_spp.R -c=ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.pseudoRep2.bam -i=control_none.beads_col_v3a-GSM1924998.50mers.TAIR10.unique.removed_organelles.pseudoRep2.bam  -odir=ABI3VP1_tnt.AT5G60130_col_a.50mers.TAIR10.unique.pseudoRep2-SPP-300K -p=8 -npeak=300000 -savr -savn -rf 

echo "Finished peak calling step"


echo "Do IDR after the peaks have been called"

















