"""create_filelist.py

Given a directory as created by unpack_ipa_file.py, create a file list from the
directory.

Usage:

   $ python create_filelist.py SOURCE

SOURCE is something like 'ipa180104' and refers to the weekly data releases from
the USPTO. Output is written to a file named file-SOURCE.txt.

The directory where the source is expected is hard-coded in the USPTO_DIR
variable, which may need to be edited.

The output file created is exactly like the files required by the tgist-features
code. That is, it has tab-separated lines with year, long path and short path.

"""


import os
import sys
import glob


USPTO_DIR = '/DATA/resources/corpora/uspto/2018/'
USPTO_DIR = '/home/j/corpuswork/corpora/uspto/2018/'

YEAR = 2018

def process(source):

    fh = open("files-%s.txt" % source, 'w')
    for directory in glob.glob("%s/????" % (USPTO_DIR + source)):
        last_element = os.path.split(directory)[1]
        for fname in os.listdir(directory):
            long_path = os.path.join(directory, fname)
            short_path = os.path.join(last_element, fname)
            fh.write("%s\t%s\t%s\n" % (YEAR, long_path, short_path))


if __name__ == '__main__':
    
    source = sys.argv[1] if len(sys.argv) > 1 else 'ipa180104'
    process(source)
