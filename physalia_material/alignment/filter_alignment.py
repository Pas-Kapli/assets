#! /usr/bin/env python

from string import maketrans
import sys

f = open(sys.argv[1], "r")
f1 = open(str(sys.argv[1])+".clean", "w")

content = f.readlines()
new=[]
for i in range(len(content)):
	new.append(content[i].strip())

count = 0
temp_seq=''
taxa = []
seqs_original = []
for i in range(len(new)):
	if '>' in new[i][0]:
		taxa.append(new[i])
		if count>0:
			seqs_original.append(temp_seq)
			temp_seq=''
	else:
		temp_seq=temp_seq + new[i]
		count = count +1
seqs_original.append(temp_seq)


seqs_trans_orig = [''.join(s) for s in zip(*seqs_original)]

intab = "X"
outtab = "-"
trantab = maketrans(intab, outtab)

count1 = 0
count2 = 0
seqs_trans_new = []
for i in range(len(seqs_trans_orig)):
	tmp = seqs_trans_orig[i].translate(trantab)
	if tmp.count("-") >= len(taxa)- int(sys.argv[2]):
		count1 = count1 +1
	elif tmp.count("-") < len(taxa)-1:
		count2 = count2 +1
		seqs_trans_new.append(seqs_trans_orig[i])
	else:
		print "Warning: there is some error"

seqs_clean = [''.join(s) for s in zip(*seqs_trans_new)]

if len(seqs_clean) == len(taxa):
	for i in range(len(taxa)):
		f1.write(str(taxa[i]) + "\n")
		f1.write(str(seqs_clean[i]) + "\n")
else:
	print "Error: the number of taxa is not equal to the number of sequences"

print "The number of taxa in the alignment is: " + str(len(taxa))
print "The original alignment_length is: " + str(len(seqs_original[0]))
print "The filtered alignment length is: " + str(len(seqs_clean[0]))


f.close()
f1.close()
