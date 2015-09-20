#!/usr/bin/env python

import sys
from pathlib import Path

powerpoint = ['.ppt']
images = ['png', 'jpg', 'jpeg']
archives = ['.zip', '.rar', '.tar.gz']
documents = ['.pdf', '.djvu' , '.doc', '.docx']

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.stderr.write('Usage: organize_downloads.py path\n')
        sys.exit(1)

    root = Path(sys.argv[1])
    files = (Path(path) for path in root.iterdir() if path.is_file())
    
    for file in files:
        if file.suffix in powerpoint:
            file.rename('{}/powerpoint/{}'.format(file.parents[0], file.name))
        elif file.suffix in archives:
            file.rename('{}/archives/{}'.format(file.parents[0], file.name))
        elif file.suffix in documents:
            file.rename('{}/documents/{}'.format(file.parents[0], file.name))

        
