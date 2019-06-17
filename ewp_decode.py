#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET

lines = open(sys.argv[1]).readlines()
root = ET.fromstringlist(lines[1:])

def nameof(r):
    return r.find('name').text

def filesof(r):
    ret = []
    for f in r.findall('file'):
        if not f.findall('excluded'):
            ret.append(nameof(f))
    return ret

def extract_common_path(files):
    retpath = []
    files = [f.split('/') for f in files]
    if len(files)==1:
        "special case"
        return '/'.join(files[0][:-1]),[files[0][-1]]
    while files and all(files):
        if len(set(f[0] for f in files)) > 1:
            break
        retpath.append(files[0][0])
        files = [f[1:] for f in files]

    ret = '/'.join(retpath)
    return ret, ['/'.join(f) for f in files]

def fixup(f):
    f = f.replace('$PROJ_DIR$','$(SRC_DIR)')
    f = f.replace('\\','/')
    return f

files = filesof(root)


# group stuff.  IAR leepp
group_defines=[] # key, value pairs

for g in root.findall('group'):
    groupname = nameof(g)
    groupfiles = map(fixup,filesof(g))
    group_common, groupfiles = extract_common_path(groupfiles)
    dir_name = (groupname+'_dir').upper().replace(' ','_')
    group_defines.append((dir_name,group_common))

    files += ["$(%s)/%s"%(dir_name,f) for f in groupfiles]

for k,v in group_defines:
    print("%s := %s"%(k,v))

def filter_ext(files, ext):
    return [f for f in files if f.endswith(ext)]

def source_files(files):
    return (filter_ext(files, '.c') +
            filter_ext(files, '.cpp') +
            filter_ext(files, '.c++'))

for f in sorted(map(fixup, source_files(files))):
    print("SOURCE_FILES +=",f)
# project, = root.findall('project')
