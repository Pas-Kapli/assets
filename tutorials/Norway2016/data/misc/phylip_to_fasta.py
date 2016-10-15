#! /usr/bin/env python
'''
to run:
$./phylip_to_fasta file.phy

'''
import sys
f = open(sys.argv[1], 'r')
f2 = open(str(sys.argv[1])+'.fasta', 'w')
content = f.readlines()
new=[]
for i in range(1, len(content)):
	new.append(content[i].split())
for i in range(len(new)):
	f2.write('>' + new[i][0] + '\n' + new[i][1] + '\n')
f2.close()
f.close()

	
	 
