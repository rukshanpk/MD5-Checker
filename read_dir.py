#!/usr/bin/env python
import os
import sys


def read_filenames(directory):
    try:
        file_names = os.listdir(directory)
        return file_names
    except:
        print("Please use the linux format")
