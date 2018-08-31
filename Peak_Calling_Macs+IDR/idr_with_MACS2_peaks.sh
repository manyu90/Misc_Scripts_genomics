#!/bin/sh
#Soft idr thresholds of 0.1 chosen for DNAse/ATAC. ChipSeq uses .05
#Use aquas_chipseq_py3 environment for doing the IDR analysis

echo "starting idr"
/oak/stanford/groups/akundaje/marinovg/programs/idr-2.0.4/bin/idr --samples macs.ENCFF308HYA.rep1_peaks.narrowPeak macs.ENCFF603PGI.rep2_peaks.narrowPeak --input-file-type narrowPeak --output-file IDR-GM12878.macs2 --rank signal.value --soft-idr-threshold 0.1 --plot --use-best-multisummit-IDR
#echo "Done idr"
echo "starting thresholds"

idr_thresh_transformed=$(awk -v p=0.1 'BEGIN{print -log(p)/log(10)}')
awk 'BEGIN{OFS="\t"} $12>='"${idr_thresh_transformed}"' {if ($2<0) $2=0; print $1,$2,$3,$4,$5,$6,$7,$8,$9,$10}' IDR-GM12878.macs2| sort | uniq | sort -k7n,7n | gzip -nc > IDR-GM12878.macs2.IDR_1e-1.narrowPeak.gz

echo "done threholds"
