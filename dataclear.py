import re
import os

root_path = "/Users/songdi/Downloads/egret-wenda-corpus-master/egret_wenda_lines.txt"

with open(root_path,'r') as f:
    lines = f.readlines()
cnt = 1
for line in lines:
    question = re.search('\S \+\+\+\$\+\+\+ (.*?) \+\+\+\$\+\+\+ (.*)',line)
    if cnt%2 == 1:
        with open("/Users/songdi/Downloads/egret-wenda-corpus-master/text.txt",'a') as f:
            f.write(question.group(2)+'\n')
    cnt = cnt+1
print("----------------------")
for line in lines:
    annser = re.search('\s\s-\s(.*)',line)
    if annser is not None:
        print(annser.group(1))

