#!/bin/bash
#SBATCH --job-name=dnase-20
#SBATCH --workdir="/oak/stanford/groups/akundaje/manyu/Misc_Scripts_genomics/DNAse_Arabidopsis_processing/dnase.20"
#SBATCH --output=dnase.20.out
#SBATCH --error=dnase.20.err
#SBATCH --time=2:00:00
#SBATCH -p akundaje,owners
#SBATCH --cpus-per-task=4
#SBATCH --mem=100000
sh ../peak_calls_2.sh /oak/stanford/groups/akundaje/manyu/DNAseSeq_data/2018-08-11-Arabidopsis-DNAse/01-Arabidopsis-DNAse-GSE53322/DS20423_PE_DNaseI-seq_7_day_old_seedling_Heat_Shock-GSM1289361
