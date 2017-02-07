"""
author: phaesoo
e-mail: phaesoo@gmail.com
description: for copy load combination files
version: python 3.5.2
"""

import os
import shutil
from distutils.dir_util import copy_tree

err_msg = 'invalid directory path'

# get src path
src = input("Input src path : ").lower()
if not os.path.isdir(src):
    raise AssertionError(err_msg)

# split drive from src path
temp = os.path.splitdrive(src)

dirs = temp[1].split('\\')
if dirs[-2] != 'rc' and dirs[-2] != 'steel':
    raise AssertionError(err_msg)

# find 'bin' index
index_bin = dirs.index('bin')

# common path
common_path = temp[0] + os.sep + os.path.join(*dirs[:index_bin + 1])

# variable path
var_path = ['vc90\\Debug\\x64\\Design\\LoadCombination',
            'vc90\\Debug\\x86\\Design\\LoadCombination',
            'vc90\\Release\\x64\\Design\\LoadCombination',
            'vc90\\Release\\x86\\Design\\LoadCombination',
            'vc110\\Debug\\x64\\Design\\LoadCombination',
            'vc110\\Debug\\x86\\Design\\LoadCombination',
            'vc110\\Release\\x64\\Design\\LoadCombination',
            'vc110\\Release\\x86\\Design\\LoadCombination', ]

# make destination path
dst_list = []
for var in var_path:
    dst = os.path.join(common_path, var, *dirs[-2:]).lower()
    if not os.path.isdir(dst):
        AssertionError("invalid dst path")
    dst_list.append(dst)

# exception
try:
    idx = dst_list.index(src)
    del dst_list[idx]
except:
    raise AssertionError(err_msg)

# remove & copy
for dst in dst_list:
    shutil.rmtree(dst)
    copy_tree(src, dst.upper())
    print("Copy Success : " + dst)
