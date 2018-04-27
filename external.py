# -*- coding: utf-8 -*-
# To you Alono oh Father, I commit myself

import os
import subprocess

# the directory
directory = 'C:/ProgramData/Anaconda3/'

def run(file, queries=''):

    # change the directory and file to be safe in testing mode
    os.chdir(directory)
    file = 'C:\\index.py'

    # the command
    cmd = "python " + file + " " + queries

    # run the subprocess
    output = subprocess.check_output(cmd, shell=True)

    # return the bin
    return output