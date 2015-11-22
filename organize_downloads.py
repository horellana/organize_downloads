#!/usr/bin/env python

import sys
import json
from pathlib import Path

class UnknownSuffix(Exception):
    pass

def prepare_root(root, directories):
    for directory in directories:
        new_dir = Path(root, directory)
        if not new_dir.exists():
            sys.stdout.stderr('Creating directory: {}\n'.format(new_dir.as_posix()))
            new_dir.mkdir()

def get_config(file):
    with open(file, 'r') as f:
        return json.load(f)['config']

def get_folder(ext, config):
    for folder, extension in config.items():
        if ext in extension:
            return folder
    raise UnknownSuffix('Unkown suffix: {}\n'.format(ext))

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        sys.stderr.write('Usage: organize_downloads.py config-file downloads-path\n')
        sys.exit(1)

    root = Path(sys.argv[2])
    config = get_config(sys.argv[1])

    prepare_root(root, config.keys())

    files = (Path(path) for path in root.iterdir() if path.is_file())

    for file in files:
        try:
            suffix = file.suffix
            root = file.parents[0]
            folder = get_folder(suffix, config)

            sys.stdout.write('{file} => Moving: {root}/{folder}/{name}\n'
                             .format(file=file,
                                     root=file.parents[0],
                                     folder=folder,
                                     name=file.name))

            file.rename('{root}/{folder}/{file}'.format(root=file.parents[0],
                                                        folder=folder,
                                                        file=file.name))
        except UnknownSuffix as err:
            sys.stderr.write('{} => {}'.format(file.as_posix(), err))
