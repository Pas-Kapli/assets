echo "begin data;"
echo -n 'dimensions ntax=4 nchar='; echo -n $1; echo ";"
echo "format missing=? gap=- interleave=no datatype=dna;"
echo "options gapmode=missing;"
echo "matrix"
cat $2 | tail -n +2
echo ";"
echo "End;"
echo "begin paup;"
echo -n "    log start replace=yes file="; echo -n $2; echo "_log.txt;"
echo "    set autoclose=yes criterion=parsimony root=outgroup storebrlens=yes increase=auto;"
echo "    hsearch addseq=random nreps=1000 swap=tbr hold=1;"
echo -n "    savetrees file="; echo -n $2; echo ".PAUP.tre format=newick brlens=yes;"
echo "    log stop;"
echo "    quit;"
echo "END;"
