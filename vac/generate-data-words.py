import mylib.fileapi as fileapi
import vac.models as models
from vac.models import VChar,VWord
import vac.config as config
import mylib.html as html
import mylib.regex as regex
import datetime

import os

def removeMultiSpace(s):
    for c in "?!;.…":
        while c in s:
            s = s.replace(c, "\n")
    while "  " in s:
        s = s.replace("  ", " ")

    for c in ",:`'’\":/\\{}[]@#$%^&*()-_+=~<>|":
        while c in s:
            s = s.replace(c, " ")
    while '”' in s:
        s = s.replace('”', " ")
    while "  " in s:
        s = s.replace("  ", " ")

    while "\n\n" in s:
        s = s.replace("\n\n", "\n")
    while "\t\t" in s:
        s = s.replace("\t\t", "\t")
    while "\t" in s:
        s = s.replace("\t", " ")
    return s

vword = VWord()
vword.load(config.words_index_csv)
#vchar = VChar()
#print(vchar.index('a'))
#print(vchar.list_index('AaOoEeIiUuYy'))


files = os.listdir(config.htmls_folder)

count = 0
for file in files:

    content = fileapi.readFile(config.htmls_folder + "/" + file)
    content = html.strip_tags(content)


    content = regex.searchStringG1DOTALL(r"(Full.*Full)",content)
    content = removeMultiSpace(content)
    lines = content.split('\n')

    sfile = ""
    for line in lines:
        line = vword.lower(line)

        words = line.split(' ')

        margin = 30
        maxrecords = 1000000
        for i in range(0, len(words)):
            w = words[i]
            if len(vword.correct(w)) == 0:
                continue
            indtarget = vword.getInternalIndex(w)
            if indtarget == 0:
                continue
            j = i - margin

            lsInds = []

            countspace = 0
            while j <= i + margin:
                if j == i:
                    #do nothing
                    uw = vword.unaccent(w)
                    indmain = vword.getIndex(uw)
                elif j >= 0 and j < len(words):
                    ind = vword.getIndex(words[j])
                    lsInds = lsInds + [ind]
                else:
                    lsInds = lsInds + [0]
                    countspace = countspace + 1
                j = j + 1
            #print(c, s.replace("\n", ""))
            if countspace < margin:
                sfile = str(indmain) + "," + str(lsInds).replace("[","").replace("]", "") + ", " + str(indtarget) + "\n"
                indmain = vword.getIndex(uw)
                count = count + 1
                filename = config.words_folder + "/" + str(indmain) + "_" + uw + ".csv"
                fileapi.appendFile(filename, sfile)

    print(datetime.datetime.now(), "update by " + file)

