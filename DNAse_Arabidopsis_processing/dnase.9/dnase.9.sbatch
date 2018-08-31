#!/bin/bash
#SBATCH --job-name=dnase-9
#SBATCH --workdir="/oak/stanford/groups/akundaje/manyu/Misc_Scripts_genomics/DNAse_Arabidopsis_processing/dnase.9"
#SBATCH --output=dnase.9.out
#SBATCH --error=dnase.9.err
#SBATCH --time=2:00:00
#SBATCH -p akundaje,owners
#SBATCH --cpus-per-task=4
#SBATCH --mem=100000
sh ../peak_calls_1.sh /oak/stanford/groups/akundaje/manyu/DNAseSeq_data/2018-08-11-Arabidopsis-DNAse/03-Arabidopsis-DNAse-GSE53324/DS21513_DNaseI-seq_root_hair_cell_7_day-GSM1289376
