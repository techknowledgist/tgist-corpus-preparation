"""create_commands.py

Convenience script to print the commands that we need to create corpora and
extract features. The most useful part here is that this script takes care of
the size of the corpora. That is, it will create things like

   python step2_process.py -c USPTO/2018/ipa180104 --tag2chk -n 7823

Just run it without command line arguments. You may was to edit the CORPORA or
YEAR variables. The script assumes file lists created by create_filelist.py and
it expects those lists to be in the current directory.

Commands are printed to the standard output.

"""


import os
import glob


CWD = os.getcwd()
CORPORA = '/home/j/corpuswork/techwatch/corpora/USPTO'
YEAR = 2018

INIT = "python step1_init.py --data uspto -f %s -c %s"
POPULATE = "python step2_process.py -c %s --populate -n %d"
XML2TXT = "python step2_process.py -c %s --xml2txt -n %d"
TXT2TAG = "python step2_process.py -c %s --txt2tag -n %d"
TAG2CHK = "python step2_process.py -c %s --tag2chk -n %d"


for fname in glob.glob("files-*.txt"):
    with open(fname) as fh:
        size = len(fh.readlines())
        filelist = os.path.join(CWD, fname)
        corpus = os.path.join(CORPORA, str(YEAR), fname[6:-4])
        print INIT % (filelist, corpus)
        print POPULATE % (corpus, size)
        print XML2TXT % (corpus, size)
        print TXT2TAG % (corpus, size)
        print TAG2CHK % (corpus, size)
        print
