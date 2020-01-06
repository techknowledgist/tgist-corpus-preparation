# corpus creation and processing

export FILES=/Users/marc/Desktop/projects/fuse/code/techknowledgist/tgist-corpus-preparation/dtriac/files.txt

export CORPUS=/DATA/dtra/dtriac/dtriac-19d/corpus

python step1_init.py -f $FILES -c $CORPUS --source text
