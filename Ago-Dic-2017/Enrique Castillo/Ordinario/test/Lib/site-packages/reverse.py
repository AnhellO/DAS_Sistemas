#!/usr/bin/env python
# encoding: utf-8

'''
Reverse the content of a file, write into another file.

Example 1:

$ cat foo.txt
Hello.
$ python reverse.py foo.txt foo.txt.rev
$ cat foo.txt.rev
.olleH
$ python reverse.py foo.txt.rev foo.txt.new
$ cat foo.txt.new
Hello.

Example 2:

$ python
>>> import reverse
>>> reverse.reverse_file('foo.txt', 'foo.txt.rev')
>>> reverse.reverse_file('foo.txt.rev', 'foo.txt.new')
>>> open('foo.txt').read() == open('foo.txt.new').read()
True

'''

import sys

__appname__ = "reverse"
__author__ = "physacco"
__version__ = "0.1.0"
__license__ = "MIT"

CHUNK_SIZE = 1024 * 16

def split_size(size):
    '''Split the file size into several chunks.'''
    rem = size % CHUNK_SIZE
    if rem == 0:
        cnt = size // CHUNK_SIZE
    else:
        cnt = size // CHUNK_SIZE + 1

    chunks = []
    for i in range(cnt):
        pos = i * CHUNK_SIZE
        if i == cnt - 1:
            disp = size - pos
        else:
            disp = CHUNK_SIZE
        chunks.append((pos, disp))
    return chunks

def reverse_fd(inf, outf):
    '''Reverse the content of inf, write to outf.
    Both inf and outf are file objects.
    inf must be seekable.
    '''
    inf.seek(0, 2)
    size = inf.tell()
    if not size:
        return

    chunks = split_size(size)
    for chunk in reversed(chunks):
        inf.seek(chunk[0], 0)
        data = inf.read(chunk[1])
        if len(data) != chunk[1]:
            raise IOError('incomplete I/O operation')
        outf.write(data[::-1])

def reverse_file(infile, outfile):
    '''Reverse the content of infile, write to outfile.
    Both infile and outfile are filenames or filepaths.
    '''
    with open(infile, 'rb') as inf:
        with open(outfile, 'wb') as outf:
            reverse_fd(inf, outf)

def show_usage():
    '''Show usage.'''
    sys.stdout.write('''Usage: reverse [options] infile outfile

Options:
    -h, --help                    Show this help message and exit
    -v, --version                 Show version message and exit
''')

def show_version():
    '''Show version.'''
    sys.stdout.write('reverse %s\n' % __version__)

def main():
    '''Script entry point.'''
    import getopt

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hv', ['help', 'version'])
    except getopt.GetoptError as err:
        sys.stderr.write('Error: %s\n' % err)
        exit(2)

    for opt, _ in opts:
        if opt in ['-h', '--help']:
            show_usage()
            exit()
        elif opt in ['-v', '--version']:
            show_version()
            exit()

    if len(args) != 2:
        show_usage()
        exit(1)

    infile, outfile = args
    if infile == outfile:
        sys.stderr.write('Error: outfile must differ from infile\n')
        exit(3)

    reverse_file(infile, outfile)
    sys.stdout.write('Successfully written to %s\n' % outfile)

if __name__ == '__main__':
    main()
