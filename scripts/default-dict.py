#!/usr/bin/env python
"""
Defaultdict
"""
from collections import defaultdict

d = defaultdict(list)
d['python'].append('2.7')
d['python'].append('3.8')
d['go'].append('1.12')

for k,v in d.items():
    print(f'{k}: {v}')

    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   

new_files = defaultdict(list)

def group_by_owners(files):
    for k,v in files.items():
        new_files[v].append(k)

    return dict(new_files)

print(group_by_owners(files))