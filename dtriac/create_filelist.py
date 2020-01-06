"""create_filelist.py

Create a file list given a directory with DTRIAC-19d files.

Usage:

   $ python create_filelist.py

"""


import os


DIR = '/DATA/dtra/dtriac/dtriac-19d/lif'


def process():

    for fname in os.listdir(DIR):
        if fname.isdigit():
            long_path = os.path.join(DIR, fname, 'tesseract-300dpi-20p.txt')
            short_path = os.path.join(fname, 'tesseract-300dpi-20p.txt')
            long_path = long_path.replace('/lif/', '/txt/')
            print("9999\t%s\t%s" % (long_path, short_path))


if __name__ == '__main__':

    process()
