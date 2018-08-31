#!/bin/bash
#SBATCH --job-name=dnase-12
#SBATCH --workdir="/oak/stanford/groups/akundaje/manyu/Misc_Scripts_genomics/DNAse_Arabidopsis_processing/dnase.12"
#SBATCH --output=dnase.12.out
#SBATCH --error=dnase.12.err
#SBATCH --time=2:00:00
#SBATCH -p akundaje,owners
#SBATCH --cpus-per-task=4
#SBATCH --mem=100000
sh ../peak_calls_1.sh /oak/stanford/groups/akundaje/manyu/DNAseSeq_data/2018-08-11-Arabidopsis-DNAse/03-Arabidopsis-DNAse-GSE53324/DS16398_DNaseI-seq_root_non_hair_cell_10_day-GSM1289375
