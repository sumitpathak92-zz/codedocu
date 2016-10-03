# -*- coding: utf-8 -*-
import glob, os
import fnmatch
import itertools

new_matches=[]
path = '/var/www/alps/'
#def hello():
#    return "Currently its in the initial phase"
def first():
    new_matches=[]
    path='/var/www/alps/'
    comment_dict = dict()
    os.chdir(path)
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.py'):
            matches.append(os.path.join(root, filename))
    for match in matches:
        match = match.split('/')[-1]
        new_matches.append(match)
    for match in matches:
        lines=[]
        com_found = False
        j=0
        comment_dict[match.split('/')[-1]] = {}
        with open(match, 'r') as f:
            for i, line  in enumerate(f):
                if '"""' in line:
                    lines.append(i)
                if len(lines)==2:
                    print lines
                    com_found = True
                    break
        if com_found:
            with open(match, 'r') as f:
                for line in itertools.islice(f, lines[0], lines[1]):
                    j+=1
                    comment_dict[match.split('/')[-1]][j] = line
    return comment_dict

if __name__ == '__main__':
    first()
