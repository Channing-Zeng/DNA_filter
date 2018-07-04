#!/usr/bin/python

f1=open('D:/fasta1.txt','w')
with open('D:/1.fastq','r') as f2:
    for line in f2:
        if '@' in line:
            f1.write('>'+line.strip('@'))
            f1.write(next(f2))
        else:
            (next(f2))
    f2.close()
