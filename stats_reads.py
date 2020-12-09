#! uss/bin/env python
"""
Calculate the metrics of .fastq files in batch mode
using one text file as following:

#Sample	PATH_FW_reads	PATH_RV_reads

"""
import os
import sys
from Bio import SeqIO

dict_stats = {}

def stats_reads(fw, rv):
	quality = []
	n_reads = 0


with open(sys.argv[1], "r") as infile:

	for line in infile:

		if line.startswith("#"):
			pass
		else:
			quality = []
			n_reads = 0
			n_bases = 0

			code = os.path.join(line.strip().split("\t")[0])
			fw = os.path.join(line.strip().split("\t")[1])
			rv = os.path.join(line.strip().split("\t")[2])

			for seq in [fw, rv]:
				print(seq)
				for record in SeqIO.parse(seq, "fastq"):
					n_reads = n_reads + 1
					n_bases = n_bases + len(record.letter_annotations["phred_quality"])
					quality.append( sum(record.letter_annotations["phred_quality"])/ len(record.letter_annotations["phred_quality"]) )
				Q = round( sum(quality)/len(quality), 2)
				#print(n_reads, n_bases, Q )
				dict_stats[code] = [n_reads, n_bases, Q]
print(dict_stats)
