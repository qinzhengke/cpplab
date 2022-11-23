import os
import re

root = 'doc'

fpaths = []
folders = {'doc/language':'语言', 'doc/std':'标准库', 'doc/stl':'标准模板库STL'}

table = ['## 目录', '\n']
url_prefix = 'https://github.com/qinzhengke/cpplab/blob/test/'

for root in ['doc/language', 'doc/std', 'doc/stl']:
    for dirpath, dirs, files in os.walk(root):
        table.append('* [' + folders[dirpath] + ']\n')
        titles = []; lvs = []
        for fname in files:
            title = '    * ['
            with open(os.path.join(dirpath, fname), 'r') as f:
                data = f.readlines()
                if data:
                    title = title + data[0][2:-1] + ']('
                    title = title + url_prefix + dirpath + '/' + fname + ')\n'
                    res = re.search('实验([0-9]+)', data[0])
                    lvs.append(int(res.group(1)))
                    titles.append(title)
        titles = [x for _,x in sorted(zip(lvs,titles))]
        for t in titles: print(t)
        table = table + titles

with open('README.md') as f:
    data = f.readlines()
    beg = 0
    end = len(data)
    for i, l in enumerate(data):
        if re.match('## 目录', l):
            beg = i
        elif beg != 0 and re.match('##', l):
            end = i

before = data[0:beg]
after = data[end:]
final = before + table + after

with open('README.md', 'w') as f:
    f.writelines(final)
