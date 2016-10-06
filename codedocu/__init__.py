# -*- coding: utf-8 -*-
import glob, os
import fnmatch
import itertools

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
        com_found = False
        j=0
        comment_dict[match.split('/')[-1]] = {}
        with open(match, 'r') as f:
            for line  in f:
                if 'class' in line:
                    lines = []
                    temp = line
                    comment_dict[match.split('/')[-1]][temp.replace('class ', '').replace(':','')]=''
                    for _ in xrange(5):
                        try:
                            line = f.next()
                            if '"""' not in line:
                                break
                            elif '"""' in line:
                                line = f.next()
                                while '"""' not in line:
                                    try:
                                        lines.append(line)
                                        line=f.next()
                                    except StopIteration:
                                        break
                                continue
                        except StopIteration:
                            break
                    print 'lines appended', ''.join(x for x in lines)
                    comment_dict[match.split('/')[-1]][temp.replace('class ','' )] = ''.join(x for x in lines)
                else:
                    continue
    return comment_dict

if __name__ == '__main__':
    print first()
