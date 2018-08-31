#!/bin/bash
#SBATCH --job-name=dnase-8
#SBATCH --workdir="/oak/stanford/groups/akundaje/manyu/Misc_Scripts_genomics/DNAse_Arabidopsis_processing/dnase.8"
#SBATCH --output=dnase.8.out
#SBATCH --error=dnase.8.err
#SBATCH --time=2:00:00
#SBATCH -p akundaje,owners
#SBATCH --cpus-per-task=4
#SBATCH --mem=100000
sh ../peak_calls_1.sh /oak/stanford/groups/akundaje/manyu/DNAseSeq_data/2018-08-11-Arabidopsis-DNAse/03-Arabidopsis-DNAse-GSE53324/DS21306_DNaseI-seq_seed_coat_cell_7DPA-GSM1289379
