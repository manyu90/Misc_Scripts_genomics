#!/bin/bash
#SBATCH --job-name=dnase-13
#SBATCH --workdir="/oak/stanford/groups/akundaje/manyu/Misc_Scripts_genomics/DNAse_Arabidopsis_processing/dnase.13"
#SBATCH --output=dnase.13.out
#SBATCH --error=dnase.13.err
#SBATCH --time=2:00:00
#SBATCH -p akundaje,owners
#SBATCH --cpus-per-task=4
#SBATCH --mem=100000
sh ../peak_calls_1.sh /oak/stanford/groups/akundaje/manyu/DNAseSeq_data/2018-08-11-Arabidopsis-DNAse/03-Arabidopsis-DNAse-GSE53324/DS20201_PE_DNaseI-seq_seed_coat_cell_4DPA-GSM1289378
