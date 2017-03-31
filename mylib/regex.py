import re

def searchStringG1(pattern, s):
    m = re.search(pattern, s)
    if m!=None:
        return m.group(1)
    return ""

def searchStringG1DOTALL(pattern, s):
    m = re.search(pattern, s, re.DOTALL)
    if m!=None:
        return m.group(1)
    return ""

def findAll(pattern, s):
    m = re.findall(pattern, s)
    return m

def findAllDOTALL(pattern, s):
    m = re.findall(pattern, s, re.DOTALL)
    return m

def replace(pattern, s1, s2):
    matchs = re.findall(pattern, s1)
    for m in matchs:
        s1 = s1.replace(m, s2)
    return s1