#!/bin/bash
#SBATCH --job-name=dnase-10
#SBATCH --workdir="/oak/stanford/groups/akundaje/manyu/Misc_Scripts_genomics/DNAse_Arabidopsis_processing/dnase.10"
#SBATCH --output=dnase.10.out
#SBATCH --error=dnase.10.err
#SBATCH --time=2:00:00
#SBATCH -p akundaje,owners
#SBATCH --cpus-per-task=4
#SBATCH --mem=100000
sh ../peak_calls_1.sh /oak/stanford/groups/akundaje/manyu/DNAseSeq_data/2018-08-11-Arabidopsis-DNAse/03-Arabidopsis-DNAse-GSE53324/DS20201_SE_DNaseI-seq_seed_coat_cell_4DPA-GSM1289377
