##################################
#                                #
# Last modified 2018/04/14       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import string
import os

def run():

    if len(sys.argv) < 6:
        print 'usage: python %s <commands list file> CPUs memory walltime queue prefix [-gpu] [-srun]' % sys.argv[0]
        sys.exit(1)

# sacct -l

    input = sys.argv[1]
    CPUs = sys.argv[2]
    mem = sys.argv[3]
    walltime = sys.argv[4]
    queue = sys.argv[5]
    prefix = sys.argv[6]

    doGPU = False
    if '-gpu' in sys.argv:
        doGPU = True

    doSR = False
    if '-srun' in sys.argv:
        doSR = True

    linelist = open(input)
    i=0
    for line in linelist:
        if line.strip() == '':
            continue
        i+=1
        outfilename = prefix + '.' + str(i) + '.sbatch'
        outfile = open(outfilename,'w')
        outfile.write('#!/bin/bash' + '\n')
        outfile.write('#SBATCH --job-name=' + prefix + '-' + str(i) + '\n')
        outfile.write('#SBATCH --output=' + prefix + '.' + str(i) + '.out' '\n')
        outfile.write('#SBATCH --error=' + prefix + '.' + str(i) + '.err' '\n')
        outfile.write('#SBATCH --time=' + walltime + '\n')
        outfile.write('#SBATCH -p ' + queue + '\n')
        outfile.write('#SBATCH --cpus-per-task=' + CPUs + '\n')
        outfile.write('#SBATCH --mem=' + mem + '\n')
        if doGPU:
            outfile.write('#SBATCH --gres gpu:1' + '\n')
        outfile.write('echo "Copying Genome Files" \n')
        outfile.write('cp -r /oak/stanford/groups/akundaje/manyu/memmap_bcolz/GRCh38.genome.fa/ $L_SCRATCH/ \n')
        outfile.write('echo "Copied Genome Files" \n')
        
        if doSR:
            if line.strip().endswith ('&'):
                outfile.write('srun ' + line.strip()[0:-1] + '\n')
            else:
                outfile.write('srun ' + line.strip() + '\n')
        else:
            if line.strip().endswith ('&'):
                outfile.write(line.strip()[0:-1] + '\n')
            else:
                outfile.write(line.strip() + '\n')
#        if line.strip().endswith ('&'):
#            outfile.write(line.strip()[0:-1] + '\n')
#        else:
#            outfile.write(line.strip() + '\n')
        outfile.close()
        cmd = 'sbatch ' + prefix + '.' + str(i) + '.sbatch'
        print cmd
        os.system(cmd)

run()

