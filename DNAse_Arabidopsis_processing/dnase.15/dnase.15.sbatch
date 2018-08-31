#!/bin/bash
#SBATCH --job-name=dnase-15
#SBATCH --workdir="/oak/stanford/groups/akundaje/manyu/Misc_Scripts_genomics/DNAse_Arabidopsis_processing/dnase.15"
#SBATCH --output=dnase.15.out
#SBATCH --error=dnase.15.err
#SBATCH --time=2:00:00
#SBATCH -p akundaje,owners
#SBATCH --cpus-per-task=4
#SBATCH --mem=100000
sh ../peak_calls_1.sh /oak/stanford/groups/akundaje/manyu/DNAseSeq_data/2018-08-11-Arabidopsis-DNAse/03-Arabidopsis-DNAse-GSE53324/DS20427_DNaseI-seq_open_flowers-GSM1289380
