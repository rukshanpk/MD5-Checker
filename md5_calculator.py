import hashlib
import os


def md5_calculator(full_path):
    try:
        with open(full_path, "rb") as f:
            chunk_num_blocks = 128
            file_hash = hashlib.md5()
            for chunk in iter(lambda: f.read(chunk_num_blocks*file_hash.block_size), b''):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except:
        return "0000000000000000000000"
