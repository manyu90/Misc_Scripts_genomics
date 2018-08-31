#!/bin/sh
#Usage: sh peak_calls.sh path_to_BAM


#peak calls with macs2 done in the py27 environment
PREFIX=$1
BAM_FILE=$PREFIX/all.2x36mers.unique.bam
pr1=$PREFIX/all.2x36mers.unique.pseudoRep1.bam
pr2=$PREFIX/all.2x36mers.unique.pseudoRep2.bam
macs_pr1_peaks=$PREFIX/macs.pr1
macs_pr2_peaks=$PREFIX/macs.pr2
macs_idr=$PREFIX/IDR_peaks
macs_output=$PREFIX/macs2.IDR_1e-1.narrowpeak.gz

echo 
source activate aquas_chipseq
echo "Activated environment"

echo "Step1: Make pseudoreps"
python /oak/stanford/groups/akundaje/marinovg/code/BAMPseudoReps.py $BAM_FILE 
echo "Made pseudoreps"
source deactivate

echo "Step2: Call peaks"

source activate py27
echo "Calling peaks pseudorep1"
macs2 callpeak -t $pr1 -f BAM -n $macs_pr1_peaks  -g hs -p 0.01 --nomodel --shift -75 --extsize 150 -B --SPMR --keep-dup all --call-summits

echo "Calling peaks pseudorep2"
macs2 callpeak -t $pr2 -f BAM -n $macs_pr2_peaks  -g hs -p 0.01 --nomodel --shift -75 --extsize 150 -B --SPMR --keep-dup all --call-summits

echo "Finished calling peaks on both the pseudoreps"

source deactivate

echo "Step 3: IDR"
#Soft idr thresholds of 0.1 chosen for DNAse/ATAC. ChipSeq uses .05
#Use aquas_chipseq_py3 environment for doing the IDR analysis


macs_pr1_peaks_input=$PREFIX/macs.pr1_peaks.narrowPeak
macs_pr2_peaks_input=$PREFIX/macs.pr2_peaks.narrowPeak

source activate aquas_chipseq_py3
echo "starting idr"
/oak/stanford/groups/akundaje/marinovg/programs/idr-2.0.4/bin/idr \
	--samples $macs_pr1_peaks_input $macs_pr2_peaks_input \
	--input-file-type narrowPeak \
	--output-file $macs_idr \
	--rank signal.value \
	--soft-idr-threshold 0.1 \
	--plot \
	--use-best-multisummit-IDR

echo "Done idr"
echo "starting thresholds"

idr_thresh_transformed=$(awk -v p=0.1 'BEGIN{print -log(p)/log(10)}')
awk 'BEGIN{OFS="\t"} $12>='"${idr_thresh_transformed}"' {if ($2<0) $2=0; print $1,$2,$3,$4,$5,$6,$7,$8,$9,$10}' $macs_idr| sort | uniq | sort -k7n,7n | gzip -nc > $macs_output
echo "done threholds"

source deactivate
