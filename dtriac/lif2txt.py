"""lif2txt.py

Creating text files from lif files.

Using LIF_DIR and TXT_DIR as input and output directories.

Assumes standard dtriac-19d directory structure.

"""

import os
import json
import codecs

LIF_DIR = '/DATA/dtra/dtriac/dtriac-19d/lif'
TXT_DIR = '/DATA/dtra/dtriac/dtriac-19d/txt'

if not os.path.exists(TXT_DIR):
    os.mkdir(TXT_DIR)

c = 0
for fname in os.listdir(LIF_DIR):
    if fname.isdigit():
        c += 1
        #if c > 10: break
        lif_path = os.path.join(LIF_DIR, fname, 'tesseract-300dpi-20p.lif')
        txt_path = os.path.join(TXT_DIR, fname, 'tesseract-300dpi-20p.txt')
        print '%06d  Creating' % c, txt_path
        subdir = os.path.join(TXT_DIR, fname)
        if not os.path.exists(subdir):
            os.mkdir(subdir)
        json_obj = json.load(open(lif_path))
        text = json_obj['payload']['text']['@value']
        out = codecs.open(txt_path, 'w', encoding='utf8')
        out.write(text)
        
