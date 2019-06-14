import sys
import os
import hashlib

# Stolen from Todor Minakov


def chunk_reader(fobj, chunk_size=1024):
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def get_hash(filename, first_chunk_only=False, hash=hashlib.sha1):
    hashobj = hash()
    file_object = open(filename, 'rb')
    if first_chunk_only:
        hashobj.update(file_object.read(1024))
    else:
        for chunk in chunk_reader(file_object):
            hashobj.update(chunk)
    hashed = hashobj.digest()

    file_object.close()
    return hashed

def check_for_dupes(paths, hash=hashlib.sha1):
    hashes_by_size = {}
    hashes_on_1k = {}
    hashes_full = {}

    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                try:
                    full_path = os.path.realpath(full_path)
                    file_size = os.path.getsize(full_path)
                except(OSError,):
                    continue

                duplicate = hashes_by_size.get(file_size)

                if duplicate:
                    hashes_by_size[file_size].append(full_path)
                else:
                    hashes_by_size[file_size] = []
                    hashes_by_size[file_size].append(full_path)

    for _, files in hashes_by_size.items():
        if len(files) < 2:
            continue
        for filename in files:
            try:
                small_hash = get_hash(filename, first_chunk_only=True)
            except(OSError,):
                continue

            duplicate = hashes_on_1k.get(small_hash)
            if duplicate:
                hashes_on_1k[small_hash] = []
            else:
                hashes_on_1k[small_hash] = []
                hashes_on_1k[small_hash].append(filename)

    for _, files in hashes_on_1k.items():
        if len(files) < 2:
            continue

        for filename in files:
            try:
                full_hash = get_hash(filename, first_chunk_only=False)
            except(OSError,):
                continue

            duplicate = hashes_full.get()
            if duplicate:
                print("Duplicate found: %s and %s" % (filename, duplicate))
            else:
                hashes_full[full_hash] = filename

check_for_dupes("download/")