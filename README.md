Various scripts which are useful for general purpose Genomics projects. For processing and cleaning differnet kinds of genomic data tracks.

analyse_chip_seq_data.py: Processes  an intervals file (in a bed format) and calculates methylation statistics for every CpG dinucleotide in every interval. It returns the interval along with total CpG sites, average methylation of CpG sites in the interval and the Average Methylation within the interval.
Writes to an output file (You need to provide a path to a chrom sizes file , a genome file FASTA and also a path to a methylation BigWig in the __init__() for the Class

