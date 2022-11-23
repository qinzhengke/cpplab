import os
import re

root = 'doc'

all_fpaths = []

lvs_rank = {'特 性':0, '规 则':1, '语法糖':2}
for root in ['doc/language', 'doc/std', 'doc/stl']:
    lvs = []; fpaths = []
    for dirpath, dirs, files in os.walk(root):
        for fname in files:
            with open(os.path.join(dirpath, fname), 'r') as f:
                data = f.readlines()
                if data:
                    res = re.search('((特 性)|(规 则)|(语法糖))', data[0])
                    lvs.append(lvs_rank[res.group(1)])
                    fpaths.append(os.path.join(dirpath, fname))
    fpaths = [x for _,x in sorted(zip(lvs,fpaths))]
    all_fpaths = all_fpaths + fpaths

for i, fpath in enumerate(all_fpaths):
    data = []


for i, fpath in enumerate(all_fpaths):
    data = []
    with open(fpath, 'r') as f:
        data = f.readlines()
        if data:
            data[0] = re.sub('实验[0-9]+', '实验'+str(i), data[0])
    with open(fpath, 'w') as f:
        f.writelines(data)