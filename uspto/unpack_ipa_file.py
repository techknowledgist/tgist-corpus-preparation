"""unpack_ipa_file.py

Take one of the USPTO files and create a directory structure with individual XML
files.

Note that the PTO files themselves are concatenations of XML files.

Usage:

   $ python unpack_ipa_file.py SOURCE

SOURCE is something like 'ipa180104' and refers to the weekly data releases from
the USPTO. The code here is geared towards the full text releases without images
that can be downloaded from http://patents.reedtech.com/parbft.php.

This can run on either the zipfile that was downloaded or the single file that
was contained in the zip. For example, if the source was 'ipa180104' then this
would take as input either 'ipa180104.xml' if it is available (since it would be
faster) or it would take 'ipa180104'.zip' as input.

Output is written to a new directory that lives in the same directory as the
source file.

For this to run you may have to edit the USPTO_DIR variable, which also drives
where output is being written.

"""


import os
import sys
import time
import zipfile
import StringIO


USPTO_DIR = '/DATA/resources/corpora/uspto/2018/'
USPTO_DIR = '/home/j/corpuswork/corpora/uspto/2018/'


def flush(string_buffer, source, file_name, directory):
    if file_name is not None:
        contents = string_buffer.getvalue()
        short_path = "%04d/%s.xml" % (directory, file_name)
        long_path = "%s/%s/%04d/%s.xml" % (USPTO_DIR, source, directory, file_name)
        dir_name = "%s/%s/%04d" % (USPTO_DIR, source, directory)
        #print "%s %d" % (short_path, len(contents))
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        open(long_path, 'w').write(contents)


def get_filename(line):
    idx = line.find(' file="')    
    file_name = line[idx:].split()[0]
    return file_name[6:file_name.find('-')]


def open_file(xml_file, zip_file):
    if os.path.exists(xml_file):
        fh = open(xml_file)
    else:
        archive = zipfile.ZipFile(zip_file)
        xml_file = archive.namelist()[0]
        fh = archive.open(xml_file)
    return fh
    
    
def process(source):

    fh = open_file(USPTO_DIR + source + '.xml',
                   USPTO_DIR + source + '.zip')
    
    string_buffer = StringIO.StringIO()
    file_name = None
    line_count = 0
    file_count = 0
    dir_count = 1

    for line in fh:

        line_count += 1
        if line_count % 100000 == 0:
            print line_count
        #if line_count > 10000: break

        if line.startswith('<?xml version="1.0" encoding="UTF-8"?>'):
            file_count += 1
            if file_count % 100 == 0:
                dir_count +=1
            flush(string_buffer, source, file_name, dir_count)
            string_buffer = StringIO.StringIO()
        elif line.startswith('<us-patent-application '):
            file_name = get_filename(line)
        string_buffer.write(line)

    file_count += 1
    if file_count % 100 == 0:
        dir_count +=1
    flush(string_buffer, source, file_name, dir_count)


if __name__ == '__main__':
    
    t0 = time.time()
    source_file = sys.argv[1] if len(sys.argv) > 1 else 'ipa180104'
    process(source_file)
    print "\nTIME ELAPSED: %.4f seconds\n" % (time.time() - t0)
