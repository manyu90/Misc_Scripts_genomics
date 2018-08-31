#!/bin/bash
#SBATCH --job-name=dnase-14
#SBATCH --workdir="/oak/stanford/groups/akundaje/manyu/Misc_Scripts_genomics/DNAse_Arabidopsis_processing/dnase.14"
#SBATCH --output=dnase.14.out
#SBATCH --error=dnase.14.err
#SBATCH --time=2:00:00
#SBATCH -p akundaje,owners
#SBATCH --cpus-per-task=4
#SBATCH --mem=100000
sh ../peak_calls_1.sh /oak/stanford/groups/akundaje/manyu/DNAseSeq_data/2018-08-11-Arabidopsis-DNAse/03-Arabidopsis-DNAse-GSE53324/DS21511_DNaseI-seq_whole_root_7_day-GSM1289374
