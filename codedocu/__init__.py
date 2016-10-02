# -*- coding: utf-8 -*-
import glob, os
import fnmatch
import itertools

matches=[]
new_matches=[]
lines=[]
comment_dict = {}
path = '/var/www/alps/'
j=0
#def hello():
#    return "Currently its in the initial phase"
def first():
    comment_dict = dict()
    os.chdir(path)
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.py'):
            matches.append(os.path.join(root, filename))
    print "matchcount is", len(matches)
    print "matches are", matches
    for match in matches:
        match = match.split('/')[-1]
        new_matches.append(match)
    print new_matches
    j=0
    print "****",j
    print "%%%%%", comment_dict
    for match in matches:
        if match.endswith('content_gap_analysis.py'):
            with open(match, 'r') as f:
                for i, line  in enumerate(f):
                    if '"""' in line:
                        lines.append(i)
                    if len(lines)==2:
                        break
            with open(match, 'r') as f:
                for line in itertools.islice(f, lines[0], lines[1]):
                    j+=1
                    comment_dict[j] = line
    print comment_dict
    return comment_dict
