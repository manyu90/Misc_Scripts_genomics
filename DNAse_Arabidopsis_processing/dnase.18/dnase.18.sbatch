#!/bin/bash
#SBATCH --job-name=dnase-18
#SBATCH --workdir="/oak/stanford/groups/akundaje/manyu/Misc_Scripts_genomics/DNAse_Arabidopsis_processing/dnase.18"
#SBATCH --output=dnase.18.out
#SBATCH --error=dnase.18.err
#SBATCH --time=2:00:00
#SBATCH -p akundaje,owners
#SBATCH --cpus-per-task=4
#SBATCH --mem=100000
sh ../peak_calls_2.sh /oak/stanford/groups/akundaje/manyu/DNAseSeq_data/2018-08-11-Arabidopsis-DNAse/01-Arabidopsis-DNAse-GSE53322/DS20968_PE_DNaseI-seq_7_day_old_seedling_Dark_24hr-GSM1289351
