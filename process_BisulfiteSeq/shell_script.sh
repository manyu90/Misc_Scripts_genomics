module load ucsc_tools/3.0.9

name=0
for file in $(find /srv/scratch/manyu/Methylation_data/|grep 'bedGraph')
do 
    name=$(echo $file|cut -d '.' -f1)
    bedGraphToBigWig $file /mnt/data/annotations/by_organism/human/hg20.GRCh38/hg38.chrom.sizes $name.bigWig
    echo '$file has been converted'
done
