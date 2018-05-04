"""create_filelist.py

Create a file list given a directory with Thyme files.

Usage:

   $ python create_filelist.py dev|test|train

The directory where the source is expected is hard-coded in the THYME_DIR
variable, which may need to be edited. The command line argument selects one of
the splits of the corpus (train is used as default if no split is given).

The output file created is exactly like the files required by the tgist-features
code. That is, it has tab-separated lines with year, long path and short path.

"""


import os
import sys


THYME_DIR = '/DATA/resources/corpora/thyme/THYME-corpus'


def process(split):

    fh = open("thyme-files-%s.txt" % split, 'w')
    directory = os.path.join(THYME_DIR, 'TextData', split)
    for fname in os.listdir(directory):
        year = get_year(directory, fname)
        long_path = os.path.join(directory, fname)
        short_path = os.path.join(fname)
        fh.write("%s\t%s\t%s\n" % (year, long_path, short_path))


def get_year(directory, fname):
    
    # TODO: not sure if this actually does the right thing
    long_path = os.path.join(directory, fname)
    if fname.startswith('ID'):
        with open(long_path) as fh:
            first_line = fh.readline()
            year = first_line.split()[1][-5:-1]
    else:
        year = '9999'
    return year

    
if __name__ == '__main__':

    split = sys.argv[1] if len(sys.argv) > 1 else 'train'
    process(split)
