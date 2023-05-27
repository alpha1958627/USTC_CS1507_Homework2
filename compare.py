with open('compare1.txt','r',encoding='utf-8') as   f1:
    lines1=set(f1.readlines())
with open('compare2.txt','r',encoding='utf-8') as   f2:
    lines2=set(f2.readlines())
unique_lines=list((lines1^lines2)-(lines1&lines2))
with open('unique.txt','w',encoding='utf-8') as f:
    for line in unique_lines:
        f.write(line)