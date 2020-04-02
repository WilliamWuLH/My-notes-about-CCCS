import os
import sys
path = 'F:\My-notes-about-CCCS'
files = os.listdir(path)
old = 'F:\My-notes-about-CCCS'
new = '.\image'
for file in files:
    if 'sion.md' in file:
        print(file)
        mdpath = 'F:\My-notes-about-CCCS\\' + file
        filedata = ''
        with open(mdpath,'r',encoding="utf-8") as mdfile:
            for line in mdfile:
                if old in line:
                    line = line.replace(old,new)
                    print(line)
                filedata += line
        with open(mdpath,'w',encoding='utf-8') as mdfile:
            mdfile.write(filedata)
        